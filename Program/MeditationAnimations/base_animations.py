# Mindfullness/Program/MeditationAnimations/base_animations.py

def get_base_css():
    """Base CSS that all activities need"""
    return """
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
    """