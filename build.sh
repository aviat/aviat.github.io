#!/bin/bash

# Build the Docker image for ARM64
docker build --platform linux/arm64 -t jekyll-site .

# Run the container and copy the built site
docker run --rm -v $(pwd)/_site:/srv/jekyll/_site jekyll-site 