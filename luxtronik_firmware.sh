#!/bin/bash
echo "======================================="
echo "Luxtronik firmware download and extract"
echo "======================================="
echo ""
echo "0 => Firmware 1.xx.x"
echo "1 => Firmware 2.xx.x"
echo "2 => Firmware 3.xx.x"
echo "3 => Firmware 4.xx.x"
echo "4 => Firmware F1.xx.x"
echo ""

read -p "Select software ID out of 0, 1, 2, 3, 4: " softwareID

# delete old stuff
rm -rf firmware

echo "https://www.heatpump24.com/software/fetchSoftware.php?softwareID=$softwareID"

# Get filename via Head request
filename=$(curl -s -I "https://www.heatpump24.com/software/fetchSoftware.php?softwareID=$softwareID" | grep -oP 'wp2?reg[-.][VF]\d+.\d+.\d+')
echo "Latest firmware is $filename"

if [[ "$filename" == *"wpreg."* ]]; then
	curl -s "https://www.heatpump24.com/software/fetchSoftware.php?softwareID=$softwareID" --output "$filename"
	echo "Downloaded as $filename"
	echo "Decompress downloaded firmware"
	./extract_V1_firmware.py $filename
	read -p "Do you want to delete the archive file? [yN] " yn
	if [[ "$yn" == "y" ]]; then
		rm $filename
	fi
	exit
else
	curl -s "https://www.heatpump24.com/software/fetchSoftware.php?softwareID=$softwareID" --output "$filename.gz"
	echo "Downloaded as $filename.gz"
fi

# Get the filenames before extracting
files=($(gzip -qdkc $filename.gz | tar tf -))

gz=${files[0]}
md5=${files[1]}

echo $gz
echo $md5

echo "Decompress downloaded firmware"
gzip -qdkc "$filename.gz" | tar xf -

rm "$filename.gz"

echo "Verify Checksum"
md5sum -c $md5

if [ $? -ne 0 ]; then
	echo "Error, checksum does not match!"
	exit $?
fi

# Delete md5 sum file, not needed anymore
rm $md5

# Rename tar file to make tar happy
tar="$gz.tar"
mv $gz "$tar"

# Make a new directory for untared firmware
mkdir firmware >/dev/null 2>&1

echo "Extract firmware into ./firmware"
tar xf $tar -C firmware

# Delete tar ball
read -p "Do you want to delete the archive file? [yN] " yn
if [[ "$yn" == "y" ]]; then
	rm $tar
fi
