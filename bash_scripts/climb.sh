#!/bin/bash
x=0
while [ $x -le $1 ]
do
  cd ..
  x=$(( $x + 1 ))
done
