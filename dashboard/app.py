import streamlit as st
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng


with st.sidebar:
    st.title("overview")



col1, col2 = st.columns(2)

with col1:
    metric_col1, metric_col2, metric_col3, metric_col4 = col1.columns(4) 
    metric_col1.metric(label="Temperature", value="70 °F", delta="1.2 °F", chart_type="bar")
    metric_col2.metric(label="Humidity", value="70 °F", delta="1.2 °F")
    metric_col3.metric(label="Light intensity", value="70 °F", delta="1.2 °F")
    metric_col4.metric(label="Noise level", value="70 °F", delta="1.2 °F")

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

col2.line_chart(df)

