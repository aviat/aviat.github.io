#!/bin/bash

cp Gemfile ./empty/

# Build the Docker image for ARM64
docker build --platform linux/arm64 -t jekyll-site -f Dockerfile ./empty/

echo "Built"
# Run the container and copy the built site
docker run --rm -v $(pwd)/:/srv/jekyll/ -p 4000:4000 -p 35729:35729 jekyll-site
