Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?<br/>
   O(1), because the list method append has constant runtime complexity.<br/><br/>

2. What is the runtime complexity of `dequeue`?<br/>
   O(1), because the list method pop has constant runtime complexity.<br/><br/>

3. What is the runtime complexity of `len`?<br/>
   O(1), because the list method len has constant runtime complexity.<br/><br/>

## Binary Search Tree

1. What is the runtime complexity of `insert`?<br/>
   O(log n) because the size of the subtree to traverse to find the right insertion point is cut in half at each step.<br/><br/>

2. What is the runtime complexity of `contains`?<br/>
   O(log n) because the size of the subtree to search is cut in half at each step.<br/><br/>

3. What is the runtime complexity of `get_max`?<br/>
   O(log n) because the size of the subtree to search is cut in half at each step.<br/><br/>

## Heap

1. What is the runtime complexity of `_bubble_up`?<br/>
   It should be O(log n) because it treats the array storage as a binary tree, meaning that the size of the array to search for the appropriate spot gets cut in half at each step. <br/><br/>

2. What is the runtime complexity of `_sift_down`?<br/>
   It should be O(log n) because it treats the array storage as a binary tree, meaning that the size of the array to search for the appropriate spot gets cut in half at each step. <br/><br/>

3. What is the runtime complexity of `insert`?<br/>
   The insertion operation itself runs in constant time, but bubbling up takes O(log n), so the whole function takes that much time.<br/><br/>

4. What is the runtime complexity of `delete`?<br/>
   The deletion operation itself runs in constant time, but sifting down takes O(log n), so the whole function takes that much time.<br/><br/>

5. What is the runtime complexity of `get_max`?<br/>
   O(1), because lists have constant time complexity for accession of a known index.<br/><br/>

## Doubly Linked List

1.  What is the runtime complexity of `ListNode.insert_after`?<br/>
    <br/><br/>

2.  What is the runtime complexity of `ListNode.insert_before`?<br/>
    <br/><br/>

3.  What is the runtime complexity of `ListNode.delete`?<br/>
    <br/><br/>

4.  What is the runtime complexity of `DoublyLinkedList.add_to_head`?<br/>
    <br/><br/>

5.  What is the runtime complexity of `DoublyLinkedList.remove_from_head`?<br/>
    <br/><br/>

6.  What is the runtime complexity of `DoublyLinkedList.add_to_tail`?<br/>
    <br/><br/>

7.  What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?<br/>
    <br/><br/>

8.  What is the runtime complexity of `DoublyLinkedList.move_to_front`?<br/>
    <br/><br/>

9.  What is the runtime complexity of `DoublyLinkedList.move_to_end`?<br/>
    <br/><br/>

10. What is the runtime complexity of `DoublyLinkedList.delete`?<br/>
    <br/><br/>

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better? <br/>
