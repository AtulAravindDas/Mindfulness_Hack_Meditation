# Mindfullness/Program/MeditationAnimations/__init__.py

from .breathe import BREATHE_ANIMATIONS
from .close_eyes import CLOSE_EYES_ANIMATIONS
from .body_attention import BODY_ATTENTION_ANIMATIONS
from .dance import DANCE_ANIMATIONS
from .base_animations import get_base_css

# Animation configurations for each program
ANIMATION_CONFIGS = {
    'A': {
        'breathe': ('breathe', 'circle_pulse'),
        'close_eyes': ('close_eyes', 'dual_eyes'),
        'body_attention': ('body_attention', 'scanning_light')
    },
    'B': {
        'breathe': ('breathe', 'expanding_rings'),
        'close_eyes': ('close_eyes', 'moon_fade'),
        'body_attention': ('body_attention', 'chakra_points'),
        'dance': ('dance', 'flowing_silhouette')
    },
    'C': {
        'breathe': ('breathe', 'lotus_bloom'),
        'close_eyes': ('close_eyes', 'curtain_close'),
        'body_attention': ('body_attention', 'wave_ripple')
    },
    'D': {
        'breathe': ('breathe', 'circle_pulse'),
        'close_eyes': ('close_eyes', 'curtain_close'),
        'body_attention': ('body_attention', 'chakra_points'),
        'dance': ('dance', 'flowing_silhouette')
    }
}

# Animation library
ANIMATION_LIBRARY = {
    'breathe': BREATHE_ANIMATIONS,
    'close_eyes': CLOSE_EYES_ANIMATIONS,
    'body_attention': BODY_ATTENTION_ANIMATIONS,
    'dance': DANCE_ANIMATIONS
}

def get_animation(activity_type, animation_name):
    """Get a specific animation configuration"""
    return ANIMATION_LIBRARY[activity_type][animation_name]

def get_program_animations(program_letter):
    """Get all animations for a specific program"""
    config = ANIMATION_CONFIGS[program_letter]
    animations = {}
    for activity_key, (activity_type, animation_name) in config.items():
        animations[activity_key] = get_animation(activity_type, animation_name)
    return animations