# https://www.hackerrank.com/challenges/determining-dna-health/problem?isFullScreen=false
#
# Input:
#   1. gene_i (string) with health_i (int)
#   2. dna_i (string) with start_i (index), end_i (index)
# Output:
#   DNA with max and min health
#
# Method:
# 1. Multiple string searching: Aho-Corasick algorithm
# 2. Range query: Prefix sum


from bisect import bisect_left, bisect_right
from collections import deque


class Node:
    """Represents a single Node of a Trie, with the following properties:
    1. child: an array of 4 pointers, pointing to the child Node or None.
    2. suffix: a pointer to the suffix Node, i.e.,
    3. dict_suffix: a pointer to the dict suffix Node, i.e.,
    """

    def __init__(self, c):
        self.char = c

        # match
        self.child = {}
        self.parent = None

        # fail
        self.suffix = None

        # customized fields for current problem
        self.indices = None
        self.prefix_sum = None


def build_aho_corasick_automaton(genes, healths):
    head = Node("")
    for index, (gene, health) in enumerate(zip(genes, healths)):
        insert_word(head, gene, health, index)
    insert_suffix_links(head)
    return head


def insert_word(head, gene, health, index):
    cur = head
    for c in gene:
        if c not in cur.child:
            cur.child[c] = Node(c)
            cur.child[c].parent = cur
        cur = cur.child[c]
    if cur.indices == None:
        cur.indices = []
        cur.prefix_sum = [0]
    cur.indices.append(index)
    cur.prefix_sum.append(cur.prefix_sum[-1] + health)


def insert_suffix_links(trie):
    """The suffix link of a node points to the longest suffix in the trie."""
    queue = deque()
    queue.append(trie)

    while len(queue) != 0:
        node = queue.popleft()
        for k in node.child:
            v = node.child[k]
            queue.append(v)
        if node.parent == None:
            continue
        _insert_suffix_link(node)


def _insert_suffix_link(node):
    # If node.char in node.parent.suffix.child,
    #   then node.suffix = node.parent.suffix.child[node.char]
    # Else, check node.parent.suffix.suffix, until head.
    #   If node.char not in head.child, node.suffix = head
    parent = node.parent
    if parent.parent == None:
        node.suffix = parent
        return
    while parent.parent != None:
        if node.char in parent.suffix.child:
            node.suffix = parent.suffix.child[node.char]
            break
        parent = parent.suffix
    else:
        # Now parent is head
        if node.char in parent.child:
            node.suffix = parent.child[node.char]
        else:
            node.suffix = parent


def calculate_dna_health(trie, dna, first, last):
    """Search the DNA on Trie, which was built upon a set of target Genes."""
    ans = 0
    cur_index = 0
    cur_node = trie
    while cur_index < len(dna):
        cur_char = dna[cur_index]
        if cur_char in cur_node.child:
            # match
            cur_index += 1
            cur_node = cur_node.child[cur_char]
            ans += output(cur_node, first, last)
            continue
        else:
            # fail to match
            if cur_node.parent != None:
                cur_node = cur_node.suffix
            else:
                cur_index += 1
    return ans


def compute_range_sum(node, first, last):
    indices = node.indices
    prefix_sum = node.prefix_sum
    return prefix_sum[bisect_right(indices, last)]-prefix_sum[bisect_left(indices, first)]


def output(node, first, last):
    ans = 0
    while node:
        if node.indices != None:
            ans += compute_range_sum(node, first, last)
        node = node.suffix
    return ans


if __name__ == "__main__":
    n = int(input().strip())
    genes = input().rstrip().split()
    healths = list(map(int, input().rstrip().split()))
    s = int(input().strip())

    automaton = build_aho_corasick_automaton(genes, healths)
    healths = []
    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()
        first = int(first_multiple_input[0])
        last = int(first_multiple_input[1])
        d = first_multiple_input[2]

        healths.append(calculate_dna_health(automaton, d, first, last))
    print(min(healths), max(healths))
