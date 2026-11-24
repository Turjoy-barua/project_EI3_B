import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

# st.title("Account")


with st.sidebar:
    st.title("Overview")

    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

    if st.button("📄 Page 1", use_container_width=True):
        st.switch_page("page_1.py")

    if st.button("📄 Page 2", use_container_width=True):
        st.switch_page("page_2.py")

st.title("Account")
st.write("Bienvenue sur la première page de Somnia !")