# https://www.hackerrank.com/challenges/text-processing-cut-9/problem


while read lines;
do
    echo "$lines" | cut -f 2-
done