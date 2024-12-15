# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists
#
# Suppose the length of the two lists are a+c and b+c, and w.o.l.g. let a < b
# Stage 1:
#   We iterate through the lists with two pointers p1 and p2
#   When p1 reaches the tail of l1, p2 would be (b-a) far from tail of l2
# Stage 2:
#   Use a new p1 starting from head of l1, and iterate together with p2
#   When p2 reaches the tail of p2, p1 would be (b-a) far from head of l1
# Stage 3:
#   Use a new p2 starting from head of l2, and iterate together with p1
#   Then when p1 and p2 meets for the first time, that would be the intersection node

import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)


def findMergeNode(head1, head2):
    p1 = head1
    p2 = head2
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
        if not p1:
            p1 = head2
        if not p2:
            p2 = head1
    return p1.data


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    tests = int(input())
    for tests_itr in range(tests):
        index = int(input())
        llist1_count = int(input())
        llist1 = SinglyLinkedList()
        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())
        llist2 = SinglyLinkedList()
        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
        for i in range(llist2_count):
            if i != llist2_count - 1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + "\n")

    fptr.close()
