# Mindfullness/Program/C/C.py
import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from activities import ActivitySequence

st.set_page_config(
    page_title="MindShare - Classroom",
    layout="wide",
    initial_sidebar_state="collapsed"
)

sequence = ActivitySequence('C')
st.markdown(sequence.get_all_css(), unsafe_allow_html=True)
sequence.render()