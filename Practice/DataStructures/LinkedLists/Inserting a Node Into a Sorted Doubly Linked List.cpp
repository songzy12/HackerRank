/*
    Insert Node in a doubly sorted linked list 
    After each insertion, the list should be sorted
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* SortedInsert(Node *head,int data)
{
    // Complete this function
   // Do not write the main method. 
    Node *prev = nullptr;
    Node *cur = head;
    while (cur && data > cur->data) {
        prev = cur;
        cur = cur->next;
    }
    Node *temp = new Node{data, cur, prev};
    if (prev != nullptr) 
        prev->next = temp;
    if (cur != nullptr)
        cur->prev = temp;
    if (prev != nullptr)
        return head;
    else
        return temp;
}
