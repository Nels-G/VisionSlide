"""
Setup script for VisionSlide package.
"""
from setuptools import setup, find_packages

setup(
    name="visionslide",
    version="1.0.0",
    author="Nelson Galley (Nels-G)",
    author_email="nelsgalley@gmail.com",
    description="Control PowerPoint presentations with hand gestures using AI-powered computer vision",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.8.0",
        "mediapipe>=0.10.0", 
        "pyautogui>=0.9.0",
        "numpy>=1.21.0"
    ],
    entry_points={
        "console_scripts": [
            "visionslide=visionslide.app:main",  
        ],
    },
    python_requires=">=3.9",
)