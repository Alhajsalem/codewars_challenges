#https://www.codewars.com/kata/53ee5429ba190077850011d4/train/shell
num1=$1
ans=$((num1 * 2))
echo $ans

#############
#!/bin/bash
greet() {
    echo "hello world!";
}
greet 

##############
n=$1
start=$((n*(n-1)+1))
end=$((start+2*n-1))
sum=0
for ((i=start;i<=end;i=i+2)); do
    sum=$((sum+i))
done
echo $sum


#!/bin/bash

countToTwenty() {
 for ((i=1;i<=20;i=i+1)); do
    echo Count: $i
done
}

countToTwenty

echo "Count: "{1..20}