import cv2
import time
import mediapipe as mp

# from mediapipe.tasks import python
# from mediapipe.tasks.python import vision

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Failed to open webcam")
    exit()
