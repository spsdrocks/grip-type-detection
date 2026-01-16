docker build -t grip-type-detection .

docker run -it --rm -v "$(pwd)/media":/usr/src/app/media grip-type-detection