import cv2
import time
import mediapipe as mp

# from mediapipe.tasks import python
# from mediapipe.tasks.python import vision

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Failed to open webcam")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('Sign Language Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break