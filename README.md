# VisionSlide 🚀

<div align="center">

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macOS%20%7C%20linux-lightgrey.svg)

**Control PowerPoint presentations with hand gestures using AI-powered computer vision**

[🎬 Demo](#demo) • [✨ Features](#features) • [🚀 Installation](#installation) • [⚡ Quick Start](#quick-start) • [🤝 Contributing](#contributing)

</div>

---

## 📖 Overview

VisionSlide revolutionizes presentation control by eliminating the need for traditional clickers. Using advanced computer vision and machine learning, it enables seamless PowerPoint navigation through intuitive hand gestures—perfect for modern presentations, remote meetings, and interactive demos.

### 🎯 Why VisionSlide?

- **🙌 Hands-free control** → More natural and engaging presentations
- **🧠 AI-powered accuracy** → Reliable gesture recognition using MediaPipe
- **🌐 Cross-platform support** → Works on Windows, macOS, and Linux
- **🔌 Easy integration** → Drop-in solution for existing PowerPoint workflows
- **📷 No hardware required** → Uses your existing webcam

---

## ✨ Features

### Current Features

| Feature | Description |
|---------|-------------|
| 🤏 **Smart gesture recognition** | Next/Previous slide navigation |
| ⚡ **Real-time hand tracking** | Fast response time with minimal latency |
| 📊 **PowerPoint integration** | Direct keyboard simulation |
| ⚙️ **Configurable sensitivity** | Customizable gesture thresholds |
| 🖥️ **Multi-platform support** | Windows, macOS, Linux compatible |
| 🛠️ **Simple setup** | Easy installation process |

### 🎮 Gesture Controls

| Gesture | Action | Description |
|---------|--------|-------------|
| 👉 | **Point RIGHT** | Navigate to next slide |
| 👈 | **Point LEFT** | Navigate to previous slide |
| ✋ | **Open hand** | Exit application |

---

## 🚀 Installation

### Method 1: Simple Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/Nels-G/visionslide.git
cd visionslide

# Install and run with one command
pip install -e .
visionslide
```

### Method 2: Traditional Python Setup

```bash
# Clone the repository
git clone https://github.com/Nels-G/visionslide.git
cd visionslide

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m visionslide.app
```

### Method 3: For End Users (No Python required)

Download the standalone executable from [Releases page](https://github.com/Nels-G/visionslide/releases)

---

## ⚡ Quick Start

### Prerequisites

- ✅ Webcam (built-in or external)
- ✅ Microsoft PowerPoint
- ✅ Python 3.9+ (for development version)

### Usage Steps

1. **Install VisionSlide** using one of the methods above
2. **Open PowerPoint** and start your slideshow (`F5`)
3. **Launch VisionSlide** → `visionslide`
4. **Use gestures** in front of your webcam:
   - 👉 Point right → Next slide
   - 👈 Point left → Previous slide
   - ✋ Open hand → Exit application

### 💡 Pro Tips

- Position yourself arm's length from the camera
- Ensure good lighting for better detection
- Hold gestures for 0.7 seconds to activate
- Press `q` or `ESC` to quit anytime

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose | Version |
|------------|---------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Core language | 3.9+ |
| ![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white) | Video capture & processing | 4.8+ |
| ![MediaPipe](https://img.shields.io/badge/MediaPipe-0167C4?style=for-the-badge&logo=google&logoColor=white) | Hand tracking & ML models | 0.10+ |
| PyAutoGUI | System automation | Latest |
| NumPy | Mathematical operations | Latest |

</div>

---

## 📁 Project Structure

```
visionslide/
├── 📱 app.py                    # Application entry point
├── 📋 requirements.txt          # Dependencies
├── 📖 README.md                 # Documentation
├── ⚙️ setup.py                  # Package configuration
│
├── 🎯 visionslide/              # Core package
│   ├── 🔧 config.py             # Configuration settings
│   ├── 📷 camera/               # Camera management
│   ├── 🤏 gestures/             # Gesture recognition
│   ├── 🎮 controls/             # System controllers
│   └── 🛠️ utils/                # Utilities
│
├── 🧪 tests/                    # Unit tests
└── 📸 assets/                   # Media files
```

---

## 🔧 Configuration

Customize VisionSlide behavior in `visionslide/config.py`:

```python
# Gesture Recognition Settings
GESTURE_CONFIDENCE_THRESHOLD = 0.7    # Detection sensitivity (0.1-1.0)
GESTURE_HOLD_DURATION = 0.7          # Seconds to hold gesture
GESTURE_COOLDOWN = 0.4               # Prevent rapid-fire gestures

# Camera Configuration
CAMERA_INDEX = 0                     # Default camera
FRAME_WIDTH = 640                    # Video resolution
FRAME_HEIGHT = 480
FPS_TARGET = 30                      # Target frame rate
```

---

## 🎬 Demo

<div align="center">

*Real-time hand tracking and gesture recognition in action*

![Demo GIF](assets/demo.gif)

</div>

---

## ❓ Frequently Asked Questions

<details>
<summary><strong>Q: Does it work with Google Slides?</strong></summary>

A: Currently, VisionSlide only supports PowerPoint. Google Slides support is planned for future releases.
</details>

<details>
<summary><strong>Q: Can I use it in video conferences?</strong></summary>

A: Yes! It works with Zoom, Teams, and other conferencing tools when sharing your PowerPoint window.
</details>

<details>
<summary><strong>Q: What's the minimum system requirements?</strong></summary>

A: Any modern computer with a webcam and PowerPoint installed. No special hardware required.
</details>

<details>
<summary><strong>Q: How accurate is the gesture recognition?</strong></summary>

A: Very accurate in good lighting conditions. Works best with clear hand gestures.
</details>

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Camera not detected" | Check if another application is using the camera |
| Gestures not recognized | Improve lighting and ensure clear hand visibility |
| PowerPoint not responding | Ensure PowerPoint is in slideshow mode (`F5`) |
| Installation errors | Make sure you have Python 3.9+ installed |

---

## 🤝 Contributing

We welcome contributions from developers, designers, and presentation enthusiasts!

### Quick Contribution Guide

```bash
# 1. Fork and clone the repository
git clone https://github.com/your-username/visionslide.git

# 2. Set up development environment
pip install -e ".[dev]"

# 3. Make your changes and test
python -m pytest tests/

# 4. Submit a pull request
```

### Areas Where We Need Help

- 🎨 **UI/UX Design** → Better user interface
- 🌐 **Multi-language** → Internationalization support
- 📱 **Mobile App** → Companion mobile controller
- 🧪 **Testing** → Cross-platform compatibility
- 📖 **Documentation** → Tutorials and guides

---

## 🔄 Changelog

### v1.0.0 (Current)
- ✅ Basic gesture recognition (point left/right, open hand)
- ✅ PowerPoint integration
- ✅ Real-time webcam processing
- ✅ Cross-platform support
- ✅ Easy installation process

### Coming Soon
- 🔄 Google Slides support
- 🔄 Advanced gesture combinations
- 🔄 GUI configuration interface
- 🔄 Performance optimizations

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

<div align="center">

**Nelson Galley (Nels-G)**

*Passionate about AI, Computer Vision, and Developer Productivity*

[![GitHub](https://img.shields.io/badge/GitHub-Nels--G-black?style=for-the-badge&logo=github)](https://github.com/Nels-G)
[![Email](https://img.shields.io/badge/Email-nelsgalley@gmail.com-red?style=for-the-badge&logo=gmail)](mailto:nelsgalley@gmail.com)

*"Building the future of human-computer interaction, one gesture at a time."*

</div>

---

## 🙏 Acknowledgments

- **MediaPipe Team** → Exceptional hand tracking models
- **OpenCV Community** → Robust computer vision foundation
- **Open Source Community** → Continuous inspiration and support

---

<div align="center">

### ⭐ Support the Project

*Enjoying VisionSlide? Help us grow by giving a star!* ⭐

[![GitHub stars](https://img.shields.io/github/stars/Nels-G/visionslide?style=social)](https://github.com/Nels-G/visionslide/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Nels-G/visionslide?style=social)](https://github.com/Nels-G/visionslide/network/members)

**Ready to revolutionize your presentations?** 🚀

[Get Started](https://github.com/Nels-G/visionslide/releases) • [Report Issue](https://github.com/Nels-G/visionslide/issues) • [Contribute](https://github.com/Nels-G/visionslide/pulls)

---

**Happy presenting!** 🎤✨

</div>
