"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
        return self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
        return self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:

    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        # if no items in DLL, set new node to be both head and tail
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        # if 1+ items in DLL, insert node before current head and update
        else:
            new_node = self.head.insert_before(value)
            new_node.next = self.head
            self.head = new_node

    def remove_from_head(self):
        # if there's no head, return None
        if not self.head:
            return None
        # if there's 1 item in the DLL, set head & tail to none, return old
        if not self.head.next:
            head = self.head
            self.head = None
            self.tail = None
            return head.value
        else:
            head = self.head
            self.head = self.head.next
            return head.value

    def add_to_tail(self, value):
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = self.tail.insert_after(value)
            self.tail = new_node

    def remove_from_tail(self):
        # if there's no tail, return None
        if not self.head:
            return None
        # if there's 1 item in the DLL, set head & tail to none, return old
        if not self.head.next:
            tail = self.tail
            self.head = None
            self.tail = None
            return tail.value
        else:
            tail = self.tail
            self.tail = self.tail.prev
            return tail.value

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        node.delete()

    def get_max(self):
        currentNode = self.head
        maxValue = currentNode.value
        while currentNode:
            if currentNode.value > maxValue:
                maxValue = currentNode.value
            else:
                currentNode = currentNode.next
        return maxValue


DLL = DoublyLinkedList()
print(DLL.head)
DLL.add_to_head(10)
DLL.add_to_head(20)
DLL.add_to_tail(30)

currentNode = DLL.head
while currentNode:
    print(currentNode.value)
    currentNode = currentNode.next
