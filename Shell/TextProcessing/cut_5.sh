# https://www.hackerrank.com/challenges/text-processing-cut-5/problem
# https://unix.stackexchange.com/questions/35369/how-to-define-tab-delimiter-with-cut-in-bash

while read lines;
do
    echo "$lines" | cut -f -3
done
