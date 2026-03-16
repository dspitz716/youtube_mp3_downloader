#!/bin/bash

# convert_mp3_to_mp4.sh
# Converts all MP3 files in a directory to MP4 using ffmpeg
# Usage: ./convert_mp3_to_mp4.sh [input_dir] [output_dir]

# ── Dependencies ────────────────────────────────────────────────────────────────
if ! command -v ffmpeg &>/dev/null; then
  echo "❌ ffmpeg not found. Install it with: brew install ffmpeg"
  exit 1
fi

# ── Arguments ───────────────────────────────────────────────────────────────────
INPUT_DIR="${1:-.}"          # Default: current directory
OUTPUT_DIR="${2:-$INPUT_DIR/mp4_output}"  # Default: mp4_output/ subfolder

mkdir -p "$OUTPUT_DIR"

# ── Conversion ──────────────────────────────────────────────────────────────────
shopt -s nullglob
MP3_FILES=("$INPUT_DIR"/*.mp3)

if [[ ${#MP3_FILES[@]} -eq 0 ]]; then
  echo "⚠️  No MP3 files found in: $INPUT_DIR"
  exit 0
fi

echo "🎵 Found ${#MP3_FILES[@]} MP3 file(s). Starting conversion..."
echo "📁 Output directory: $OUTPUT_DIR"
echo "────────────────────────────────────────────"

SUCCESS=0
FAIL=0

for INPUT_FILE in "${MP3_FILES[@]}"; do
  BASENAME=$(basename "$INPUT_FILE" .mp3)
  OUTPUT_FILE="$OUTPUT_DIR/$BASENAME.mp4"

  echo "▶  Converting: $BASENAME.mp3"

  ffmpeg -y \
    -i "$INPUT_FILE" \
    -vn \
    -acodec aac \
    -b:a 192k \
    "$OUTPUT_FILE" \
    -loglevel error

  if [[ $? -eq 0 ]]; then
    echo "   ✅ Done → $OUTPUT_FILE"
    ((SUCCESS++))
  else
    echo "   ❌ Failed: $BASENAME.mp3"
    ((FAIL++))
  fi
done

echo "────────────────────────────────────────────"
echo "✅ Converted: $SUCCESS  |  ❌ Failed: $FAIL"