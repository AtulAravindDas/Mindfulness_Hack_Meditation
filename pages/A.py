# pages/A.py
import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from activities import ActivitySequence

st.set_page_config(
    page_title="MindShare - Individual",
    layout="wide",
    initial_sidebar_state="collapsed"
)

sequence = ActivitySequence('A')
st.markdown(sequence.get_all_css(), unsafe_allow_html=True)
sequence.render()