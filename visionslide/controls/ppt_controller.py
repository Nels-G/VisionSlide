"""
PowerPoint control module for VisionSlide.
Simulates keyboard inputs to control PowerPoint presentations.
"""
import pyautogui
import time
from visionslide.utils.logger import setup_logger

class PPTController:
    """Controls PowerPoint presentations using keyboard simulations."""
    
    def __init__(self):
        self.logger = setup_logger('PPTController')
        self.is_connected = False
        self.last_action_time = 0
        self.action_cooldown = 0.5  # Prevent multiple rapid actions
        
        # Configure pyautogui for safety
        pyautogui.FAILSAFE = True  # Move mouse to corner to abort
        pyautogui.PAUSE = 0.1      # Small pause between actions
        
        self.logger.info("PPT Controller initialized")
    
    def check_powerpoint_running(self):
        """
        Check if PowerPoint is running and in slideshow mode.
        This is a basic check - we'll assume user has started slideshow.
        """
        # For now, we'll assume PowerPoint is running
        # In a more advanced version, we could check processes
        return True
    
    def connect(self):
        """Connect to PowerPoint presentation."""
        if self.check_powerpoint_running():
            self.is_connected = True
            self.logger.info("Connected to PowerPoint presentation")
            return True
        else:
            self.logger.warning("PowerPoint not detected. Please start a slideshow.")
            return False
    
    def next_slide(self):
        """Go to next slide."""
        if not self._can_perform_action():
            return False
        
        try:
            pyautogui.press('right')
            pyautogui.press('pagedown')
            # Try both keys for compatibility
            self.logger.info("Next slide action performed")
            self.last_action_time = time.time()
            return True
        except Exception as e:
            self.logger.error(f"Next slide failed: {e}")
            return False
    
    def previous_slide(self):
        """Go to previous slide."""
        if not self._can_perform_action():
            return False
        
        try:
            pyautogui.press('left')
            pyautogui.press('pageup')
            # Try both keys for compatibility
            self.logger.info("Previous slide action performed")
            self.last_action_time = time.time()
            return True
        except Exception as e:
            self.logger.error(f"Previous slide failed: {e}")
            return False
    
    def exit_presentation(self):
        """Exit slideshow mode."""
        if not self._can_perform_action():
            return False
        
        try:
            pyautogui.press('esc')
            self.logger.info("Exit presentation action performed")
            self.last_action_time = time.time()
            return True
        except Exception as e:
            self.logger.error(f"Exit presentation failed: {e}")
            return False
    
    def _can_perform_action(self):
        """Check if we can perform an action (cooldown and connection)."""
        if not self.is_connected:
            self.logger.warning("Not connected to PowerPoint")
            return False
        
        current_time = time.time()
        if current_time - self.last_action_time < self.action_cooldown:
            return False
        
        return True
    
    def disconnect(self):
        """Disconnect from PowerPoint."""
        self.is_connected = False
        self.logger.info("Disconnected from PowerPoint")