#!/bin/bash
cd ..;
cd data/unzipped;
# convert file types
for file in *; do
    if [ "${file: -4}" == ".doc" ] # ; then
    then
        unoconv -fpdf "$file";
    fi
done;
# move to separate 'pdf' sibling dir -- difficulty with siblings
# for filename in *; do
  # this syntax emits the value in lowercase: ${var,,*}  (bash version 4)
    # if [ "${filename: -4}" == ".pdf" ]; then
        # mv "$filename" "~/phil/data/pdf/$filename" ;
    # fi
# done
