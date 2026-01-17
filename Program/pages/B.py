# Mindfullness/Program/B/B.py
import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from activities import ActivitySequence

st.set_page_config(
    page_title="MindShare - Friends",
    layout="wide",
    initial_sidebar_state="collapsed"
)

sequence = ActivitySequence('B')
st.markdown(sequence.get_all_css(), unsafe_allow_html=True)
sequence.render()