"""
Configuration settings for VisionSlide application.
"""

# Gesture Recognition Settings
GESTURE_CONFIDENCE_THRESHOLD = 0.7
GESTURE_HOLD_DURATION = 1.5
GESTURE_COOLDOWN = 0.8

# Camera Configuration
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FPS_TARGET = 30

# Performance Tuning
MODEL_COMPLEXITY = 1
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.5

# Application Settings
DEBUG_MODE = True
SHOW_FPS = True