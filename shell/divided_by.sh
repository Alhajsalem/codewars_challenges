#!/bin/bash
local_array=("$@")
echo ${local_array[@]}
if [ `expr ${local_array[0]} % ${local_array[1]}` -eq 0 ] && [ `expr ${local_array[0]} % ${local_array[2]}` -eq 0 ]
then
    echo "true"
else
    echo "false"
fi


#!/bin/bash
# input : 2 strings with substrings separated by `,`
# output: number as a string
accum () {
    ARRAY=()
    for i in $(echo $1 | sed "s/,/ /g")
        do
        for ii in $(echo $2 | sed "s/,/ /g")
            do
            x=$(( ${#ii}-${#i} ))
            y=$( sed "s/-//" <<< $x )
            ARRAY+=($y) 
        done
    done
    if [ "${#ARRAY[@]}" -eq 0 ]; then
        echo -1 
    fi
    max=0
    for v in "${ARRAY[@]}"; do
    if (( $v > $max )); then max=$v; fi; 
    done
    echo $max

}



accum () {
    echo `python -c "$aux4657" "$1" "$2"`
}

accum hoqq,bbllkw,oox,ejjuyyy,plmiis,xxxzgpsssa,xxwwkktt,znnnnfqknaz,qqquuhii,dvvvwz cccooommaaqqoxii,gggqaffhhh,tttoowwwmmww