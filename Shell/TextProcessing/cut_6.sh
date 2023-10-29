# https://www.hackerrank.com/challenges/text-processing-cut-6/problem

while read lines;
do
    echo "$lines" | cut -c 13-
done