#!/bin/bash
if [ "$1" == "us" ]; then
  while true
  do
      clear
      TZ=America/New_York date
      echo $TZ
      sleep 1
  done
fi
if [ "$1" == "sk" ]; then
  while true
  do
      clear
      TZ=Asia/Seoul date
      echo $TZ
      sleep 1
  done
fi
if [ "$1" == "no" ]; then
  while true
  do
      clear
      #mumbo jumbo to read
      echo $(date)
      sleep 1
  done
fi
