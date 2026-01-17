# Mindfullness/Program/MeditationAnimations/dance.py

DANCE_ANIMATIONS = {
    'flowing_silhouette': {
        'bg_class': 'dance-bg',
        'css': """
        .dance-bg {
            background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
        }
        
        @keyframes dance-sway {
            0%, 100% { transform: rotate(-5deg) translateX(-10px); }
            50% { transform: rotate(5deg) translateX(10px); }
        }
        
        @keyframes arm-wave {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(-30deg); }
            75% { transform: rotate(30deg); }
        }
        
        .dancer {
            width: 150px;
            height: 350px;
            margin: 3rem auto;
            position: relative;
            animation: dance-sway 2s ease-in-out infinite;
        }
        
        .dancer-body {
            width: 80px;
            height: 150px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 40px;
            margin: 0 auto;
        }
        
        .dancer-head {
            width: 60px;
            height: 60px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 50%;
            margin: 0 auto 10px;
        }
        
        .dancer-arm {
            width: 60px;
            height: 15px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            position: absolute;
            top: 80px;
        }
        
        .dancer-arm-left {
            left: -20px;
            transform-origin: right center;
            animation: arm-wave 1.5s ease-in-out infinite;
        }
        
        .dancer-arm-right {
            right: -20px;
            transform-origin: left center;
            animation: arm-wave 1.5s ease-in-out 0.75s infinite;
        }
        """,
        'html': """
        <div class="dancer">
            <div class="dancer-head"></div>
            <div class="dancer-body"></div>
            <div class="dancer-arm dancer-arm-left"></div>
            <div class="dancer-arm dancer-arm-right"></div>
        </div>
        """
    }
}


