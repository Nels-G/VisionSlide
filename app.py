"""
VisionSlide - Main Application Entry Point
Control PowerPoint presentations with hand gestures.
"""
import cv2
import sys
import os

# Add the visionslide package to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from visionslide.camera.camera_stream import CameraStream
from visionslide.gestures.gesture_detector import GestureDetector
from visionslide.gestures.gesture_mapping import GestureMapper
from visionslide.controls.ppt_controller import PPTController
from visionslide.controls.os_controller import OSController
from visionslide.config import *

def main():
    """Main application function."""
    print("VisionSlide - PowerPoint Gesture Control")
    print("=" * 40)
    print("Gesture Controls:")
    print("👉 Point RIGHT → Next slide")
    print("👈 Point LEFT → Previous slide") 
    print("✋ Open hand → Exit application")
    print("Press 'q' or ESC to quit")
    print("=" * 40)
    print("IMPORTANT: Start PowerPoint slideshow first!")
    print()
    
    # Initialize components
    camera = CameraStream()
    gesture_detector = GestureDetector()
    gesture_mapper = GestureMapper()
    ppt_controller = PPTController()
    os_controller = OSController()
    
    # Initialize camera
    if not camera.initialize():
        print("Failed to initialize camera. Please check your webcam.")
        return
    
    # Connect to PowerPoint
    ppt_controller.connect()
    
    print("VisionSlide started successfully!")
    print("Gesture controls are now active...")
    
    try:
        while camera.is_running():
            # Read frame from camera
            frame = camera.read_frame()
            if frame is None:
                break
            
            # Detect gestures
            processed_frame, hand_landmarks = gesture_detector.detect_gestures(frame)
            
            gesture_name = None
            action_performed = False
            
            if hand_landmarks:
                gesture_name = gesture_detector.recognize_gesture(hand_landmarks)
            
            # Display information on frame
            fps = camera.get_fps()
            cv2.putText(processed_frame, f"FPS: {fps}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            status_text = f"Gesture: {gesture_name if gesture_name else 'None'}"
            cv2.putText(processed_frame, status_text, (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Check and execute actions
            if gesture_name:
                action = gesture_mapper.update_gesture(gesture_name, hand_landmarks, gesture_detector)
                
                if action:
                    action_text = f"Action: {action}"
                    cv2.putText(processed_frame, action_text, (10, 90), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    
                    # Execute the action
                    if action == "next_slide":
                        ppt_controller.next_slide()
                        action_performed = True
                    elif action == "previous_slide":
                        ppt_controller.previous_slide()
                        action_performed = True
                    elif action == "exit":
                        print("Exit gesture detected - stopping VisionSlide")
                        break
            
            # Show action confirmation
            if action_performed:
                cv2.putText(processed_frame, "ACTION EXECUTED", (10, 120), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            
            # Display frame
            cv2.imshow('VisionSlide - PowerPoint Gesture Control', processed_frame)
            
            # Check for quit key
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # 'q' or ESC
                print("Quit signal received")
                break
                
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
    
    finally:
        # Cleanup
        gesture_detector.release()
        camera.release()
        cv2.destroyAllWindows()
        print("VisionSlide stopped successfully")

if __name__ == "__main__":
    main()