import streamlit as st
import time
from streamlit_lottie import st_lottie
import json

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="MindShare - Individual",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Activity container */
    .activity-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
        transition: all 1s ease-in-out;
    }
    
    /* Breathing animation */
    @keyframes breathe-in {
        0% { transform: scale(1); opacity: 0.7; }
        100% { transform: scale(1.8); opacity: 1; }
    }
    
    @keyframes breathe-hold {
        0%, 100% { transform: scale(1.8); opacity: 1; }
    }
    
    @keyframes breathe-out {
        0% { transform: scale(1.8); opacity: 1; }
        100% { transform: scale(1); opacity: 0.7; }
    }
    
    .breathe-circle {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        box-shadow: 0 0 60px rgba(102, 126, 234, 0.6);
        margin: 3rem auto;
    }
    
    .breathe-in {
        animation: breathe-in 4s ease-in-out;
    }
    
    .breathe-hold {
        animation: breathe-hold 2s ease-in-out;
    }
    
    .breathe-out {
        animation: breathe-out 4s ease-in-out;
    }
    
    /* Close Eyes styling */
    .close-eyes-bg {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        transition: background 2s ease-in-out;
    }
    
    @keyframes eye-close {
        0% { height: 100px; border-radius: 50%; }
        100% { height: 10px; border-radius: 50%; }
    }
    
    @keyframes eye-open {
        0% { height: 10px; border-radius: 50%; }
        100% { height: 100px; border-radius: 50%; }
    }
    
    .eye-shape {
        width: 150px;
        height: 100px;
        background: white;
        border-radius: 50%;
        margin: 2rem;
        position: relative;
        box-shadow: 0 0 40px rgba(255, 255, 255, 0.3);
    }
    
    .eye-close-anim {
        animation: eye-close 3s ease-in-out forwards;
    }
    
    /* Body Attention styling */
    .body-bg {
        background: linear-gradient(135deg, #134e5e 0%, #71b280 100%);
    }
    
    @keyframes pulse-glow {
        0%, 100% { opacity: 0.5; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.1); }
    }
    
    .body-outline {
        width: 200px;
        height: 400px;
        border: 3px solid rgba(255, 255, 255, 0.8);
        border-radius: 100px 100px 80px 80px;
        margin: 2rem auto;
        position: relative;
        animation: pulse-glow 3s ease-in-out infinite;
    }
    
    @keyframes scan-body {
        0% { top: 0%; }
        100% { top: 90%; }
    }
    
    .body-scan-line {
        position: absolute;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, transparent, #fff, transparent);
        animation: scan-body 5s ease-in-out infinite;
    }
    
    /* Fade transitions */
    @keyframes fade-out-up {
        0% { opacity: 1; transform: translateY(0); }
        100% { opacity: 0; transform: translateY(-100px); }
    }
    
    @keyframes fade-in-down {
        0% { opacity: 0; transform: translateY(100px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .fade-out {
        animation: fade-out-up 1s ease-in-out forwards;
    }
    
    .fade-in {
        animation: fade-in-down 1s ease-in-out forwards;
    }
    
    /* Activity title styling */
    .activity-title {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        color: white;
        text-shadow: 0 0 30px rgba(255, 255, 255, 0.5);
        margin-bottom: 2rem;
    }
    
    .activity-instruction {
        font-size: 1.8rem;
        text-align: center;
        color: rgba(255, 255, 255, 0.9);
        margin-top: 2rem;
        font-weight: 300;
    }
    
    /* Breathing background */
    .breathe-bg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if 'current_activity' not in st.session_state:
    st.session_state.current_activity = 0
if 'activity_started' not in st.session_state:
    st.session_state.activity_started = False
if 'breath_cycle' not in st.session_state:
    st.session_state.breath_cycle = 0

# --- ACTIVITIES ---
activities = [
    {
        'name': 'Breathe',
        'bg_class': 'breathe-bg',
        'instruction': 'Follow the circle with your breath'
    },
    {
        'name': 'Close Your Eyes',
        'bg_class': 'close-eyes-bg',
        'instruction': 'Gently close your eyes and relax'
    },
    {
        'name': 'Attention to Body',
        'bg_class': 'body-bg',
        'instruction': 'Scan through your body from head to toe'
    }
]

# --- ACTIVITY RENDERER ---
def render_activity(activity_index):
    activity = activities[activity_index]
    
    # Activity intro screen
    if not st.session_state.activity_started:
        st.markdown(f"""
        <div class="activity-container {activity['bg_class']} fade-in">
            <h1 class="activity-title">{activity['name']}</h1>
            <p class="activity-instruction">{activity['instruction']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Begin", use_container_width=True, type="primary"):
                st.session_state.activity_started = True
                st.rerun()
    
    else:
        # BREATHE ACTIVITY
        if activity_index == 0:
            st.markdown(f'<div class="activity-container {activity["bg_class"]}">', unsafe_allow_html=True)
            st.markdown(f'<h1 class="activity-title">{activity["name"]}</h1>', unsafe_allow_html=True)
            
            # Breathing cycles
            breath_phases = [
                ('Breathe In', 'breathe-in', 4),
                ('Hold', 'breathe-hold', 2),
                ('Breathe Out', 'breathe-out', 4),
                ('Hold', 'breathe-hold', 2)
            ]
            
            cycle_num = st.session_state.breath_cycle % len(breath_phases)
            phase_name, phase_class, duration = breath_phases[cycle_num]
            
            st.markdown(f'<p class="activity-instruction">{phase_name}</p>', unsafe_allow_html=True)
            st.markdown(f'<div class="breathe-circle {phase_class}"></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Auto-cycle through breathing
            time.sleep(duration)
            st.session_state.breath_cycle += 1
            
            # After 3 full cycles (12 phases), move to next activity
            if st.session_state.breath_cycle >= 12:
                st.session_state.current_activity += 1
                st.session_state.activity_started = False
                st.session_state.breath_cycle = 0
            
            st.rerun()
        
        # CLOSE EYES ACTIVITY
        elif activity_index == 1:
            st.markdown(f'<div class="activity-container {activity["bg_class"]}">', unsafe_allow_html=True)
            st.markdown(f'<h1 class="activity-title">{activity["name"]}</h1>', unsafe_allow_html=True)
            
            # Two eyes closing
            st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center;">
                <div class="eye-shape eye-close-anim"></div>
                <div class="eye-shape eye-close-anim"></div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f'<p class="activity-instruction">Let your eyes gently close...</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            time.sleep(6)
            st.session_state.current_activity += 1
            st.session_state.activity_started = False
            st.rerun()
        
        # BODY ATTENTION ACTIVITY
        elif activity_index == 2:
            st.markdown(f'<div class="activity-container {activity["bg_class"]}">', unsafe_allow_html=True)
            st.markdown(f'<h1 class="activity-title">{activity["name"]}</h1>', unsafe_allow_html=True)
            
            # Body outline with scanning line
            st.markdown("""
            <div class="body-outline">
                <div class="body-scan-line"></div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f'<p class="activity-instruction">Notice the sensations in your body...</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            time.sleep(10)
            st.markdown('<div class="fade-out"><p class="activity-instruction">Session Complete</p></div>', unsafe_allow_html=True)
            time.sleep(2)
            
            # Return to home
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                if st.button("Return Home", use_container_width=True, type="primary"):
                    st.switch_page("app.py")

# --- MAIN RENDER ---
if st.session_state.current_activity < len(activities):
    render_activity(st.session_state.current_activity)
else:
    st.markdown('<div class="activity-container"><h1 class="activity-title">All Activities Complete! 🙏</h1></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Return Home", use_container_width=True, type="primary"):
            st.switch_page("app.py")