#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 2 ] ; then
    echo "Usage: $0 img1 [img2 [...]]"
    echo "  remove privacy sensitive metadata from Exif"
    exit 1
fi;


# Loop over all arguments
for f in "$@"; do
  if [ ! -f "$f" ]; then
    echo "Skipping non-file: $f"
    continue
  fi

  echo "Sanitizing: $f"
  exiftool -all= \
    -tagsfromfile @ \
    -Orientation -ThumbnailImage -XMP:all -IPTC:all -ICC_Profile \
    -overwrite_original "$f"
done

