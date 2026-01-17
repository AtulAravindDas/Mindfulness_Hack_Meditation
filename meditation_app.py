import streamlit as st
import time
import os

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="MindShare",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. INITIALIZE SESSION STATE ---
if 'selection' not in st.session_state:
    st.session_state.selection = "Home"
if 'current_activity' not in st.session_state:
    st.session_state.current_activity = 0
if 'activity_started' not in st.session_state:
    st.session_state.activity_started = False
if 'breath_cycle' not in st.session_state:
    st.session_state.breath_cycle = 0

# --- 3. CUSTOM CSS (Activities + Layout) ---
st.markdown("""
<style>
    /* Activity container */
    .activity-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 70vh;
        border-radius: 20px;
        padding: 20px;
    }
    
    .breathe-circle {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        box-shadow: 0 0 60px rgba(102, 126, 234, 0.6);
        margin: 2rem auto;
    }

    /* Animations from your snippet */
    @keyframes breathe-in { 0% { transform: scale(1); opacity: 0.7; } 100% { transform: scale(1.6); opacity: 1; } }
    @keyframes breathe-out { 0% { transform: scale(1.6); opacity: 1; } 100% { transform: scale(1); opacity: 0.7; } }
    .breathe-in { animation: breathe-in 4s ease-in-out; }
    .breathe-out { animation: breathe-out 4s ease-in-out; }
    
    .activity-title { font-size: 2.5rem; color: white; text-align: center; }
    .activity-instruction { font-size: 1.5rem; color: white; text-align: center; }
    .breathe-bg { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .close-eyes-bg { background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); }
    .body-bg { background: linear-gradient(135deg, #134e5e 0%, #71b280 100%); }
    
    /* Custom button styling for larger buttons */
    .stButton > button {
        height: 150px;
        font-size: 1.5rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("MindShare")
    if st.button("Reset to Home"):
        st.session_state.selection = "Home"
        st.rerun()

# --- 5. MAIN NAVIGATION LOGIC ---

# CASE A: THE INDIVIDUAL ACTIVITY PAGE
if st.session_state.selection == "Individual":
    activities = [
        {'name': 'Breathe', 'bg_class': 'breathe-bg', 'instruction': 'Follow the circle'},
        {'name': 'Close Your Eyes', 'bg_class': 'close-eyes-bg', 'instruction': 'Relax...'},
        {'name': 'Attention to Body', 'bg_class': 'body-bg', 'instruction': 'Scan your body'}
    ]
    
    current_idx = st.session_state.current_activity
    
    if current_idx < len(activities):
        act = activities[current_idx]
        
        # UI for Activity
        st.markdown(f'<div class="activity-container {act["bg_class"]}">', unsafe_allow_html=True)
        st.markdown(f'<h1 class="activity-title">{act["name"]}</h1>', unsafe_allow_html=True)
        
        if not st.session_state.activity_started:
            st.markdown(f'<p class="activity-instruction">{act["instruction"]}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            if st.button("Begin Session", width="stretch"):
                st.session_state.activity_started = True
                st.rerun()
        else:
            # Simple breathing logic as example
            st.markdown('<div class="breathe-circle breathe-in"></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            time.sleep(4)
            st.session_state.current_activity += 1
            st.rerun()
    else:
        st.success("Session Complete!")
        if st.button("Return Home", width="stretch"):
            st.session_state.selection = "Home"
            st.session_state.current_activity = 0
            st.session_state.activity_started = False
            st.rerun()

# CASE B: THE HOME PAGE (Logo + 2x2 Grid)
else:
    # Logo
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        if os.path.exists("MindShare_Logo.png"):
            st.image("MindShare_Logo.png", use_container_width=True)
        else:
            st.title("MindShare")

    st.markdown("---")

    # 2x2 Grid
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        if st.button("Individual", width="stretch", key="btn_individual"):
            st.session_state.selection = "Individual"
            st.rerun()
    with r1c2:
        st.button("Group", width="stretch", key="btn_group")
        
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        st.button("Progress", width="stretch", key="btn_progress")
    with r2c2:
        st.button("Settings", width="stretch", key="btn_settings")