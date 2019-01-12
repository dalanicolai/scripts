#!/bin/sh

SOURCE=./supplementary_notes.pdf # set to the file name of the PDF
OUTPUT=supplementary_notes.txt # set to the final output file
RESOLUTION=600 # set to the resolution the scanner used (the higher, the better)

touch final.txt
for i in `seq 1 21`; do
    convert -density 300 -type grayscale supplementary_notes.pdf[$i] page$i.tif
    echo processing page $i
    tesseract page$i.tif tempoutput$i
done

for i in page*.tif; do echo $i; tesseract $i $(basename $i .tif) pdf; done

pdftk $(ls page*.pdf | sort -V) cat output merged.pdf

