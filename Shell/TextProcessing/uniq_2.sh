# https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-2/problem?isFullScreen=true
uniq -c | awk '{$1=$1;print}'