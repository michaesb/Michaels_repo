#!/bin/bash
#fikk ikke \n til å fungere.

echo sed - i "/$2/d" counter.txt


echo $PWD
echo -e "\n"
echo lol

if [ "$1" ==  "-a" ]; then
  echo -e "\n" >> .bookmark
  echo $2 "$PWD" >> .bookmark
fi


if [ "$1" == "-r" ]; then
    echo sed - i "/$2/d" .bookmark
fi
