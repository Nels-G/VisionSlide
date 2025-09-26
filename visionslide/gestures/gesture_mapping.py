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
        try:
            current_time = time.time()
            
            # Ignorer les gestes non reconnus
            if gesture_name in ["unknown", "no_hand", "pointing", "error"]:
                return None
            
            # Check cooldown period
            if current_time - self.last_action_time < self.gesture_cooldown:
                return None
            
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
        
        except Exception as e:
            self.logger.error(f"Error in gesture mapping: {e}")
            return None