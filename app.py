import streamlit as st
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MindShare",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- 2. SIDEBAR ---
with st.sidebar:
    st.title("MindShare Menu")
    st.write("Navigation & Settings")

# --- 3. LOGO (Top Center) ---
col_l, col_m, col_r = st.columns([1, 2, 1])

with col_m:
    # Check if file exists to prevent the 'empty screen' error
    if os.path.exists("MindShare_Logo.png"):
        st.image("MindShare_Logo.png", use_container_width=True)
    else:
        # Placeholder if image is missing so the app still runs
        st.title("🧠 MindShare")
        st.warning("Logo file 'MindShare_Logo.png' not found in directory.")

st.markdown("---")

# --- 4. THE 2x2 BUTTON GRID ---
# Using a container to keep the grid tight
with st.container():
    # Top Row: Buttons A and B
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        if st.button("A", use_container_width=True):
            st.session_state.selection = "A"
            
    with row1_col2:
        if st.button("B", use_container_width=True):
            st.session_state.selection = "B"

    # Bottom Row: Buttons C and D
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        if st.button("C", use_container_width=True):
            st.session_state.selection = "C"
            
    with row2_col2:
        if st.button("D", use_container_width=True):
            st.session_state.selection = "D"

# --- 5. CONTENT AREA ---
if 'selection' in st.session_state:
    st.write(f"### You selected Section {st.session_state.selection}")