import cv2
import mediapipe as mp
import time
import math
import pygame

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize Webcam
cap = cv2.VideoCapture(0)
previous_time = 0

# Thresholds and Landmark Indices
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]
MOUTH = [13, 14, 78, 308, 61, 291]  # Outer lip landmarks
EAR_THRESHOLD = 0.2  # Eye Aspect Ratio threshold
MAR_THRESHOLD = 0.5  # Mouth Aspect Ratio threshold (adjusted after testing)
CLOSURE_FRAMES = 50  # Frames required for fatigue detection
YAWN_FRAMES = 40  # Frames required for yawn detection

# Variables to track consecutive events
consecutive_closed_eyes = 0
consecutive_yawn_frames = 0

# Initialize pygame mixer
pygame.mixer.init()

def play_alert():
    pygame.mixer.music.load(r"C:\Users\pawar\Music\alert.mp3")  # Replace with your alert file path
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_ear(landmarks, eye_indices):
    A = calculate_distance(landmarks[eye_indices[1]], landmarks[eye_indices[5]])
    B = calculate_distance(landmarks[eye_indices[2]], landmarks[eye_indices[4]])
    C = calculate_distance(landmarks[eye_indices[0]], landmarks[eye_indices[3]])
    return (A + B) / (2.0 * C)

def calculate_mar(landmarks, mouth_indices):
    A = calculate_distance(landmarks[mouth_indices[0]], landmarks[mouth_indices[1]])  # Top to bottom
    B = calculate_distance(landmarks[mouth_indices[2]], landmarks[mouth_indices[3]])  # Top corners
    C = calculate_distance(landmarks[mouth_indices[4]], landmarks[mouth_indices[5]])  # Left to right
    return (A + B) / (2.0 * C)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            height, width, _ = frame.shape
            points = [(int(lm.x * width), int(lm.y * height)) for lm in face_landmarks.landmark]

            
            # Calculate EAR (Eye Aspect Ratio)
            left_ear = calculate_ear(points, LEFT_EYE)
            right_ear = calculate_ear(points, RIGHT_EYE)
            avg_ear = (left_ear + right_ear) / 2.0

            # Calculate MAR (Mouth Aspect Ratio)
            mar = calculate_mar(points, MOUTH)

            # Display EAR and MAR values
            cv2.putText(frame, f"EAR: {avg_ear:.2f}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
            cv2.putText(frame, f"MAR: {mar:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

            # Draw landmarks on the frame
            for lm in face_landmarks.landmark:
                x, y = int(lm.x * width), int(lm.y * height)
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
                
            # Check for fatigue
            if avg_ear < EAR_THRESHOLD:
                consecutive_closed_eyes += 1
            else:
                consecutive_closed_eyes = 0

            if consecutive_closed_eyes >= CLOSURE_FRAMES:
                cv2.putText(frame, "FATIGUE DETECTED!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                play_alert()

            # Check for yawn
            if mar > MAR_THRESHOLD:
                consecutive_yawn_frames += 1
            else:
                consecutive_yawn_frames = 0

            if consecutive_yawn_frames >= YAWN_FRAMES:
                cv2.putText(frame, "YAWN DETECTED!", (50, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                play_alert()

    # Display frame with FPS
    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.imshow("Driver Monitoring", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
