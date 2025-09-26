"""
Test script for camera functionality.
"""
import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import cv2
    from visionslide.camera.camera_stream import CameraStream
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install required packages: pip install opencv-python mediapipe pyautogui numpy")
    sys.exit(1)

def test_camera():
    """Test camera initialization and frame capture."""
    print("Testing VisionSlide Camera...")
    print("Press 'q' to quit or 'ESC' to exit")
    
    camera = CameraStream()
    
    if not camera.initialize():
        print("❌ Camera initialization failed")
        return
    
    print("✅ Camera initialized successfully")
    
    try:
        while camera.is_running():
            frame = camera.read_frame()
            if frame is None:
                print("❌ Failed to read frame")
                break
            
            # Display FPS and instructions
            fps = camera.get_fps()
            cv2.putText(frame, f"FPS: {fps}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, "Press 'q' or 'ESC' to quit", (10, 70), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            cv2.imshow('VisionSlide Camera Test', frame)
            
            # Better key handling - both 'q' and ESC will work
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # 27 is ESC key
                print("Quit signal received")
                break
                
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    
    finally:
        camera.release()
        print("✅ Camera test completed")

if __name__ == "__main__":
    test_camera()