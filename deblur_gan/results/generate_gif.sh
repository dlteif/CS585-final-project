#!/bin/sh

palette="/tmp/palette.png"


ffmpeg -v warning -i $1 -vf "palettegen" -y $palette
ffmpeg -v warning -i $1 -i $palette -lavfi "paletteuse" -y $2
