# https://www.hackerrank.com/challenges/text-processing-cut-8/problem

while read lines;
do
    echo "$lines" | cut -d ' ' -f -3
done