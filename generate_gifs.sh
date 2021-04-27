#!/bin/bash

for folder in gifs/*; do
    echo $folder
    for f in $folder/*; do
        echo $f
        ffmpeg -y -i $f -vf palettegen palette.png
        ffmpeg -y -i $f -i palette.png -lavfi paletteuse ${f%%.*}.gif
    done
rm -rf folder/*.mp4
done


