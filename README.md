# 🚗 Driver Behavior Safety System

A real-time driver monitoring system designed to enhance road safety by detecting fatigue and yawning through computer vision and facial landmark analysis. This system uses Mediapipe and OpenCV to process live webcam feeds and trigger audio alerts when unsafe behaviors are detected.

---

## 🌟 Features
- **Fatigue Detection**: Monitors eye closure over time using the Eye Aspect Ratio (EAR).
- **Yawn Detection**: Identifies excessive mouth opening using the Mouth Aspect Ratio (MAR).
- **Real-Time Alerts**: Plays an alert sound when signs of fatigue or yawning are detected.
- **Lightweight and Efficient**: Runs seamlessly on standard webcams with minimal system requirements.

---

## 🛠️ Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - [Mediapipe](https://google.github.io/mediapipe/) for facial landmark detection.
  - [OpenCV](https://opencv.org/) for real-time video processing.
  - [Pygame](https://www.pygame.org/) for audio alerts.
- **Hardware**: Standard webcam or equivalent video capture device.

---

## 📦 Installation

### Prerequisites
- Python 3.7 or later
- A functional webcam

### Steps to Set Up
- Clone the repository:
   ```bash
   git clone https://github.com/TanishqP07/Driver-Behavior-Safety-System.git
   cd Driver-Behavior-Safety-System
-  Install Dependencies Install the required Python libraries using:
   ```bash
   pip install -r requirements.txt

- Run the Application Start the program with:
  ```bash
    python main.py
  
- Optional:  Modify the alert sound in the script by replacing alert.mp3 with your own audio file in the corresponding line:
  ```bash
  pygame.mixer.music.load(r"C:\path\to\your\alert.mp3")

---

# 📋 Usage

1. Ensure your webcam is connected and functional.
2. Run the `main.py` script.
3. The system will:
   - Monitor your eyes and mouth in real time.
   - Display EAR and MAR values on the screen.
   - Trigger an audio alert if:
     - **Fatigue is detected** (prolonged eye closure).
     - **Yawning is detected** (excessive mouth opening).
4. Press `q` to exit the application.

---

# 🚀 Future Enhancements

- Integration with IoT devices for vehicle-based alerts.
- Improved accuracy using advanced deep learning models.
- Cloud-based logging for long-term behavior analysis.
- Multi-language support for alerts.

---

# 🤝 Contributing

Contributions are welcome! Here's how you can help:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request for review.

---

# 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

# 📫 Contact

For any questions, suggestions, or a collaboration, feel free to reach out:
- **Email**: [tanishq.m.pawar@gmail.com](mailto:tanishq.m.pawar@gmail.com)
- **GitHub**: [TanishqP07](https://github.com/TanishqP07)

