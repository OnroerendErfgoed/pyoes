#!/bin/bash
cd ../static/extensions/pyoes/templates/pinpoints/pinpoints
for d in $(find * -type d)
do
	echo "Converting $d"
	cd $d
	rm -f *-half.png
	rm -f *-quarter.png
	filelist=`ls | grep '.png'`
	for image_file in $filelist
	do
		inname=`convert $image_file -format "%t" info:`
		convert $image_file -resize 50% ${inname}-half.png
		convert $image_file -resize 25% ${inname}-quarter.png
	done
	cd ..
done
