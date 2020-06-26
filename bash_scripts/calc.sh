echo $@

if [ "$#" == "0" ]; then
  echo 'please write in letter and numbers in command line'
fi


if [ "$1" == "S" ]; then
  counter=0
  shift
  for n in $@; do
      let "counter+=n"
  done
  echo $counter
fi

#space
if [ "$1" == "P" ]; then
  counter=1
  shift
  for n in $@; do
    let "counter=counter*n"
  done
  echo $counter
fi
#space
if [ "$1" == "M" ]; then
  shift
  counter=0
  for n in $@; do
    if [ "$n" -gt "$counter" ]; then
      counter=$n
    fi
  done
  echo $counter
fi

if [ "$1" == "m" ]; then
  shift
  counter=$1
  for n in $@; do
    if [ "$n" -lt  "$counter" ]; then
      counter=$n
    fi
  done
  echo $counter
fi
