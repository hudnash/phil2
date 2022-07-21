#!/bin/bash
cd ..;
cd data/unzipped;
for file in *; do
    if [[ $file == *.doc ]] # ; then
    then
        antiword "$file" > "${file%.*}.pdf";
    fi
done;
for filename in *; do
  # this syntax emits the value in lowercase: ${var,,*}  (bash version 4)
  case "${filename,,*}" in
    *pdf) mv "$filename" "-/data/pdf" ;;
    *doc) ;;
  esac
done
