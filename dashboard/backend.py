from collections import deque
from datetime import datetime
import threading
import time

from fastapi import FastAPI
from grove.adc import ADC
import seeed_dht
import uvicorn

app = FastAPI()

# --- Hardware Configuration ---
DHT_TYPE = "22"      # Matches seeed_dht.DHT("22", 5) in your test script
DHT_PIN = 5
LIGHT_CHANNEL = 0    # Matches adc.read(0)
SOUND_CHANNEL = 2    # Change to the ADC port you used for test_sound_sensor.py

# Initialize sensors once
dht_sensor = seeed_dht.DHT(DHT_TYPE, DHT_PIN)
adc = ADC(address=0x08)

# --- In-Memory Rolling Buffers (Last 20 readings) ---
MAX_POINTS = 20
temp_history = deque(maxlen=MAX_POINTS)
humidity_history = deque(maxlen=MAX_POINTS)
light_history = deque(maxlen=MAX_POINTS)
noise_history = deque(maxlen=MAX_POINTS)
events_log = deque(maxlen=10)

start_time = datetime.now()
data_lock = threading.Lock()


def log_event(description: str, value: str, icon: str):
    now_str = datetime.now().strftime("%H:%M")
    events_log.appendleft({
        "time": now_str,
        "description": description,
        "value": value,
        "icon": icon,
    })


def sensor_polling_loop():
    """Background thread that reads all 3 Grove sensors every second."""
    log_event("Monitoring started", "", "🟢")

    while True:
        try:
            humi, temp = dht_sensor.read()
            light_val = adc.read(LIGHT_CHANNEL)
            sound_val = adc.read(SOUND_CHANNEL)

            # DHT sensors occasionally return None if polled too quickly
            if humi is not None and temp is not None:
                with data_lock:
                    prev_temp = temp_history[-1] if temp_history else temp
                    prev_light = light_history[-1] if light_history else light_val
                    prev_sound = noise_history[-1] if noise_history else sound_val

                    temp_history.append(round(float(temp), 1))
                    humidity_history.append(round(float(humi), 1))
                    light_history.append(int(light_val))
                    noise_history.append(int(sound_val))

                    # Trigger threshold events matching your Somnia dashboard
                    if light_val - prev_light > 50:
                        log_event("Light increase detected", f"{light_val} units", "🟡")
                    if sound_val - prev_sound > 40:
                        log_event("Noise peak detected", f"{sound_val} units", "🟣")
                    if temp - prev_temp >= 0.5:
                        log_event("Temperature increase", f"+{round(temp - prev_temp, 1)} °C", "🔵")

        except Exception as e:
            print(f"Sensor read error: {e}")

        time.sleep(1)


@app.on_event("startup")
def start_sensors():
    thread = threading.Thread(target=sensor_polling_loop, daemon=True)
    thread.start()


@app.get("/")
def index():
    return {"status": "Somnia Pi 5 API running"}


@app.get("/dashboard")
def get_dashboard_data():
    with data_lock:
        t_list = list(temp_history) or [0.0]
        h_list = list(humidity_history) or [0.0]
        l_list = list(light_history) or [0]
        n_list = list(noise_history) or [0]
        ev_list = list(events_log)

    def calc_delta(series, unit=""):
        if len(series) < 2:
            return f"0{unit}"
        diff = round(series[-1] - series[-2], 1)
        sign = "+" if diff > 0 else ""
        return f"{sign}{diff}{unit}"

    elapsed_hours = max(1, round((datetime.now() - start_time).total_seconds() / 3600))

    return {
        "metrics": {
            "temperature": {
                "value": f"{t_list[-1]} °C",
                "delta": calc_delta(t_list, " °C"),
                "history": t_list,
            },
            "humidity": {
                "value": f"{h_list[-1]}%",
                "delta": calc_delta(h_list, "%"),
                "history": h_list,
            },
            "light": {
                "value": f"{l_list[-1]} units",
                "delta": calc_delta(l_list, " units"),
                "history": l_list,
            },
            "noise": {
                "value": f"{n_list[-1]} units",
                "delta": calc_delta(n_list, " units"),
                "history": n_list,
            },
        },
        "graph": {
            "Temperature": t_list,
            "Humidity": h_list,
            "Noise": n_list,
        },
        "summary": {
            "duration": f"{elapsed_hours}H",
            "avg_temp": f"{round(sum(t_list) / len(t_list), 1)} °C",
            "avg_sound": f"{round(sum(n_list) / len(n_list))} units",
            "avg_humidity": f"{round(sum(h_list) / len(h_list))}%",
        },
        "events": ev_list,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)