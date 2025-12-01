#! /bin/bash

for file in ./import/*.svg; do
    mv "${file}" ./svg/
done

for file in ./import/*.png; do
    filename=$(basename -- "$file")
    suffix=$(echo $filename | grep -oE "(-[0-9]+.png)$")
    filename=${filename%"$suffix"}
    size=$(echo $suffix | grep -oE "[0-9]+")
    dir="./png/${size}/"

    if [ ! -d "$dir" ]; then
      mkdir -p "$dir"
    fi
    
    mv "$file" "${dir}${filename}.png"
done
