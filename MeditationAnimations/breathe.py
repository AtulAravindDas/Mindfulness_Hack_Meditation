# Mindfullness/Program/MeditationAnimations/breathe.py

BREATHE_ANIMATIONS = {
    'circle_pulse': {
        'bg_class': 'breathe-bg',
        'css': """
        /* Breathing background */
        .breathe-bg {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
        """,
        'html': lambda phase_class: f'<div class="breathe-circle {phase_class}"></div>'
    },
    
    'expanding_rings': {
        'bg_class': 'breathe-bg-rings',
        'css': """
        .breathe-bg-rings {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        @keyframes ring-expand {
            0% { transform: scale(0.5); opacity: 1; }
            100% { transform: scale(2.5); opacity: 0; }
        }
        
        .breathe-rings {
            position: relative;
            width: 200px;
            height: 200px;
            margin: 3rem auto;
        }
        
        .breathe-ring {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            border: 3px solid rgba(255, 255, 255, 0.6);
            top: 0;
            left: 0;
        }
        
        .breathe-in .breathe-ring:nth-child(1) {
            animation: ring-expand 4s ease-out infinite;
        }
        
        .breathe-in .breathe-ring:nth-child(2) {
            animation: ring-expand 4s ease-out 1s infinite;
        }
        
        .breathe-in .breathe-ring:nth-child(3) {
            animation: ring-expand 4s ease-out 2s infinite;
        }
        """,
        'html': lambda phase_class: f"""
        <div class="breathe-rings {phase_class}">
            <div class="breathe-ring"></div>
            <div class="breathe-ring"></div>
            <div class="breathe-ring"></div>
        </div>
        """
    },
    
    'lotus_bloom': {
        'bg_class': 'breathe-bg-lotus',
        'css': """
        .breathe-bg-lotus {
            background: linear-gradient(135deg, #fc466b 0%, #3f5efb 100%);
        }
        
        @keyframes petal-open {
            0% { transform: scale(0.3) rotate(0deg); opacity: 0.5; }
            100% { transform: scale(1) rotate(45deg); opacity: 1; }
        }
        
        @keyframes petal-close {
            0% { transform: scale(1) rotate(45deg); opacity: 1; }
            100% { transform: scale(0.3) rotate(0deg); opacity: 0.5; }
        }
        
        .lotus-container {
            position: relative;
            width: 250px;
            height: 250px;
            margin: 3rem auto;
        }
        
        .petal {
            position: absolute;
            width: 100px;
            height: 100px;
            background: linear-gradient(135deg, rgba(255,255,255,0.8), rgba(255,255,255,0.4));
            border-radius: 50% 0 50% 0;
            top: 50%;
            left: 50%;
            transform-origin: 0 0;
        }
        
        .breathe-in .petal { animation: petal-open 4s ease-in-out forwards; }
        .breathe-out .petal { animation: petal-close 4s ease-in-out forwards; }
        
        .petal:nth-child(1) { transform: rotate(0deg); }
        .petal:nth-child(2) { transform: rotate(45deg); }
        .petal:nth-child(3) { transform: rotate(90deg); }
        .petal:nth-child(4) { transform: rotate(135deg); }
        .petal:nth-child(5) { transform: rotate(180deg); }
        .petal:nth-child(6) { transform: rotate(225deg); }
        .petal:nth-child(7) { transform: rotate(270deg); }
        .petal:nth-child(8) { transform: rotate(315deg); }
        """,
        'html': lambda phase_class: f"""
        <div class="lotus-container {phase_class}">
            <div class="petal"></div>
            <div class="petal"></div>
            <div class="petal"></div>
            <div class="petal"></div>
            <div class="petal"></div>
            <div class="petal"></div>
            <div class="petal"></div>
            <div class="petal"></div>
        </div>
        """
    }
}