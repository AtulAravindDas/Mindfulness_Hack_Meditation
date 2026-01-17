import streamlit as st
import time
import os
from activities import ActivitySequence

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

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("MindShare")
    if st.button("Reset to Home"):
        st.session_state.selection = "Home"
        st.session_state.current_activity = 0
        st.session_state.activity_started = False
        st.session_state.breath_cycle = 0
        st.rerun()

# --- 4. MAIN NAVIGATION LOGIC ---

# CASE: ACTIVITY SEQUENCE PAGES (A, B, C, D)
if st.session_state.selection in ["A", "B", "C", "D"]:
    # Create activity sequence for the selected program
    sequence = ActivitySequence(st.session_state.selection)
    
    # Inject CSS
    st.markdown(sequence.get_all_css(), unsafe_allow_html=True)
    
    # Render the sequence
    sequence.render()

# CASE: SIMPLE INDIVIDUAL ACTIVITY PAGE (Original)
elif st.session_state.selection == "Individual":
    # --- CUSTOM CSS FOR SIMPLE ACTIVITIES ---
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

        /* Animations */
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
            if st.button("Begin Session", width="stretch", key="begin_simple"):
                st.session_state.activity_started = True
                st.rerun()
        else:
            # Simple breathing logic as example
            st.markdown('<div class="breathe-circle breathe-in"></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            time.sleep(4)
            st.session_state.current_activity += 1
            st.session_state.activity_started = False
            st.rerun()
    else:
        st.success("Session Complete!")
        if st.button("Return Home", width="stretch", key="return_simple"):
            st.session_state.selection = "Home"
            st.session_state.current_activity = 0
            st.session_state.activity_started = False
            st.rerun()

# CASE: THE HOME PAGE (Logo + 2x2 Grid)
else:
    # --- CUSTOM CSS FOR HOME PAGE ---
    st.markdown("""
    <style>
        /* Custom button styling for larger buttons */
        .stButton > button {
            height: 150px;
            font-size: 1.5rem;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Logo
    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        if os.path.exists("MindShare_Logo.png"):
            st.image("MindShare_Logo.png", width="stretch")
        else:
            st.title("🧠 MindShare")

    st.markdown("---")

    # 2x2 Grid with Program Selection
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        if st.button("👤 Individual (A)", width="stretch", key="btn_a", type="primary"):
            st.session_state.selection = "A"
            st.session_state.current_activity = 0
            st.session_state.activity_started = False
            st.rerun()
    with r1c2:
        if st.button("👥 Group (B)", width="stretch", key="btn_b", type="primary"):
            st.session_state.selection = "B"
            st.session_state.current_activity = 0
            st.session_state.activity_started = False
            st.rerun()
        
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        if st.button("🎓 Classroom (C)", width="stretch", key="btn_c", type="primary"):
            st.session_state.selection = "C"
            st.session_state.current_activity = 0
            st.session_state.activity_started = False
            st.rerun()
    with r2c2:
        if st.button("⚽ Team (D)", width="stretch", key="btn_d", type="primary"):
            st.session_state.selection = "D"
            st.session_state.current_activity = 0
            st.session_state.activity_started = False
            st.rerun()
    
    # Welcome message
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h2>Welcome to MindShare</h2>
        <p style="font-size: 1.2rem; color: #666;">
            Select a mindfulness program above to begin your journey
        </p>
    </div>
    """, unsafe_allow_html=True)