# https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/problem?isFullScreen=true
read x
if [[ $x = "Y" || $x = "y" ]]; then
    echo "YES"
elif [[ $x = "N" || $x = "n" ]]; then
    echo "NO"
else
    echo "$x"
fi
