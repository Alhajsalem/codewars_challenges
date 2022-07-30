#!/bin/bash

foo=$1
RESULT=""
for (( i=0; i<${#foo}; i++ )); do
  if [[ "${foo:$i:1}" == "#" ]]; then
  break
  fi
  RESULT+="${foo:$i:1}"  
done

echo $RESULT


#!/bin/bash

removeUrlAnchor(){
stripcode=`echo $1|sed 's/#/ /g'|awk '{print $1}'`
echo $stripcode
}

removeUrlAnchor $1