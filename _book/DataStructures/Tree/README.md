https://en.wikipedia.org/wiki/Template:CS_trees

Quoted from https://www.baeldung.com/cs/tree-segment-interval-range-binary-indexed：
1. Segment Tree (ST) is a generic data structure that can be applied to solve range query problems.
2. Binary Index Tree (BIT), or Fenwick Tree, is a scheme to precalculate sums on an array. It allows answering RSQ in $O(log(N))$ time. We don’t usually construct an explicit tree for a BIT. Instead, a BIT can be represented in an array having the same number of elements as the original array.
3. Interval Tree (IT) is a computational geometry data structure. It enables us to quickly find out which intervals contain the given point or which intervals intersect with the given interval.
4. Range Tree (RT) is another computational geometry data structure. It solves the problem opposite to the one solved by IT: given a set of points, count or find all the points that the given interval contains.

Quoted from https://stackoverflow.com/a/64191287:
1. There are things that a segment tree can do but a BIT cannot : A BIT essentially works with cumulative quantities. When the cumulative quantity for interval `[i..j]` is required, it is found as the difference between cumulative quantities for `[1...j]` and `[1...i-1]`. This works only because `addition` has an inverse operation. You cannot do this if the operation is non-invertible (such as `max`). On the other hand, every interval on a segment tree can be found as *union of disjoint intervals* and no inverse operation is required.
2. A BIT requires only half as much *memory* as a segment tree.
3. Though BIT and segment tree operations are both $O(log(n))$, the segment tree operations have a larger *constant factor*.
