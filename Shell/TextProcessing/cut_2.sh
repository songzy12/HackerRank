# https://www.hackerrank.com/challenges/text-processing-cut-2/problem
# https://www.folkstalk.com/2012/02/cut-command-in-unix-linux-examples.html

while read lines;
do
    echo $lines | cut -c 2,7
done