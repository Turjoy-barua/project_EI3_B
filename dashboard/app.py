import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng
from datetime import time







page_element="""
<style>
.stApp {
background-image: url("https://images.pexels.com/photos/31646205/pexels-photo-31646205.png");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
"""
st.markdown(page_element, unsafe_allow_html=True)

st.set_page_config( # --> configuring the page
    page_title="weatherlive",
    page_icon="🌦️",
    layout="wide",
)



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




changes = list(rng(4).standard_normal(20))
data = [sum(changes[:i]) for i in range(20)]
delta = round(data[-1], 2)

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", 10, delta, chart_data=data, chart_type="line", border=True)
b.metric("Humidity", "35%", "5%", chart_data=data, chart_type="line", border=True)

c.metric("Light", "200 lux", "-50 lux", chart_data=data, chart_type="line", border=True)
d.metric("Noise", "35 dBA", "5 dBA", chart_data=data, chart_type="line", border=True)

col1, col2= st.columns([3,1], border=True)

with col1:
    st.header("Graph")
    df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
    st.line_chart(df)

with col2:
    st.header("Tonight's summary",)

    summary_col1, summary_col2 = col2.columns(2)
    summary_col1.divider()
    summary_col2.divider()
    summary_col1.text("Monitoring duration", text_alignment='left')
    summary_col2.markdown("**8H**",text_alignment="right")
    summary_col1.divider()
    summary_col2.divider()
    summary_col1.text("Average temperature", text_alignment='left')
    summary_col2.subheader("25",text_alignment="right")
    summary_col1.divider()
    summary_col2.divider()
    summary_col1.text("Average sound intensity", text_alignment='left')
    summary_col2.subheader("19 units",text_alignment="right")
    summary_col1.divider()
    summary_col2.divider()
    summary_col1.text("Average humidity", text_alignment='left')
    summary_col2.subheader("20%",text_alignment="right")
    summary_col1.divider()
    summary_col2.divider()


events = [
    ("23:15", "Light increase detected", "82 units", "🟡"),
    ("22:30", "Noise peak detected", "76 units", "🟣"),
    ("23:00", "Temperature increase", "+0.5 °C", "🔵"),
    ("23:00", "Monitoring started", "", "🟢"),
]

with st.container(border=True):

    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("Recent Events")

    with col2:
        st.caption("View all →")

    st.divider()

    for time, description, value, icon in events:

        col1, col2, col3 = st.columns([1, 3, 1])

        with col1:
            st.write(f"{icon} {time}", )

        with col2:
            st.write(description)

        with col3:
            st.caption(value)

        st.divider()