#!/bin/bash
time=$1
# The fun begins here.


if (( $(echo "$time*0.5 < 1" |bc -l) )); then
   echo "0"

else
    t=$(echo $time*0.5 | bc)
    int=${t%.*}
    echo $int
fi

#!/bin/bash
time=$1
# The fun begins here.
echo "$1/2" | bc


#!/bin/bash
python -c "import math; print(math.floor($1 * 0.5))"

python -c "for i in range($1): print(i)"