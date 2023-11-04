# https://www.hackerrank.com/challenges/text-processing-cut-7/problem

while read lines;
do
    echo "$lines" | cut -d ' ' -f 4
done