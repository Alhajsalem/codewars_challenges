#!/bin/bash
local_array=("$@")
#echo ${local_array[@]}
if [ `expr ${local_array[0]} % ${local_array[1]}` -eq 0 ] && [ `expr ${local_array[0]} % ${local_array[2]}` -eq 0 ]
then
    echo "true"
else
    echo "false"
fi