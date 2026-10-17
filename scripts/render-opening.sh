#!/usr/bin/env bash
# Jakarta-to-Asia map, then SECHA's supplied modular assembly film.
# Requires Python matplotlib and ffmpeg. Uses source data bundled alongside script.
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
secha_frame_dir="$(mktemp -d /tmp/secha-map-frames.XXXXXX)"
trap 'rm -rf "$secha_frame_dir"' EXIT
MPLCONFIGDIR="$secha_frame_dir/mpl" XDG_CACHE_HOME="$secha_frame_dir/cache" python3 "$secha_repo_dir/scripts/render-indonesia-map.py" --output "$secha_frame_dir"
ffmpeg -hide_banner -loglevel error -y -framerate 24 -i "$secha_frame_dir/%04d.png"   -i "$secha_source_film" -filter_complex_threads 1 -filter_complex   '[0:v]fps=24,format=yuv420p,settb=AVTB[map];[1:v]setpts=1.2*PTS,fps=24,eq=saturation=0.72:contrast=1.02:brightness=0.005,colorbalance=rm=0.015:bm=-0.02,format=yuv420p,settb=AVTB[assembly];[map][assembly]xfade=transition=fade:duration=0.45:offset=2.05,format=yuv420p[out]'   -map '[out]' -an -c:v libx264 -preset medium -crf 21 -movflags +faststart "$secha_repo_dir/assets/film/opening.mp4"
ffmpeg -hide_banner -loglevel error -y -ss 0.7 -i "$secha_repo_dir/assets/film/opening.mp4"   -frames:v 1 "$secha_repo_dir/assets/film/opening-poster.jpg"
