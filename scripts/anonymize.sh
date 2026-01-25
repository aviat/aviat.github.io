#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 file1 [file2 [...]]"
    echo "  Anonymize images (remove metadata) or movies (remove sound)"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

for f in "$@"; do
    if [ ! -f "$f" ]; then
        echo "Skipping non-file: $f"
        continue
    fi

    mime=$(file --brief --mime-type "$f")

    case "$mime" in
        image/*)
            echo "Image detected: $f"
            "$SCRIPT_DIR/remove-img-metadata.sh" "$f"
            ;;
        video/*)
            echo "Movie detected: $f"
            "$SCRIPT_DIR/remove-sound.sh" "$f"
            ;;
        *)
            echo "Unknown type ($mime), skipping: $f"
            ;;
    esac
done
