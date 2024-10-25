https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm

# Aho–Corasick algorithm

Informally, the algorithm constructs a finite-state machine that resembles a trie with additional links between the various internal nodes. These extra internal links allow fast transitions between failed string matches (e.g. a search for cart in a trie that does not contain cart, but contains art, and thus would fail at the node prefixed by car), to other branches of the trie that share a common suffix (e.g., in the previous case, a branch for attribute might be the best lateral transition). This allows the automaton to transition between string matches without the need for backtracking.

## Example

Dictionary: {a, ab, bab, bc, bca, c, caa}.

![image](https://upload.wikimedia.org/wikipedia/commons/6/62/Ahocorasick.svg)

### Node

The data structure has one node for every prefix of every string in the dictionary. So if (bca) is in the dictionary, then there will be nodes for (bca), (bc), (b), and (). 

If a node is in the dictionary then it is a *blue* node. Otherwise it is a *grey* node.

### Child Edge

There is a *black* directed "child" arc from each node to a node whose name is found by appending one character. So there is a black arc from (bc) to (bca).

### Suffix Edge

There is a *blue* directed "suffix" arc from each node to the node that is the longest possible strict suffix of it in the graph. For example, for node (caa), its strict suffixes are (aa) and (a) and (). The longest of these that exists in the graph is (a). So there is a blue arc from (caa) to (a). 

The blue arcs can be computed in linear time by performing a breadth-first search [potential suffix node will always be at lower level] starting from the root. The target for the blue arc of a visited node can be found by following its parent's blue arc to its longest suffix node and searching for a child of the suffix node whose character matches that of the visited node. If the character does not exist as a child, we can find the next longest suffix (following the blue arc again) and then search for the character. We can do this until we either find the character (as child of a node) or we reach the root (which will always be a suffix of every string).

### Dictionary Suffix Edge

There is a *green* "dictionary suffix" arc from each node to the next node in the dictionary that can be reached by following blue arcs. For example, there is a green arc from (bca) to (a) because (a) is the first node in the dictionary (i.e. a blue node) that is reached when following the blue arcs to (ca) and then on to (a). 

The green arcs can be computed in linear time by repeatedly traversing blue arcs until a blue node is found, and memoizing this information. At each step, the current node is extended by finding its child, and if that doesn't exist, finding its suffix's child, and if that doesn't work, finding its suffix's suffix's child, and so on, finally ending in the root node if nothing's seen before.

### Output

When the algorithm reaches a node, it *outputs* all the dictionary entries that end at the current character position in the input text. This is done by printing every node reached by following the dictionary suffix links, starting from that node, and continuing until it reaches a node with no dictionary suffix link. In addition, the node itself is printed, if it is a dictionary entry.

## Reference

Original paper: https://dl.acm.org/doi/pdf/10.1145/360825.360855
> Aho, A. V., & Corasick, M. J. (1975). Efficient string matching: an aid to bibliographic search. Communications of the ACM, 18(6), 333-340.

## Practice

https://www.hackerrank.com/challenges/determining-dna-health/problem
