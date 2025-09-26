"""
Test script for PowerPoint integration.
"""
import sys
import os
import time

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import cv2
    from visionslide.camera.camera_stream import CameraStream
    from visionslide.gestures.gesture_detector import GestureDetector
    from visionslide.gestures.gesture_mapping import GestureMapper
    from visionslide.controls.ppt_controller import PPTController
    from visionslide.controls.os_controller import OSController
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

def test_ppt_integration():
    """Test complete PowerPoint integration."""
    print("Testing VisionSlide PowerPoint Integration...")
    print("IMPORTANT: Please open PowerPoint and start a slideshow first!")
    print("Gesture commands:")
    print("- 👉 Point right → Next slide")
    print("- 👈 Point left → Previous slide") 
    print("- ✊ Close fist → Exit presentation")
    print("- Press 'q' to quit VisionSlide")
    print()
    
    # Initialize all components
    camera = CameraStream()
    gesture_detector = GestureDetector()
    gesture_mapper = GestureMapper()
    ppt_controller = PPTController()
    os_controller = OSController()
    
    if not camera.initialize():
        print("❌ Camera initialization failed")
        return
    
    # Connect to PowerPoint
    if not ppt_controller.connect():
        print("⚠️  PowerPoint not detected. Gestures will be simulated but may not work.")
    
    print("✅ VisionSlide started successfully")
    print("🎮 Gesture controls are now active!")
    
    try:
        while camera.is_running():
            frame = camera.read_frame()
            if frame is None:
                break
            
            # Detect gestures
            processed_frame, hand_landmarks = gesture_detector.detect_gestures(frame)
            
            gesture_name = None
            action_performed = False
            
            if hand_landmarks:
                gesture_name = gesture_detector.recognize_gesture(hand_landmarks)
                
                # Determine direction for pointing gestures
                if gesture_name and ("point" in gesture_name):
                    gesture_name = gesture_mapper.determine_direction(gesture_name, hand_landmarks)
            
            # Display information
            fps = camera.get_fps()
            cv2.putText(processed_frame, f"FPS: {fps}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            status_text = f"Gesture: {gesture_name if gesture_name else 'None'}"
            cv2.putText(processed_frame, status_text, (10, 70), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Check and execute actions
            if gesture_name:
                action = gesture_mapper.update_gesture(gesture_name, hand_landmarks)
                if action:
                    action_text = f"Action: {action}"
                    cv2.putText(processed_frame, action_text, (10, 110), 
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
                cv2.putText(processed_frame, "ACTION EXECUTED", (10, 150), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            
            cv2.imshow('VisionSlide - PowerPoint Control', processed_frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:
                print("Quit signal received")
                break
                
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    
    finally:
        gesture_detector.release()
        camera.release()
        print("✅ PowerPoint integration test completed")

if __name__ == "__main__":
    test_ppt_integration()