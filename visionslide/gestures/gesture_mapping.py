"""
Gesture to action mapping and gesture state management.
"""
import time
from visionslide.config import *
from visionslide.utils.logger import setup_logger

class GestureMapper:
    """Maps detected gestures to actions with state management."""
    
    def __init__(self):
        self.logger = setup_logger('GestureMapper')
        self.current_gesture = None
        self.gesture_start_time = 0
        self.last_action_time = 0
        self.gesture_hold_duration = GESTURE_HOLD_DURATION
        self.gesture_cooldown = GESTURE_COOLDOWN
        
        # Gesture to action mapping
        self.gesture_actions = {
            "point_right": "next_slide",
            "point_left": "previous_slide",
            "fist": "exit",
            "open_hand": "none"  # No action, can be used for calibration
        }
    
    def update_gesture(self, gesture_name, hand_landmarks):
        """
        Update current gesture and check if action should be triggered.
        Returns action name if triggered, None otherwise.
        """
        current_time = time.time()
        
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
    
    def determine_direction(self, gesture_name, hand_landmarks):
        """
        Determine gesture direction based on hand position.
        For pointing gestures, determine if pointing left or right.
        """
        if not hand_landmarks or gesture_name not in ["point_right", "point_left"]:
            return gesture_name
        
        # Use wrist position to determine hand orientation
        wrist = hand_landmarks.landmark[0]  # Wrist landmark
        
        # Simple heuristic: if wrist is on the left side, pointing right
        # This will be refined with actual hand orientation later
        if wrist.x < 0.5:  # Left side of frame
            return "point_right"
        else:  # Right side of frame
            return "point_left"