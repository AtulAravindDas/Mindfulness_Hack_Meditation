# pages/B.py
import streamlit as st
from activities import ActivitySequence

st.set_page_config(
    page_title="MindShare - Friends",
    layout="wide",
    initial_sidebar_state="collapsed"
)

sequence = ActivitySequence('B')
st.markdown(sequence.get_all_css(), unsafe_allow_html=True)
sequence.render()