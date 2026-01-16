docker build -t grip-type-detection .

docker run -it --rm --device=/dev/video0:/dev/video0 grip-type-detection