#!/bin/sh

set -ex

if [ $# -ne 1 ] ; then 
    echo "Usage: $0 video.mov"
    echo "  creates silent_video.mov, with sound striped"
    exit 1
fi;

dir=$(dirname $1)
name=$(basename $1)

ffmpeg -i $1 -map_metadata -1 -c copy -an ${dir}/silent_${name}
