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
        
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        self.hands = self.mp_hands.Hands(
            model_complexity=MODEL_COMPLEXITY,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE,
            max_num_hands=1,
            static_image_mode=False
        )
        
        self.logger.info("Gesture detector initialized")
    
    def detect_gestures(self, frame):
        """Detect hand gestures in a frame."""
        if frame is None:
            return frame, None
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame.flags.writeable = False
        results = self.hands.process(rgb_frame)
        rgb_frame.flags.writeable = True
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
        
        hand_landmarks = None
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style()
                )
            hand_landmarks = results.multi_hand_landmarks[0]
        
        return frame, hand_landmarks
    
    def get_finger_state(self, hand_landmarks):
        """Determine which fingers are extended."""
        if not hand_landmarks:
            return None
        
        finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
        finger_pips = [6, 10, 14, 18]
        
        finger_state = {
            'index': False,
            'middle': False,
            'ring': False,
            'pinky': False
        }
        
        for i in range(4):
            tip = hand_landmarks.landmark[finger_tips[i]]
            pip = hand_landmarks.landmark[finger_pips[i]]
            finger_name = ['index', 'middle', 'ring', 'pinky'][i]
            finger_state[finger_name] = tip.y < pip.y
        
        return finger_state
    
    def recognize_gesture(self, hand_landmarks):
        """
        Gestes simples :
        - 👉 Pointer droite → Suivant
        - 👈 Pointer gauche → Précédent  
        - ✋ Main ouverte → Quitter
        """
        if not hand_landmarks:
            return None
        
        finger_state = self.get_finger_state(hand_landmarks)
        if not finger_state:
            return None
        
        # 👉 Pointer (index seul) → Direction déterminée par position main
        if (finger_state['index'] and 
            not finger_state['middle'] and 
            not finger_state['ring'] and 
            not finger_state['pinky']):
            return "pointing"
        
        # ✋ Main ouverte (tous doigts) → Quitter
        elif (finger_state['index'] and finger_state['middle'] and 
              finger_state['ring'] and finger_state['pinky']):
            return "open_hand"
        
        return None
    
    def get_hand_position(self, hand_landmarks):
        """Get hand position in frame for direction."""
        if not hand_landmarks:
            return "center"
        
        wrist = hand_landmarks.landmark[0]
        if wrist.x < 0.4:
            return "left"
        elif wrist.x > 0.6:
            return "right"
        else:
            return "center"
    
    def release(self):
        """Release resources."""
        self.hands.close()
        self.logger.info("Gesture detector released")