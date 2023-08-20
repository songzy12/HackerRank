# https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations/problem
read exp
res=$(echo $exp | bc -l)
printf "%.3f" "$res"
