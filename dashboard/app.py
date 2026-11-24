import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng
from datetime import time




#different pages

# Define pages
home = st.Page("app.py", title="🏠Home", default=True)
page1 = st.Page("page_1.py", title="📄Page 1")
page2 = st.Page("page_2.py", title="📄Page 2")

# Navigation
pg = st.navigation([home, page1, page2])



# Sidebar
with st.sidebar:
    st.title("Overview")





st.title("Somnia dashboard")

period = st.select_slider(
    "Select how many hours you're planning to sleep",
    options=[
        "5h",
        "6h",
        "7h",
        "8h",
        "9h",
        "10h",
        "11h",
    ],
    key="sleep_hours_slider"
)



#Alarm
t = st.time_input(
    "Set an alarm for",
    time(8, 45),
    key="alarm_time"
)

st.write("Alarm is set for", t)



#charts

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "28°C", "-9°C", border=True)
b.metric("Humidity", "35%", "5%", border=True)

c.metric("Light", "200 lux", "-50 lux", border=True)
d.metric("Noise", "35 dBA", "5 dBA", border=True)

col1, col2= st.columns(2)

with col1:
    df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
    st.line_chart(df)

with col2:
    st.header("Tonight's summary")

