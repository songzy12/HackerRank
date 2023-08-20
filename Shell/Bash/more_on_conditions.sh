# https://www.hackerrank.com/challenges/bash-tutorials---more-on-conditionals/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
read x
read y
read z
if [[ $x = $y && $y = $z ]]; then
    echo "EQUILATERAL"
elif [[ $x = $y || $x = $z || $y = $z ]]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
