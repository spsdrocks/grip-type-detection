# ========================= Imports =========================

import cv2
import mediapipe as mp
import numpy as np



# ========================= Function Definitions =========================

def getAngle(landmarkOne, landmarkTwo, landmarkThree):
    """Gets the angle at a joint based on position of surrounding ones

    :landmarkOne: Joint closer to wrist
    :landmarkTwo: Joint of interest
    :landmarkThree: Joint further from wrist
    :Return: Current Angle in degrees"""

    # Convert landmarks to vectors
    vectorOne = np.array([landmarkOne.x - landmarkTwo.x, landmarkOne.y - landmarkTwo.y, landmarkOne.z - landmarkTwo.z])
    vectorTwo = np.array([landmarkTwo.x - landmarkThree.x, landmarkTwo.y - landmarkThree.y, landmarkTwo.z - landmarkThree.z])

    # Get length of vectors
    magOne = np.linalg.norm(vectorOne)
    magTwo = np.linalg.norm(vectorTwo)

    # Get the angle using dot product formula
    resultAngle = np.arccos(np.dot(vectorOne, vectorTwo) / (magOne * magTwo))

    return np.degrees(resultAngle)

def getFingerGrip(fingerAngleOne, fingerAngleTwo):
    """Gets a grip type score given a fingers angles
    
    :fingerAngleOne: The angle at the middle joint
    :fingerAngleTwo: The angle at the front joint
    :Return: Angle score scaled on [0, 2] representing grip type"""

    # Finish this
    return 0

def totalGrip(scorePointer, scoreMiddle, scoreRing):
    """Gets the total grip score of the hand
    
    :scorePointer: The grip score of the pointer finger
    :scoreMiddle: The grip score of the middle finger
    :scoreRing: The grip score of the ring finger
    :Return: Total grip score on [0, 2] of the hand"""

    # Finish this
    return 0



# ========================= Main =========================

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
inputVideo = cv2.VideoCapture("media/test_video_2.mp4")

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

    # Get angle for each fingers middle joint
    pointerAngleOne = getAngle(hand_landmarks[5], hand_landmarks[6], hand_landmarks[7])
    middleAngleOne = getAngle(hand_landmarks[9], hand_landmarks[10], hand_landmarks[11])
    ringAngleOne = getAngle(hand_landmarks[13], hand_landmarks[14], hand_landmarks[15])

    # Get angle for each fingers outside joint
    pointerAngleTwo = getAngle(hand_landmarks[6], hand_landmarks[7], hand_landmarks[8])
    middleAngleTwo = getAngle(hand_landmarks[10], hand_landmarks[11], hand_landmarks[12])
    ringAngleTwo = getAngle(hand_landmarks[14], hand_landmarks[15], hand_landmarks[16])

    # Print the angles on the video
    # anglesString = "P: {}, M: {}, R: {}".format(round(np.degrees(pointerAngleOne), 2), round(np.degrees(middleAngleOne), 2), round(np.degrees(ringAngleOne), 2))
    # cv2.putText(videoFrame, anglesString, (5, 120), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0))

    # Write the processed frame to output video
    outputVideo.write(videoFrame)

    # Increment frame number    
    frameNumber += 1

# Release capturer and writer
inputVideo.release()
outputVideo.release()