"""
Gesture to action mapping.
"""
import time
from visionslide.config import *
from visionslide.utils.logger import setup_logger

class GestureMapper:
    """Maps detected gestures to actions."""
    
    def __init__(self):
        self.logger = setup_logger('GestureMapper')
        self.current_gesture = None
        self.gesture_start_time = 0
        self.last_action_time = 0
        self.gesture_hold_duration = GESTURE_HOLD_DURATION
        self.gesture_cooldown = GESTURE_COOLDOWN
        
        self.gesture_actions = {
            "point_right": "next_slide",
            "point_left": "previous_slide", 
            "open_hand": "exit"
        }
    
    def update_gesture(self, gesture_name, hand_landmarks, gesture_detector):
        """
        Update current gesture and check if action should be triggered.
        """
        current_time = time.time()
        
        # Check cooldown
        if current_time - self.last_action_time < self.gesture_cooldown:
            return None
        
        # Determine direction for pointing gesture
        if gesture_name == "pointing" and hand_landmarks:
            hand_pos = gesture_detector.get_hand_position(hand_landmarks)
            if hand_pos == "left":
                gesture_name = "point_left"
            elif hand_pos == "right":
                gesture_name = "point_right"
            else:
                return None  # Ignorer si main au centre
        
        # New gesture detected
        if gesture_name != self.current_gesture:
            self.current_gesture = gesture_name
            self.gesture_start_time = current_time
            return None
        
        # Same gesture held for required duration
        if (current_time - self.gesture_start_time >= self.gesture_hold_duration and
            gesture_name in self.gesture_actions):
            
            action = self.gesture_actions[gesture_name]
            self.last_action_time = current_time
            self.logger.info(f"Gesture '{gesture_name}' triggered action: {action}")
            return action
        
        return None