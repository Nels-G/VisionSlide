"""
Test script for gesture detection.
"""
import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import cv2
    from visionslide.camera.camera_stream import CameraStream
    from visionslide.gestures.gesture_detector import GestureDetector
    from visionslide.gestures.gesture_mapping import GestureMapper
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

def test_gestures():
    """Test gesture detection functionality."""
    print("Testing VisionSlide Gesture Detection...")
    print("Show your hand to the camera and make gestures:")
    print("- Point with index finger → Point gesture")
    print("- Close fist → Fist gesture")
    print("- Open hand → Open hand gesture")
    print("Press 'q' to quit")
    
    # Initialize components
    camera = CameraStream()
    gesture_detector = GestureDetector()
    gesture_mapper = GestureMapper()
    
    if not camera.initialize():
        print("❌ Camera initialization failed")
        return
    
    print("✅ Gesture detection test started")
    
    try:
        while camera.is_running():
            frame = camera.read_frame()
            if frame is None:
                break
            
            # Detect gestures
            processed_frame, hand_landmarks = gesture_detector.detect_gestures(frame)
            
            gesture_name = None
            if hand_landmarks:
                gesture_name = gesture_detector.recognize_gesture(hand_landmarks)
                
                # Determine direction for pointing gestures
                if gesture_name and ("point" in gesture_name):
                    gesture_name = gesture_mapper.determine_direction(gesture_name, hand_landmarks)
            
            # Display gesture information
            fps = camera.get_fps()
            cv2.putText(processed_frame, f"FPS: {fps}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            status_text = f"Gesture: {gesture_name if gesture_name else 'None'}"
            cv2.putText(processed_frame, status_text, (10, 70), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Check if action should be triggered
            if gesture_name:
                action = gesture_mapper.update_gesture(gesture_name, hand_landmarks)
                if action:
                    action_text = f"Action: {action}"
                    cv2.putText(processed_frame, action_text, (10, 110), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    print(f"🎯 Action triggered: {action}")
            
            cv2.imshow('VisionSlide Gesture Test', processed_frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:
                print("Quit signal received")
                break
                
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    
    finally:
        gesture_detector.release()
        camera.release()
        print("✅ Gesture test completed")

if __name__ == "__main__":
    test_gestures()