/*
   Reverse a doubly linked list, input list may also be empty
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* Reverse(Node* head)
{
    // Complete this function
    // Do not write the main method. 
    if (head == nullptr)
        return head;
    Node * prev = nullptr;
    while (head) {
        Node * next = head->next;
        head->next = prev;
        head->prev = next;
        prev = head;
        head = next;
    }
    return prev;
}
