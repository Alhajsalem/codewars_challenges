n=$1
sum=0
for i in $( eval echo {0..$n} )
do
       sum=$((sum + i))
done
echo $sum