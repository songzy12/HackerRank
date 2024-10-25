# https://www.hackerrank.com/challenges/determining-dna-health/problem?isFullScreen=false

from collections import defaultdict


class Node:
    """Represents a single Node of a Trie, with the following properties:
    1. child: an array of 4 pointers, pointing to the child Node or None.
    2. suffix: a pointer to the suffix Node, i.e.,
    3. dict_suffix: a pointer to the dict suffix Node, i.e.,
    """

    # class memeber shared by all instances.
    node_index = defaultdict(int)

    def __init__(self, c):
        self.char = c
        self.label = str(Node.node_index[self.char])
        Node.node_index[self.char] += 1

        # match
        self.child = {}
        self.parent = None

        self.in_dict = False
        self.health = 0

        # fail
        self.suffix = None
        # output
        self.dict_suffix = None

    def is_head(self):
        """Returns whether the current node is the head of trie."""
        return self.parent is None

    def get_label(self):
        return self.char + self.label


def build_trie(genes, healths):
    head = Node("")
    for gene, health in zip(genes, healths):
        insert_word(head, gene, health)
    insert_suffix_links(head)
    insert_dict_suffix_links(head)
    return head


def insert_word(head, gene, health):
    cur = head
    for c in gene:
        if c not in cur.child:
            cur.child[c] = Node(c)
            cur.child[c].parent = cur
        cur = cur.child[c]
    cur.health += health
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
    print(node.get_label())
    print("child:", " ".join(node.child[c].get_label() for c in node.child))
    print("suffix:", node.suffix.get_label() if node.suffix else None)
    print("dict_suffix:", node.dict_suffix.get_label() if node.dict_suffix else None)
    print()


def search(trie, dna):
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
            ans += output(cur_node)
            continue
        else:
            # fail to match
            if not cur_node.is_head():
                cur_node = cur_node.suffix
            else:
                cur_index += 1
    return ans


def output(node):
    ans = 0
    while node:
        ans += node.health
        node = node.dict_suffix
    return ans


def compute_dna_health(dna, genes, healths):
    # print(dna)
    trie = build_trie(genes, healths)
    # print_trie(trie)
    return search(trie, dna)


if __name__ == "__main__":
    n = int(input().strip())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    s = int(input().strip())

    healths = []
    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()
        first = int(first_multiple_input[0])
        last = int(first_multiple_input[1])
        d = first_multiple_input[2]

        healths.append(
            compute_dna_health(d, genes[first : last + 1], health[first : last + 1])
        )
    print(min(healths), max(healths))
