import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng
from datetime import time

st.title("Somnia dashboard")


with st.sidebar:
    st.title("overview")
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

    if st.button("📄 Page 1", use_container_width=True):
        st.switch_page("page_1.py")

    if st.button("📄 Page 2", use_container_width=True):
        st.switch_page("page_2.py")

color = st.select_slider(
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

#t = st.time_input("Set an alarm for", time(8, 45))
#st.write("Alarm is set for", t)



#different pages

#pages = {
#    "Your account": [
#        st.Page("create_account.py", title="Create your account"),
#        st.Page("manage_account.py", title="Manage your account"),
#    ],
#    "Resources": [
#        st.Page("learn.py", title="Learn about us"),
#        st.Page("trial.py", title="Try it out"),
#    ],
#}

#pg = st.navigation(pages, position="top")
#pg.run()




#charts

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "28°C", "-9°C", border=True)
b.metric("Humidity", "35%", "5%", border=True)

c.metric("Light", "200 lux", "-50 lux", border=True)
d.metric("Noise", "35 dBA", "5 dBA", border=True)


#col1, col2 = st.columns(2)

#with col1:
#    metric_col1, metric_col2, metric_col3, metric_col4 = col1.columns(4) 
#    metric_col1.metric(label="Temperature", value="70 °F", delta="1.2 °F", chart_type="bar")
#    metric_col2.metric(label="Humidity", value="70 °F", delta="1.2 °F")
#    metric_col3.metric(label="Light intensity", value="70 °F", delta="1.2 °F")
#    metric_col4.metric(label="Noise level", value="70 °F", delta="1.2 °F")

#df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["T°", "Light", "Noise"])

#col2.line_chart(df)