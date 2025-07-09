# 🖐️ Gesture Volume Controller using MediaPipe & Pycaw

Control your system's volume using **hand gestures** via your webcam! This project utilizes **MediaPipe** for hand tracking, **OpenCV** for real-time video processing, and **Pycaw** to control the system volume.

---


## ⚙️ Features

✅ Real-time hand landmark detection  
✅ Smooth volume control using gesture distance  
✅ FPS counter overlay  
✅ Visual cues with circles and lines  
✅ Modular codebase with reusable tracking module

---

## 📁 Project Structure

```
gesture-volume-controller/
├── handTracking/
│   ├── GestureVolumeControl.py     # Main application script
│   ├── hand_tracking_module.py     # Reusable hand detection module
│   ├── hand_tracking.py            # Optional/utility script
│   └── __pycache__/                # Auto-generated
│
├── venv/                           # Python virtual environment
├── .gitignore
├── requirements.txt                # Required Python packages
└── README.md                       # You're reading it!
```

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/AbhinavRai2004/gesture-volume-controller
   cd gesture-volume-controller
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate          # Windows
   # or
   source venv/bin/activate       # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the project**
   ```bash
   python handTracking/GestureVolumeControl.py
   ```

---

## 🧠 How It Works

- Captures webcam frames using OpenCV.
- Detects 21 hand landmarks using MediaPipe.
- Calculates distance between **landmark 4 (thumb tip)** and **landmark 8 (index tip)**.
- Maps that distance to system volume using Pycaw.
- Provides real-time feedback with visuals and FPS counter.

---

## 📦 Dependencies

- `mediapipe`
- `opencv-python`
- `pycaw`
- `numpy`
- `comtypes`

> 📄 All packages are listed in [`requirements.txt`](./requirements.txt)

---

## 🚀 Future Enhancements

- 🔇 Add gesture for mute/unmute (e.g., pinky + thumb)
- 🎛️ On-screen volume bar
- ⏯️ Gesture-based media controls (play, pause, next, prev)
- 📱 Extend support for other platforms (mobile, Linux audio backend)

---

## 👨‍💻 Author

**Abhinav Rai**

🔗 [LinkedIn](https://www.linkedin.com/in/abhinav2004/)  
⭐ If you find this useful, consider starring the repo and connecting!

---

> 📝 *This is a fun project showcasing how computer vision can enhance human-computer interaction using simple gestures.*
