# https://www.hackerrank.com/challenges/text-processing-cut-3/problem

while read lines;
do
    echo $lines | cut -c 2-7
done