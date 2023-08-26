read N
sum=0
for i in $(eval echo "{1..$N}"); do
    read x
    sum=$(expr $sum + $x)
done

res=$(echo "$sum/$N" | bc -l)
printf "%.3f" "$res"
