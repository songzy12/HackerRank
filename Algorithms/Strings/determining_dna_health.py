# https://www.hackerrank.com/challenges/determining-dna-health/problem?isFullScreen=false

from collections import defaultdict


class Node:
    """Represents a single Node of a Trie, with the following properties:
    1. child: an array of 4 pointers, pointing to the child Node or None.
    2. suffix: a pointer to the suffix Node, i.e.,
    3. dict_suffix: a pointer to the dict suffix Node, i.e.,
    """

    def __init__(self, c, index):
        self.char = c
        self.index = set()

        # match
        self.child = {}
        self.parent = None

        self.in_dict = False
        self.health = {}

        # fail
        self.suffix = None
        # output
        self.dict_suffix = None

    def is_head(self):
        """Returns whether the current node is the head of trie."""
        return self.parent is None


def build_trie(genes, healths):
    head = Node("", -1)
    index = 0
    for gene, health in zip(genes, healths):
        insert_word(head, gene, health, index)
        index += 1
    insert_suffix_links(head)
    insert_dict_suffix_links(head)
    return head


def insert_word(head, gene, health, index):
    cur = head
    for c in gene:
        if c not in cur.child:
            cur.child[c] = Node(c, -1)
            cur.child[c].parent = cur
        cur = cur.child[c]
    cur.index.add(index)
    cur.health[index] = health
    cur.in_dict = True


def insert_suffix_links(trie):
    """The suffix link of a node points to the longest suffix in the trie."""
    queue = [trie]
    visited = {trie}
    while len(queue) != 0:
        node = queue.pop(0)
        for k in node.child:
            v = node.child[k]
            if v not in visited:
                queue.append(v)
                visited.add(v)
        if node.is_head():
            continue
        _insert_suffix_link(node)


def _insert_suffix_link(node):
    # If node.char in node.parent.suffix.child,
    #   then node.suffix = node.parent.suffix.child[node.char]
    # Else, check node.parent.suffix.suffix, until head.
    #   If node.char not in head.child, node.suffix = head
    parent = node.parent
    if parent.is_head():
        node.suffix = parent
        return
    while not parent.is_head():
        if node.char in parent.suffix.child:
            node.suffix = parent.suffix.child[node.char]
            break
        parent = parent.suffix
    else:
        # Now parrent is head
        if node.char in parent.child:
            node.suffix = parent.child[node.char]
        else:
            node.suffix = parent


def insert_dict_suffix_links(trie):
    queue = [trie]
    visited = {trie}
    while len(queue) != 0:
        node = queue.pop(0)
        for k in node.child:
            v = node.child[k]
            if v not in visited:
                queue.append(v)
                visited.add(v)
        _insert_dict_suffix_link(node)


def _insert_dict_suffix_link(node):
    suffix = node.suffix
    while suffix and not suffix.is_head() and not suffix.in_dict:
        suffix = suffix.suffix
    if suffix and not suffix.is_head():
        node.dict_suffix = suffix


def print_trie(trie):
    queue = [trie]
    visited = {trie}
    while len(queue) != 0:
        node = queue.pop(0)
        for k in node.child:
            v = node.child[k]
            if v not in visited:
                queue.append(v)
                visited.add(v)
        print_node(node)


def print_node(node):
    print(node.index)
    print("child:", " ".join(node.child[c].index for c in node.child))
    print("suffix:", node.suffix.index if node.suffix else None)
    print("dict_suffix:", node.dict_suffix.index if node.dict_suffix else None)
    print()


def search(trie, dna, first, last):
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
            if not cur_node.is_head():
                cur_node = cur_node.suffix
            else:
                cur_index += 1
    return ans


def output(node, first, last):
    ans = 0
    while node:
        for index in node.index:
            if first <= index <= last:
                ans += node.health.get(index, 0)
        node = node.dict_suffix
    return ans


if __name__ == "__main__":
    n = int(input().strip())
    genes = input().rstrip().split()
    healths = list(map(int, input().rstrip().split()))
    s = int(input().strip())

    trie = build_trie(genes, healths)
    healths = []
    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()
        first = int(first_multiple_input[0])
        last = int(first_multiple_input[1])
        d = first_multiple_input[2]

        healths.append(search(trie, d, first, last))
    print(min(healths), max(healths))
