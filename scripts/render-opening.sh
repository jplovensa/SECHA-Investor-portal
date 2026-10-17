#!/usr/bin/env bash
# Original interface motion graphic; no website footage or source clip required.
# Requires Python Playwright, system Chromium and ffmpeg.
set -euo pipefail
secha_repo_dir="$(cd -- "$(dirname -- "$0")/.." && pwd)"
secha_frame_dir="$(mktemp -d /tmp/secha-interface-frames.XXXXXX)"
trap 'rm -rf "$secha_frame_dir"' EXIT
python3 "$secha_repo_dir/scripts/render-opening-frames.py" --output "$secha_frame_dir"
ffmpeg -hide_banner -loglevel error -y -framerate 24 -i "$secha_frame_dir/%04d.png" -an -c:v libx264 -pix_fmt yuv420p -preset medium -crf 20 -movflags +faststart "$secha_repo_dir/assets/film/opening.mp4"
ffmpeg -hide_banner -loglevel error -y -ss 4 -i "$secha_repo_dir/assets/film/opening.mp4" -frames:v 1 "$secha_repo_dir/assets/film/opening-poster.jpg"
