# Import requird dependencies
import cv2
import time
import mediapipe as mp

# Load input video file
inputVideo = cv2.VideoCapture("media/test_video.mp4")

# Quit if file not found
if not inputVideo.isOpened():
    print("Video failed to open")
    exit()

# Load video information to be used in output video
videoFps = inputVideo.get(cv2.CAP_PROP_FPS)
videoWidth = int(inputVideo.get(cv2.CAP_PROP_FRAME_WIDTH))
videoHeight = int(inputVideo.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create output video instance
outputVideo = cv2.VideoWriter("media/output_video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), videoFps, (videoWidth, videoHeight))

# Loop to process frames
while (inputVideo.isOpened()):
    # Load video frame
    videoReturn, videoFrame = inputVideo.read()

    # Next loop iteration if no frame found
    if not videoReturn:
        break

    
    
    # Write the processed frame to output video
    outputVideo.write(videoFrame)

# Release capturer and writer
inputVideo.release()
outputVideo.release()