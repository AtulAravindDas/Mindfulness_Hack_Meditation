import streamlit as st
import time
import os
from MeditationAnimations import get_base_css, get_program_animations

# ============================================================================
# ACTIVITY CLASSES (Integrated directly)
# ============================================================================

class MindfulnessActivity:
    """Base class for all mindfulness activities"""
    
    def __init__(self, name, instruction, duration, animation_config):
        self.name = name
        self.instruction = instruction
        self.bg_class = animation_config['bg_class']
        self.duration = duration
        self.animation_config = animation_config
    
    def render_intro(self):
        """Render the intro screen for the activity"""
        st.markdown(f"""
        <div class="activity-container {self.bg_class} fade-in">
            <h1 class="activity-title">{self.name}</h1>
            <p class="activity-instruction">{self.instruction}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Begin", width="stretch", type="primary", key=f"begin_{self.name}"):
                return True
        return False
    
    def get_css(self):
        """Get CSS from animation config"""
        return self.animation_config['css']
    
    def get_html(self, *args):
        """Get HTML from animation config"""
        html_generator = self.animation_config['html']
        if callable(html_generator):
            return html_generator(*args)
        return html_generator
    
    def render_activity(self):
        """Override in subclasses"""
        raise NotImplementedError


class BreatheActivity(MindfulnessActivity):
    
    def __init__(self, animation_config):
        super().__init__(
            name="Breathe",
            instruction="Follow the animation with your breath",
            duration=40,
            animation_config=animation_config
        )
        self.breath_phases = [
            ('Breathe In', 'breathe-in', 4),
            ('Hold', 'breathe-hold', 2),
            ('Breathe Out', 'breathe-out', 4),
            ('Hold', 'breathe-hold', 2)
        ]
    
    def render_activity(self):
        if 'breath_cycle' not in st.session_state:
            st.session_state.breath_cycle = 0
        
        cycle_num = st.session_state.breath_cycle % len(self.breath_phases)
        phase_name, phase_class, duration = self.breath_phases[cycle_num]
        
        st.markdown(f'<div class="activity-container {self.bg_class}">', unsafe_allow_html=True)
        st.markdown(f'<h1 class="activity-title">{self.name}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p class="activity-instruction">{phase_name}</p>', unsafe_allow_html=True)
        st.markdown(self.get_html(phase_class), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        time.sleep(duration)
        st.session_state.breath_cycle += 1
        
        if st.session_state.breath_cycle >= 12:
            st.session_state.breath_cycle = 0
            return True
        
        st.rerun()


class CloseEyesActivity(MindfulnessActivity):
    
    def __init__(self, animation_config):
        super().__init__(
            name="Close Your Eyes",
            instruction="Gently close your eyes and relax",
            duration=6,
            animation_config=animation_config
        )
    
    def render_activity(self):
        st.markdown(f'<div class="activity-container {self.bg_class}">', unsafe_allow_html=True)
        st.markdown(f'<h1 class="activity-title">{self.name}</h1>', unsafe_allow_html=True)
        st.markdown(self.get_html(), unsafe_allow_html=True)
        st.markdown(f'<p class="activity-instruction">Let your eyes gently close...</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        time.sleep(self.duration)
        return True


class BodyAttentionActivity(MindfulnessActivity):
    
    def __init__(self, animation_config):
        super().__init__(
            name="Attention to Body",
            instruction="Scan through your body from head to toe",
            duration=10,
            animation_config=animation_config
        )
    
    def render_activity(self):
        st.markdown(f'<div class="activity-container {self.bg_class}">', unsafe_allow_html=True)
        st.markdown(f'<h1 class="activity-title">{self.name}</h1>', unsafe_allow_html=True)
        st.markdown(self.get_html(), unsafe_allow_html=True)
        st.markdown(f'<p class="activity-instruction">Notice the sensations in your body...</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        time.sleep(self.duration)
        return True


class DanceActivity(MindfulnessActivity):
    
    def __init__(self, animation_config):
        super().__init__(
            name="Dance",
            instruction="Move your body freely to the rhythm",
            duration=15,
            animation_config=animation_config
        )
    
    def render_activity(self):
        st.markdown(f'<div class="activity-container {self.bg_class}">', unsafe_allow_html=True)
        st.markdown(f'<h1 class="activity-title">{self.name}</h1>', unsafe_allow_html=True)
        st.markdown(self.get_html(), unsafe_allow_html=True)
        st.markdown(f'<p class="activity-instruction">Let your body move naturally...</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        time.sleep(self.duration)
        return True


# Activity class mapping
ACTIVITY_CLASSES = {
    'breathe': BreatheActivity,
    'close_eyes': CloseEyesActivity,
    'body_attention': BodyAttentionActivity,
    'dance': DanceActivity
}


class ActivitySequence:
    """Manages a sequence of activities"""
    
    def __init__(self, program_letter):
        self.program_letter = program_letter
        self.animations = get_program_animations(program_letter)
        
        # Create activities dynamically based on config
        self.activities = []
        for activity_key, animation_config in self.animations.items():
            activity_class = ACTIVITY_CLASSES[activity_key]
            self.activities.append(activity_class(animation_config))
        
    def get_all_css(self):
        """Combine base CSS with all activity-specific CSS"""
        css = f"<style>{get_base_css()}"
        for activity in self.activities:
            css += activity.get_css()
        css += "</style>"
        return css
    
    def render(self):
        """Render the current activity in the sequence"""
        if 'activity_started' not in st.session_state:
            st.session_state.activity_started = False
        if 'current_activity' not in st.session_state:
            st.session_state.current_activity = 0
        
        current_index = st.session_state.current_activity
        
        if current_index >= len(self.activities):
            return self._render_completion()
        
        activity = self.activities[current_index]
        
        if not st.session_state.activity_started:
            if activity.render_intro():
                st.session_state.activity_started = True
                st.rerun()
        else:
            if activity.render_activity():
                st.session_state.current_activity += 1
                st.session_state.activity_started = False
                st.rerun()
    
    def _render_completion(self):
        """Show completion screen"""
        st.markdown('<div class="activity-container"><h1 class="activity-title">All Activities Complete! 🙏</h1></div>', 
                   unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Return Home", width="stretch", type="primary"):
                st.session_state.selection = "Home"
                st.session_state.current_activity = 0
                st.session_state.activity_started = False
                st.rerun()


# ============================================================================
# MAIN APP
# ============================================================================

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