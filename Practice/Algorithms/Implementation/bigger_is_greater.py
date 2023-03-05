# iterate from back to front
# find the first position that there is a decreasing
# keep head unchanged
# then put the next larger char here
# sort all the others to the tail


def compute(s):

    def get_i(s):
        for i in range(len(s) - 1, 0, -1):
            if ord(s[i - 1]) < ord(s[i]):
                return i - 1
        return -1

    i = get_i(s)
    if i == -1:
        return 'no answer'

    def get_p(s):
        j = len(s) - 1
        while ord(s[j]) <= ord(s[0]):
            j -= 1

        return s[j], ''.join(sorted(s[:j] + s[j + 1:]))

    p, back = get_p(s[i:])
    return s[:i] + p + back


n = int(raw_input())
for t in range(n):
    s = raw_input()
    print compute(s)
