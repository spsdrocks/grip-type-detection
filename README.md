docker build -t grip-type-detection .

Unix: docker run -it --rm -v "$(pwd)/media":/usr/src/app/media grip-type-detection
Powershell: docker run -it --rm -v "${PWD}/media:/usr/src/app/media" grip-type-detection
Command Prompt: docker run -it --rm -v "%cd%/media:/usr/src/app/media" grip-type-detection