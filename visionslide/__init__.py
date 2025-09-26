"""
VisionSlide - Control PowerPoint presentations with hand gestures.
"""

__version__ = "1.0.0"
__author__ = "Nelson Galley"
__email__ = "nelsgalley@gmail.com"

# Import des modules principaux
from visionslide.camera.camera_stream import CameraStream
from visionslide.gestures.gesture_detector import GestureDetector
from visionslide.gestures.gesture_mapping import GestureMapper
from visionslide.controls.ppt_controller import PPTController

__all__ = [
    "CameraStream",
    "GestureDetector", 
    "GestureMapper",
    "PPTController",
]