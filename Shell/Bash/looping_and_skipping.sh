# https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping/problem?isFullScreen=true
for i in {1..100}; do
    if (($i % 2 == 1)); then
        echo "$i"
    fi
done
