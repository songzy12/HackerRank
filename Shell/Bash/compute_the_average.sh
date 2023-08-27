read N
sum=0

for i in $(seq 1 $N); do
    read x
    sum=$(($sum + $x))
done

res=$(echo "$sum/$N" | bc -l)
printf "%.3f" "$res"
