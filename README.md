# Grip Type Detection

A simple Python program for detecting the type of grip a rock climber is using.

Built with the [hand landmarks model from mediapipe](https://mediapipe.readthedocs.io/en/latest/solutions/hands.html#hand-landmark-model) and [video processor from opencv](https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html).

## Setup

Simple three step setup:

1. Clone the repository onto your machine
2. Upload video into the media folder (or use existing example video)
3. Change `inputVideo` in main.py to point to the video of choice

## Running

### Using Docker

1. Open docker on your machine
2. Navigate to the project root
3. Run the build script:

`docker build -t grip-type-detection .`

4. Run the docker image:

Unix: `docker run -it --rm -v "$(pwd)/media":/usr/src/app/media grip-type-detection`

Powershell: `docker run -it --rm -v "${PWD}/media:/usr/src/app/media" grip-type-detection`

Command Prompt: `docker run -it --rm -v "%cd%/media:/usr/src/app/media" grip-type-detection`

### Using uv

If you have uv installed on your machine

1. Install the correct python into uv:

`uv python install 3.13`

2. Navigate to the project root

3. Install the dependencies:

`uv pip sync uv.lock`

4. Run the program with uv:

`uv run python main.py`