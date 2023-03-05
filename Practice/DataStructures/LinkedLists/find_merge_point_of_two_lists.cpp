/*
   Find merge point of two linked lists
   Node is defined as
   struct Node
   {
       int data;
       Node* next;
   }
*/
int FindMergeNode(Node *headA, Node *headB)
{
    // Complete this function
    // Do not write the main method.

    // Assume a+c and b+c, and a<b
    // then when l1 reach tail, l2 is (b-a) from tail
    // start from b, then when l2 reach tail, l2' is (b-a) from head
    // then they will meet
    Node *curB = headB, *curA = headA;
    while (curA != curB)
    {
        curA = curA->next;
        curB = curB->next;
        if (!curA)
            curA = headB;
        if (!curB)
            curB = headA;
    }
    return curA->data;
}
