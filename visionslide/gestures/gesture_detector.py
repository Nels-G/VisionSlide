"""
Gesture detection module using MediaPipe Hands.
"""
import cv2
import mediapipe as mp
from visionslide.config import *
from visionslide.utils.logger import setup_logger

class GestureDetector:
    """Hand gesture detection using MediaPipe."""
    
    def __init__(self):
        self.logger = setup_logger('GestureDetector')
        
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        self.hands = self.mp_hands.Hands(
            model_complexity=MODEL_COMPLEXITY,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE,
            max_num_hands=1  # Detect only one hand for simplicity
        )
        
        self.logger.info("Gesture detector initialized")
    
    def detect_gestures(self, frame):
        """
        Detect hand gestures in a frame.
        Returns:
            - Processed frame with landmarks
            - List of hand landmarks if detected, None otherwise
        """
        if frame is None:
            return frame, None
        
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame.flags.writeable = False
        
        # Process the frame
        results = self.hands.process(rgb_frame)
        
        # Convert back to BGR
        rgb_frame.flags.writeable = True
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
        
        hand_landmarks = None
        
        # Draw hand landmarks if detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks on frame
                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style()
                )
            
            hand_landmarks = results.multi_hand_landmarks[0]  # Take first hand
        
        return frame, hand_landmarks
    
    def get_finger_state(self, hand_landmarks):
        """
        Determine which fingers are extended.
        Returns a dictionary with finger states.
        """
        if not hand_landmarks:
            return None
        
        # Finger tip landmarks indices
        finger_tips = {
            'thumb': 4,
            'index': 8,
            'middle': 12,
            'ring': 16,
            'pinky': 20
        }
        
        # Finger PIP (proximal interphalangeal) joints for comparison
        finger_pips = {
            'thumb': 2,
            'index': 6,
            'middle': 10,
            'ring': 14,
            'pinky': 18
        }
        
        finger_state = {}
        
        for finger, tip_idx in finger_tips.items():
            pip_idx = finger_pips[finger]
            
            # Get landmark positions
            tip = hand_landmarks.landmark[tip_idx]
            pip = hand_landmarks.landmark[pip_idx]
            
            # For thumb, we need special logic (compare with different joint)
            if finger == 'thumb':
                # Use the base of the thumb for comparison
                thumb_base = hand_landmarks.landmark[2]
                # Thumb is extended if tip is farther from wrist than base
                finger_state[finger] = tip.y < thumb_base.y
            else:
                # Finger is extended if tip is above PIP joint
                finger_state[finger] = tip.y < pip.y
        
        return finger_state
    
    def recognize_gesture(self, hand_landmarks):
        """
        Recognize specific gestures from hand landmarks.
        Returns gesture name or None.
        """
        if not hand_landmarks:
            return None
        
        finger_state = self.get_finger_state(hand_landmarks)
        if not finger_state:
            return None
        
        # Gesture: Pointing right (only index finger extended)
        if (finger_state['index'] and 
            not finger_state['middle'] and 
            not finger_state['ring'] and 
            not finger_state['pinky']):
            return "point_right"
        
        # Gesture: Pointing left (only index finger extended, but we'll determine direction later)
        elif (finger_state['index'] and 
              not finger_state['middle'] and 
              not finger_state['ring'] and 
              not finger_state['pinky']):
            return "point_left"  # Direction will be determined by hand position
        
        # Gesture: Closed fist (no fingers extended)
        elif (not finger_state['index'] and 
              not finger_state['middle'] and 
              not finger_state['ring'] and 
              not finger_state['pinky']):
            return "fist"
        
        # Gesture: Open hand (all fingers extended)
        elif (finger_state['index'] and 
              finger_state['middle'] and 
              finger_state['ring'] and 
              finger_state['pinky']):
            return "open_hand"
        
        return None
    
    def release(self):
        """Release resources."""
        self.hands.close()
        self.logger.info("Gesture detector released")