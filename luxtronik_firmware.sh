#!/bin/bash

read -p "Select software ID out of 0, 1, 2, 3, 4: " softwareID

# delete old stuff
rm -rf firmware

echo "https://www.heatpump24.com/software/fetchSoftware.php?softwareID=$softwareID"

# Get filename via Head request
filename=$(curl -s -I "https://www.heatpump24.com/software/fetchSoftware.php?softwareID=$softwareID" | grep -oP 'wp2?reg[-.][VF]\d+.\d+.\d+')
echo "Latest firmware is $filename"

if [[ "$filename" == *"wpreg."*  ]]; then
    curl -s "https://www.heatpump24.com/software/fetchSoftware.php?softwareID=$softwareID" --output "$filename"
    echo "Downloaded as $filename"
    echo "Firmware $filename can be decompressed with python via \"./extract_V1_firmware.py $filename\"."
    exit
else
    curl -s "https://www.heatpump24.com/software/fetchSoftware.php?softwareID=$softwareID" --output "$filename.gz"
    echo "Downloaded as $filename.gz"
fi

exit 0


echo "Decompress downloaded firmware"
gzip -qdkc "$filename.gz" | tar xf -

rm "$filename.gz"

echo "Verify Checksum"
find . -name 'home.*.md5' -print0 | xargs -0 md5sum -c

if [ $? -ne 0  ]; then
    echo "Error, checksum does not match!"
    exit $?
fi

# Delete md5 sum file, not needed anymore
rm home.*.md5

# Rename tar file to make tar happy
filename=$(find . -name 'home.wp2reg*')
mv $filename "$filename.tar" 

# Make a new directory for untared firmware
mkdir firmware >/dev/null 2>&1

echo "Extract firmware into ./firmware"
tar xf "$filename.tar" -C firmware

# Delete tar ball
rm "$filename.tar" 


