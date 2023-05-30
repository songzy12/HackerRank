/*
  Get Nth element from the end in a linked list of integers
  Number of elements in the list will always be greater than N.
  Node is defined as
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
struct result
{
    int data;
    int position;
};
result GetPosition(Node *head, int positionFromTail)
{
    if (head == nullptr)
        return result{-1, 0};
    result temp = GetPosition(head->next, positionFromTail);
    if (temp.position == positionFromTail)
        return result{head->data, temp.position + 1};
    else if (temp.position < positionFromTail)
        return result{-1, temp.position + 1};
    else
        return result{temp.data, temp.position + 1};
}

int GetNode(Node *head, int positionFromTail)
{
    // This is a "method-only" submission.
    // You only need to complete this method.
    return GetPosition(head, positionFromTail).data;
}
