import cv2
import time
import mediapipe as mp

# from mediapipe.tasks import python
# from mediapipe.tasks.python import vision

inputVideo = cv2.VideoCapture("media/test_video.mp4")

if not inputVideo.isOpened():
    print("Video failed to open")
    exit()

videoFps = inputVideo.get(cv2.CAP_PROP_FPS)
videoWidth = int(inputVideo.get(cv2.CAP_PROP_FRAME_WIDTH))
videoHeight = int(inputVideo.get(cv2.CAP_PROP_FRAME_HEIGHT))

outputVideo = cv2.VideoWriter("media/output_video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), videoFps, (videoWidth, videoHeight))

while (inputVideo.isOpened()):
    videoReturn, videoFrame = inputVideo.read()

    if not videoReturn:
        break

    # add hand detection and overlay here next time
    
    outputVideo.write(videoFrame)

inputVideo.release()
outputVideo.release()