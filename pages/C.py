# pages/C.py
import streamlit as st
import sys
import os

# Add parent directory to path so we can import activities
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from activities import ActivitySequence

st.set_page_config(
    page_title="MindShare - Classroom",
    layout="wide",
    initial_sidebar_state="collapsed"
)

sequence = ActivitySequence('C')
st.markdown(sequence.get_all_css(), unsafe_allow_html=True)
sequence.render()