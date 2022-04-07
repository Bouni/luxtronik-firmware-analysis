#!/bin/sh

# Get filename via Head request
filename=$(curl -s -I https://www.heatpump24.com/software/fetchSoftware.php?softwareID=2 | grep -oP 'wp2reg-V\d+.\d+.\d+')
echo "Latest firmware is $filename"

curl -s 'https://www.heatpump24.com/software/fetchSoftware.php?softwareID=2' --output "$filename.gz"
echo "Downloaded as $filename.gz"

echo "Decompress downloaded firmware"
gzip -qdkc "$filename.gz" | tar xf -
rm "$filename.gz"

echo "Verify Checksum"
find . -name 'home.wp2reg*.md5' -print0 | xargs -0 md5sum -c

if [ $? -ne 0  ]; then
    echo "Error, checksum does not match!"
    exit $?
fi

# Delete md5 sum file, not needed anymore
rm home.wp2reg*.md5

# Rename tar file to make tar happy
filename=$(find . -name 'home.wp2reg*')
mv $filename "$filename.tar" 

# Make a new directory for untared firmware
mkdir firmware >/dev/null 2>&1

echo "Extract firmware into ./firmware"
tar xf "$filename.tar" -C firmware

# Delete tar ball
rm "$filename.tar" 


