# VisionSlide 🎥➡️📊

VisionSlide is an experimental project that allows you to **control Microsoft PowerPoint presentations using computer vision and hand gestures**.  
No more clickers – just your camera, your hands, and AI-powered interaction. 🚀

---

## ✨ Features (MVP)
- Move to **next slide** with a hand gesture
- Move to **previous slide** with a hand gesture  
- Close PowerPoint with a specific gesture
- Real-time hand tracking and gesture recognition
- (Planned) Use gestures to highlight or point during a presentation

---

## 🛠️ Tech Stack
- **Python 3.9+**
- [OpenCV](https://opencv.org/) → video capture and image processing
- [MediaPipe](https://developers.google.com/mediapipe) → hand & gesture detection
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) → simulate keyboard control for PowerPoint
- [NumPy](https://numpy.org/) → mathematical operations

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- A webcam
- Microsoft PowerPoint installed
- Windows/macOS/Linux compatible

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/visionslide.git
   cd visionslide
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the prototype:
   ```bash
   python app.py
   ```

### Usage
1. Open a PowerPoint presentation
2. Launch VisionSlide
3. Position yourself in front of your camera
4. Use the following gestures:
   - **Next slide**: Point right with index finger
   - **Previous slide**: Point left with index finger
   - **Exit**: Close your fist and hold for 2 seconds

---

## 📁 Project Structure
```
visionslide/
├── app.py                 # Main application entry point
├── gesture_detector.py    # Hand gesture recognition logic
├── presentation_controller.py # PowerPoint control interface
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
└── assets/               # Images and demo files
    └── demo.gif          # Demo video (coming soon)
```

---

## 🎯 Roadmap
- [x] Detect basic gestures (next/previous slide)
- [ ] Add gesture to exit PowerPoint
- [ ] Add gesture to activate a laser pointer
- [ ] Build a GUI to customize gestures
- [ ] Integration with Zoom/Teams presentations
- [ ] Support for Google Slides and other presentation software
- [ ] Voice command integration
- [ ] Multiple hand gesture combinations

---

## 🔧 Configuration
You can customize gesture sensitivity and controls by modifying the configuration in `config.py`:

```python
# Gesture sensitivity (0.1 - 1.0)
GESTURE_CONFIDENCE = 0.7

# Gesture hold time (seconds)
GESTURE_HOLD_TIME = 1.5

# Camera settings
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
```

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎬 Demo
A comprehensive video demo will be added once the first stable prototype is ready.

![Demo GIF placeholder](assets/demo.gif)
*Demo coming soon...*

---

## 🐛 Known Issues
- Lighting conditions may affect gesture recognition accuracy
- Currently optimized for single-user presentations
- Requires stable internet connection for MediaPipe models

---

## 💡 Vision
This project started as an innovative idea to make presentations more **interactive and intuitive**. The long-term vision is to **integrate gesture-based control into Microsoft Office tools** and improve productivity during live or online presentations.

Future possibilities include integration with AR/VR headsets, multi-user gesture control, and AI-powered presentation assistance.

---

## 👤 Author
**Nelson (Nelsbrowser)** – Passionate about AI, computer vision, and building innovative productivity tools.

- GitHub: [@nelsbrowser](https://github.com/nelsbrowser)
- Email: nelson@example.com

---

## 🙏 Acknowledgments
- [MediaPipe](https://developers.google.com/mediapipe) team for excellent hand tracking models
- [OpenCV](https://opencv.org/) community for computer vision tools
- Microsoft PowerPoint for inspiration

---

## ⭐ Star this repo
If you find this project interesting, please consider giving it a star! It helps others discover the project.
