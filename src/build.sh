#!/bin/bash

# copy markdown files locally for inclusion in docker container.
cp -r ../markdown ./

# build docker image.
#docker build -t fiaf_manual .

# run container.
#docker run -d -i -v ./render:/render fiaf_manual 

