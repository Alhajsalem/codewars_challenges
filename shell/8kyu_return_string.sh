# https://www.codewars.com/kata/55a70521798b14d4750000a4/train/shell
# FUNDAMENTALS STRINGS

!/bin/bash
getval="Hello, ${1} how are you doing today?"  
echo $getval

#!/bin/bash
printerError() {
foo=$1
count_there=0
count_not_there=0
for (( i=0; i<${#foo}; i++ )); do
  if [[ "abcdefghijklm" =~ "${foo:$i:1}" ]]; then
   count_there=$((count_there+1))
  else
  count_not_there=$((count_not_there+1))
  fi
done
echo $count_not_there/${#foo}
}
printerError $1

#!/bin/bash
printerError() {
  ERRORS=`echo $1 | sed "s/[a-m]//g" `
  echo "${#ERRORS}/${#1}"
}
printerError $1