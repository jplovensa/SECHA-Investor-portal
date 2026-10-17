#!/usr/bin/env bash
# Regrade SECHA's supplied modular assembly film; requires ffmpeg.
set -euo pipefail
if [ "$#" -ne 1 ]; then
  echo "Usage: bash scripts/render-opening.sh /path/to/original/furniture-assembly.mp4" >&2
  exit 2
fi
secha_source_film="$1"
secha_repo_dir="$(cd -- "$(dirname -- "$0")/.." && pwd)"
if [ "$(realpath "$secha_source_film")" = "$(realpath "$secha_repo_dir/assets/film/opening.mp4")" ]; then
  echo "Use the original source film; the generated output cannot be its own input." >&2
  exit 2
fi
ffmpeg -hide_banner -loglevel error -y -i "$secha_source_film" -an   -vf 'setpts=1.2*PTS,fps=24,eq=saturation=0.72:contrast=1.02:brightness=0.005,colorbalance=rm=0.015:bm=-0.02,format=yuv420p'   -c:v libx264 -preset medium -crf 21 -movflags +faststart "$secha_repo_dir/assets/film/opening.mp4"
ffmpeg -hide_banner -loglevel error -y -ss 2.5 -i "$secha_repo_dir/assets/film/opening.mp4"   -frames:v 1 "$secha_repo_dir/assets/film/opening-poster.jpg"
