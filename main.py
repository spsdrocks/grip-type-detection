# Import requird dependencies
import cv2
import time
import mediapipe as mp
import numpy as np

# Converts provided landmarks to vectors and gets the angle between them
def getAngle(landmarkOne, landmarkTwo, landmarkThree):
    # Convert landmarks to vectors
    vectorOne = np.array([landmarkOne.x - landmarkTwo.x, landmarkOne.y - landmarkTwo.y, landmarkOne.z - landmarkTwo.z])
    vectorTwo = np.array([landmarkTwo.x - landmarkThree.x, landmarkTwo.y - landmarkThree.y, landmarkTwo.z - landmarkThree.z])

    # Get length of vectors
    magOne = np.linalg.norm(vectorOne)
    magTwo = np.linalg.norm(vectorTwo)

    # Get the angle using dot product formula
    resultAngle = np.arccos(np.dot(vectorOne, vectorTwo) / (magOne * magTwo))

    return resultAngle

# Load model prerequisites
baseOptions = mp.tasks.BaseOptions
handLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
visionRunningMode = mp.tasks.vision.RunningMode

# Set up model options
modelOptions = handLandmarkerOptions(base_options=baseOptions(model_asset_path='model/hand_landmarker.task'), running_mode=visionRunningMode.VIDEO)

# Create model based on options
handLandmarker = mp.tasks.vision.HandLandmarker
handLandmarker = handLandmarker.create_from_options(modelOptions)

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

# Councter to keep track of current frame number
frameNumber = 0

# Loop to process frames
while (inputVideo.isOpened()):
    # Load video frame
    videoReturn, videoFrame = inputVideo.read()

    # Next loop iteration if no frame found
    if not videoReturn:
        break

    # Convert frame to model format
    currentFrameRGB = cv2.cvtColor(videoFrame, cv2.COLOR_BGR2RGB)
    currentFrameMP = mp.Image(image_format=mp.ImageFormat.SRGB, data=currentFrameRGB)

    # Calculate frame timestamp
    frameTimestamp = int((frameNumber / videoFps) * 1000)

    # Use model on current frame
    modelResults = handLandmarker.detect_for_video(currentFrameMP, frameTimestamp)

    # Check if model found hand landmarks
    if modelResults.hand_landmarks:
        for hand_landmarks in modelResults.hand_landmarks:
            for landmark in hand_landmarks:
                # Place circles on each identified landmark
                x = int(landmark.x * videoFrame.shape[1])
                y = int(landmark.y * videoFrame.shape[0])
                cv2.circle(videoFrame, (x, y), 4, (0, 255, 0), -1)

    # Write the processed frame to output video
    outputVideo.write(videoFrame)

    # Increment frame number    
    frameNumber += 1

# Release capturer and writer
inputVideo.release()
outputVideo.release()