#!/usr/bin/env bash
set -euo pipefail

for f in "$@"; do
  if [ ! -f "$f" ]; then
    echo "Skipping non-file: $f"
    continue
  fi

  # Extract rotation value using ffprobe
  # rotation=$(ffprobe -v quiet -select_streams v:0 \
  #       -show_entries stream_tags=rotate \
  #       -of default=nw=1:nk=1 "$f" 2>/dev/null || echo "")

  rotation=$(exiftool -Rotation $f |awk '{print $3}')

  case "$rotation" in
    90|270)
      echo "Rotating $f (was $rotation)…"
      exiftool -Rotation=0 $f
      ;;
    *)
      echo "Already horizontal: $f"
      ;;
  esac
done
