# Mindfullness/Program/MeditationAnimations/body_attention.py

BODY_ATTENTION_ANIMATIONS = {
    'scanning_light': {
        'bg_class': 'body-bg',
        'css': """
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
        """,
        'html': """
        <div class="body-outline">
            <div class="body-scan-line"></div>
        </div>
        """
    },
    
    'chakra_points': {
        'bg_class': 'body-bg-chakra',
        'css': """
        .body-bg-chakra {
            background: linear-gradient(135deg, #2c3e50 0%, #4ca1af 100%);
        }
        
        @keyframes chakra-glow {
            0%, 100% { opacity: 0.3; transform: scale(0.8); }
            50% { opacity: 1; transform: scale(1.2); }
        }
        
        .body-outline {
            width: 200px;
            height: 400px;
            border: 2px solid rgba(255, 255, 255, 0.5);
            border-radius: 100px 100px 80px 80px;
            margin: 2rem auto;
            position: relative;
        }
        
        .chakra {
            position: absolute;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            left: 50%;
            transform: translateX(-50%);
        }
        
        .chakra:nth-child(1) { top: 10%; background: #9b59b6; animation: chakra-glow 2s ease-in-out 0s infinite; }
        .chakra:nth-child(2) { top: 25%; background: #3498db; animation: chakra-glow 2s ease-in-out 0.3s infinite; }
        .chakra:nth-child(3) { top: 40%; background: #1abc9c; animation: chakra-glow 2s ease-in-out 0.6s infinite; }
        .chakra:nth-child(4) { top: 55%; background: #f1c40f; animation: chakra-glow 2s ease-in-out 0.9s infinite; }
        .chakra:nth-child(5) { top: 70%; background: #e67e22; animation: chakra-glow 2s ease-in-out 1.2s infinite; }
        .chakra:nth-child(6) { top: 85%; background: #e74c3c; animation: chakra-glow 2s ease-in-out 1.5s infinite; }
        """,
        'html': """
        <div class="body-outline">
            <div class="chakra"></div>
            <div class="chakra"></div>
            <div class="chakra"></div>
            <div class="chakra"></div>
            <div class="chakra"></div>
            <div class="chakra"></div>
        </div>
        """
    },
    
    'wave_ripple': {
        'bg_class': 'body-bg-wave',
        'css': """
        .body-bg-wave {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        @keyframes ripple-wave {
            0% { transform: scale(0.5) translateY(0); opacity: 0; }
            50% { opacity: 1; }
            100% { transform: scale(2) translateY(400px); opacity: 0; }
        }
        
        .body-outline {
            width: 200px;
            height: 400px;
            border: 2px solid rgba(255, 255, 255, 0.6);
            border-radius: 100px 100px 80px 80px;
            margin: 2rem auto;
            position: relative;
            overflow: hidden;
        }
        
        .ripple {
            position: absolute;
            width: 100%;
            height: 50px;
            border: 2px solid rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            top: 0;
            left: 0;
        }
        
        .ripple:nth-child(1) { animation: ripple-wave 6s ease-in-out 0s infinite; }
        .ripple:nth-child(2) { animation: ripple-wave 6s ease-in-out 2s infinite; }
        .ripple:nth-child(3) { animation: ripple-wave 6s ease-in-out 4s infinite; }
        """,
        'html': """
        <div class="body-outline">
            <div class="ripple"></div>
            <div class="ripple"></div>
            <div class="ripple"></div>
        </div>
        """
    }
}