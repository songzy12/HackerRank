# https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-3/problem?isFullScreen=true
uniq -ci | awk '{$1=$1;print}'