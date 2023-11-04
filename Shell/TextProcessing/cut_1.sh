# https://www.hackerrank.com/challenges/text-processing-cut-1/problem

while read lines;
do
    echo "$lines" | cut -c 3
done