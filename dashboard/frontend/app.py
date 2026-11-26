import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng
from datetime import datetime






page_element="""
<style>
.stApp {
background-image: url("https://images.pexels.com/photos/8417258/pexels-photo-8417258.jpeg");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}
.st-key-my_blur_box {filter: blur(4px);}
</style>
"""
st.markdown(page_element, unsafe_allow_html=True)

st.set_page_config( # --> configuring the page
    page_title="weatherlive",
    page_icon="🌦️",
    layout="wide",
)
# top bar
top_col1, top_col2 = st.columns(2)
top_col1.header("Somnia dashboard")
date = datetime.now().strftime("%a %d %b %Y")


date_content = [date, ]
date_col1, date_col2 = top_col2.columns(2)
date_col1.badge("Device online", width="stretch", color="green")
date_col2.subheader(f":blue[{date}]", text_alignment="right",)

#different pages

# side bar
home = st.Page("app.py", title="🏠Home", default=True)
page1 = st.Page("page_1.py", title="📄Page 1")
page2 = st.Page("page_2.py", title="📄Page 2")

# Navigation
#pg = st.navigation([home, page1, page2])



# Sidebar
with st.sidebar:
    st.title("Overview")







changes = list(rng(4).standard_normal(20))
data = [sum(changes[:i]) for i in range(20)]
delta = round(data[-1], 2)


col1, col2, col3, col4 = st.columns(4, gap="medium", border=True)

with col1:
    st.metric("Temperature", "21.5 °C", "+0.2 °C",
              chart_data=[1,2,3,2,1,5],
              chart_type="line", border=True)

with col2:
    st.metric("Humidity", "45%", "-1%",
              chart_data=[1,2,3,2,1,5],
              chart_type="line", border=True)

with col3:
    st.metric("Light", "12 lux", "-3 lux",
              chart_data=[1,2,3,2,1,5],
              chart_type="line", border=True)

with col4:
    st.metric("Noise", "28 dB", "+2 dB",
              chart_data=[1,2,3,2,1,5],
              chart_type="line", border=True)
    
    
    
col1, col2= st.columns([3,1], border=True)

with col1:
    st.header("Graph")
    df = pd.DataFrame(rng(0).standard_normal((20, 4)), columns=["Temp", "Hum", "Lum", "sound"])
    st.line_chart(df)


summmary = [
    ("Environment condition", "Good"),
    ("Monitoring duration", "8H"),
    ("Average temperature", "25°C"),
    ("Average sound intensity", "19 units"),
    ("Average humidity", "20%")
]
Sensors_condition = [
    ("Temp & Hum", "Online"),
    ("Sound", "Off"),
    ("Light", "Online")
]
with col2:
    st.subheader("Tonight's activity")
    activity_container = st.container(border=True)
    with activity_container:
            for description, value in summmary:
                summ_col1, summ_col2 = st.columns([3, 1])
                with summ_col1:
                            st.write(description)
                with summ_col2:
                            st.badge(value, color="orange")
    st.subheader("Sensors")
    sensor_container = st.container(border=True)
    with sensor_container:
        for description, value in Sensors_condition:
                summ_col1, summ_col2 = st.columns([3, 1])
                with summ_col1:
                            st.write(description)
                with summ_col2:
                    if value == "Online":
                            st.badge(value, color="green")
                    else:
                        st.badge(value, color="red")
        
        


recent_events = [
    ("23:15", "Light increase detected", "82 units"),
    ("22:30", "Noise peak detected", "76 units"),
    ("23:00", "Temperature increase", "+0.5 °C"),
    ("23:00", "Monitoring started", ""),
]

with st.container(border=True):

    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("Recent Events")

    with col2:
        st.caption("View all →")

    st.divider()

    for time, description, value in recent_events:

        col1, col2 = st.columns([3, 1])


        with col1:
            st.write(description)

        with col2:
            st.caption(value)

        st.divider()