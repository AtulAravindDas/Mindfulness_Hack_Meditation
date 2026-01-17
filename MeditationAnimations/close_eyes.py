# Mindfullness/Program/MeditationAnimations/close_eyes.py

CLOSE_EYES_ANIMATIONS = {
    'dual_eyes': {
        'bg_class': 'close-eyes-bg',
        'css': """
        .close-eyes-bg {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            transition: background 2s ease-in-out;
        }
        
        @keyframes eye-close {
            0% { height: 100px; border-radius: 50%; }
            100% { height: 10px; border-radius: 50%; }
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
        """,
        'html': """
        <div style="display: flex; justify-content: center; align-items: center;">
            <div class="eye-shape eye-close-anim"></div>
            <div class="eye-shape eye-close-anim"></div>
        </div>
        """
    },
    
    'moon_fade': {
        'bg_class': 'close-eyes-bg-moon',
        'css': """
        .close-eyes-bg-moon {
            background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        }
        
        @keyframes moon-dim {
            0% { opacity: 1; box-shadow: 0 0 80px rgba(255, 255, 255, 0.8); }
            100% { opacity: 0.2; box-shadow: 0 0 20px rgba(255, 255, 255, 0.2); }
        }
        
        .moon {
            width: 200px;
            height: 200px;
            background: white;
            border-radius: 50%;
            margin: 3rem auto;
            animation: moon-dim 4s ease-in-out forwards;
        }
        """,
        'html': '<div class="moon"></div>'
    },
    
    'curtain_close': {
        'bg_class': 'close-eyes-bg-curtain',
        'css': """
        .close-eyes-bg-curtain {
            background: linear-gradient(135deg, #232526 0%, #414345 100%);
        }
        
        @keyframes curtain-left {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(0); }
        }
        
        @keyframes curtain-right {
            0% { transform: translateX(100%); }
            100% { transform: translateX(0); }
        }
        
        .curtain-container {
            position: relative;
            width: 400px;
            height: 300px;
            margin: 3rem auto;
            overflow: hidden;
            border-radius: 20px;
        }
        
        .curtain {
            position: absolute;
            width: 50%;
            height: 100%;
            background: linear-gradient(90deg, #7f00ff, #e100ff);
            top: 0;
        }
        
        .curtain-left {
            left: 0;
            animation: curtain-left 3s ease-in-out forwards;
        }
        
        .curtain-right {
            right: 0;
            animation: curtain-right 3s ease-in-out forwards;
        }
        """,
        'html': """
        <div class="curtain-container">
            <div class="curtain curtain-left"></div>
            <div class="curtain curtain-right"></div>
        </div>
        """
    }
}