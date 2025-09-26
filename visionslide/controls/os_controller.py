"""
OS-level controller for cross-platform compatibility.
"""
import platform
import pyautogui
from visionslide.utils.logger import setup_logger

class OSController:
    """Handles OS-specific operations."""
    
    def __init__(self):
        self.logger = setup_logger('OSController')
        self.os_type = platform.system().lower()
        self.logger.info(f"Detected OS: {self.os_type}")
    
    def get_screen_size(self):
        """Get screen size for coordinate calculations."""
        try:
            width, height = pyautogui.size()
            return width, height
        except Exception as e:
            self.logger.error(f"Failed to get screen size: {e}")
            return 1920, 1080  # Default fallback
    
    def is_powerpoint_process_running(self):
        """
        Check if PowerPoint process is running.
        Basic implementation - can be enhanced with psutil later.
        """
        # For MVP, we'll assume user manages PowerPoint manually
        # This can be enhanced with proper process checking
        return True
    
    def bring_powerpoint_to_front(self):
        """
        Try to bring PowerPoint window to front.
        This is OS-specific and may not work perfectly on all systems.
        """
        try:
            if self.os_type == "windows":
                # Windows-specific window management
                pyautogui.hotkey('alt', 'tab')
            elif self.os_type == "darwin":  # macOS
                pyautogui.hotkey('command', 'tab')
            elif self.os_type == "linux":
                # Linux window management varies by desktop environment
                pyautogui.hotkey('alt', 'tab')
            
            self.logger.info("Attempted to bring PowerPoint to front")
            return True
        except Exception as e:
            self.logger.warning(f"Could not bring PowerPoint to front: {e}")
            return False