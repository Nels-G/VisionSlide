"""
Camera management module for VisionSlide.
Handles video capture and frame processing.
"""
import cv2
import time
from visionslide.config import *
from visionslide.utils.logger import setup_logger

class CameraStream:
    """Manages camera capture and frame processing."""
    
    def __init__(self, camera_index=CAMERA_INDEX):
        self.logger = setup_logger('CameraStream')
        self.camera_index = camera_index
        self.cap = None
        self.frame_count = 0
        self.fps = 0
        self.last_time = time.time()
        self._is_running = False
        
    def initialize(self):
        """Initialize camera capture."""
        try:
            self.cap = cv2.VideoCapture(self.camera_index)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
            self.cap.set(cv2.CAP_PROP_FPS, FPS_TARGET)
            
            if not self.cap.isOpened():
                raise Exception(f"Could not open camera index {self.camera_index}")
            
            self._is_running = True
            self.logger.info(f"Camera initialized: {FRAME_WIDTH}x{FRAME_HEIGHT} @ {FPS_TARGET}FPS")
            return True
            
        except Exception as e:
            self.logger.error(f"Camera initialization failed: {e}")
            return False
    
    def read_frame(self):
        """Read a frame from the camera and calculate FPS."""
        if not self._is_running or not self.cap or not self.cap.isOpened():
            return None
        
        ret, frame = self.cap.read()
        if not ret:
            self.logger.error("Failed to read frame from camera")
            return None
        
        # Calculate FPS
        self.frame_count += 1
        current_time = time.time()
        if current_time - self.last_time >= 1.0:
            self.fps = self.frame_count
            self.frame_count = 0
            self.last_time = current_time
        
        return frame
    
    def release(self):
        """Release camera resources."""
        self._is_running = False
        if self.cap:
            self.cap.release()
            cv2.destroyAllWindows()
            self.logger.info("Camera resources released")
    
    def get_resolution(self):
        """Get current camera resolution."""
        if self.cap and self.cap.isOpened():
            width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            return width, height
        return FRAME_WIDTH, FRAME_HEIGHT
    
    def get_fps(self):
        """Get current FPS."""
        return self.fps
    
    def is_running(self):
        """Check if camera is running."""
        return self._is_running