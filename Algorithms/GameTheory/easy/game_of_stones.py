# https://www.hackerrank.com/challenges/game-of-stones-1/problem
#
# The idea is that
# 1. for a condition to be a winning position, there is at least one move to a losing position
# 2. for a condition to be a losing position, all moves lead to winning positions
# We can stop here now and write some recursion code as the solution for the current problem.
# 
# A more mathematically way is to do some calculation on paper and see the pattern:
#
# Trivial cases:
#   n=0,1 -> L, since we cannot make a move
#   n=2,3,5 -> W, since we can remove all stones to leave n=0 (L)
#
# For n=4, we enumerate the possible moves and find that removing 3 leads to n=1 (L), so n=4 is W.
# For n=6, removing 5 leads to n=1 (L), so n=6 is W.
# Now we have the base cases: [L, L, W, W, W, W, W].
#                             [0, 1, 2, 3, 4, 5, 6].

# For n=7, removing 2,3,5 falls into the interval [2, 5], which are all W, so n=7 is L.
# For n=8, removing 2,3,5 falls into the interval [3, 6], which are all W, so n=8 is L.
# Then since n=7 is L, so n=9,10,12 are W.
# since n=8 is L, so n=10,11,13 are W.
# The pattern repeated: [L, L, W,  W,  W,  W,  W]...
#                       [7, 8, 9, 10, 11, 12, 13]...

# Therefore, we can conclude that if n % 7 in [0, 1], then it's a losing position, otherwise it's winning.


import os


def gameOfStones(n):
    if n % 7 == 0 or n % 7 == 1:
        return "Second"
    return "First"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
