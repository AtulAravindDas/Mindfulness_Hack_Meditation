# app.py
import streamlit as st
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MindShare",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- 2. INITIALIZE SESSION STATE ---
if 'selection' not in st.session_state:
    st.session_state.selection = None

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("MindShare Menu")
    st.write("Navigation & Settings")
    
    # Show current selection if exists
    if st.session_state.selection:
        st.info(f"Current: **{st.session_state.selection}**")
    
    # Reset button
    if st.button("🏠 Return Home"):
        st.session_state.selection = None
        # Clear activity states
        for key in ['current_activity', 'activity_started', 'breath_cycle']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# --- 4. PROGRAM MAPPING ---
PROGRAM_MAPPING = {
    'A': 'pages/A.py',
    'B': 'pages/B.py',
    'C': 'pages/C.py',
    'D': 'pages/D.py'
}

# --- 5. NAVIGATION LOGIC ---
# If a program is selected, switch to it
if st.session_state.selection in PROGRAM_MAPPING:
    st.switch_page(PROGRAM_MAPPING[st.session_state.selection])

# --- 6. HOME PAGE ---
# Logo (Top Center)
col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    if os.path.exists("MindShare_Logo.png"):
        st.image("MindShare_Logo.png", use_container_width=True)
    else:
        st.title("🧠 MindShare")
        st.caption("💡 Add 'MindShare_Logo.png' to display your logo")

st.markdown("---")

# --- 7. THE 2x2 BUTTON GRID ---
with st.container():
    # Top Row: Buttons A and B
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        if st.button("👤 Individual (A)", use_container_width=True, key="btn_a", type="primary"):
            st.session_state.selection = "A"
            st.rerun()
    with row1_col2:
        if st.button("👥 Group (B)", use_container_width=True, key="btn_b", type="primary"):
            st.session_state.selection = "B"
            st.rerun()
    
    # Bottom Row: Buttons C and D
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        if st.button("🎓 Classroom (C)", use_container_width=True, key="btn_c", type="primary"):
            st.session_state.selection = "C"
            st.rerun()
    with row2_col2:
        if st.button("⚽ Team (D)", use_container_width=True, key="btn_d", type="primary"):
            st.session_state.selection = "D"
            st.rerun()

# --- 8. WELCOME MESSAGE ---
if not st.session_state.selection:
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h2>Welcome to MindShare</h2>
        <p style="font-size: 1.2rem; color: #666;">
            Select an experience above to begin your mindfulness journey
        </p>
    </div>
    """, unsafe_allow_html=True)