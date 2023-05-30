/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node *Reverse(Node *head)
{
  // Complete this method
  if (head == nullptr)
    return head;
  Node *pre = nullptr;
  while (head->next)
  {
    Node *post = head->next;
    head->next = pre;
    pre = head;
    head = post;
  }
  head->next = pre;
  return head;
}
