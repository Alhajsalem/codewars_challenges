#https://www.codewars.com/kata/584857c5a7878e993b0005cc/train/shell
#!/bin/bash
if [ "$1" = "" ]
then
    echo "Nothing to find"
    exit 3
fi
DIR=$1
if [ -d "$DIR" ]; then
    Result=$(find $1 -type f | wc -l)
    echo "There are ${Result} files in /home/codewarrior/shell/${1}"  
else 
    echo "Directory not found"
fi


