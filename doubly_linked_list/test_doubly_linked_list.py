import unittest
from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList


class DoublyLinkedListTests(unittest.TestCase):
    def setUp(self):
        self.node = ListNode(1)
        self.dll = DoublyLinkedList(self.node)

    def test_list_remove_from_tail(self):
        self.dll.add_to_tail(33)
        self.assertEqual(self.dll.remove_from_tail(), 33)

        self.dll.add_to_tail(68)
        self.assertEqual(self.dll.remove_from_tail(), 68)

    def test_list_remove_from_head(self):
        self.dll.add_to_head(2)
        self.assertEqual(self.dll.remove_from_head(), 2)

        self.dll.add_to_head(55)
        self.assertEqual(self.dll.remove_from_head(), 55)

    def test_list_add_to_tail(self):
        self.dll.add_to_tail(30)
        self.assertEqual(self.dll.tail.value, 30)

        self.dll.add_to_tail(20)
        self.assertEqual(self.dll.tail.value, 20)

    def test_node_delete(self):
        self.dll.delete(self.node)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

        self.dll.add_to_tail(1)
        self.dll.add_to_head(9)
        self.dll.add_to_tail(6)

        self.dll.delete(self.dll.head)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 6)

        self.dll.delete(self.dll.head)
        self.assertEqual(self.dll.head.value, 6)
        self.assertEqual(self.dll.tail.value, 6)

    def test_node_insert_before(self):
        self.node.insert_before(0)
        self.assertEqual(self.node.prev.value, 0)

    def test_list_add_to_head(self):
        self.assertEqual(self.dll.head.value, 1)
        self.dll.add_to_head(10)
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.head.next.value, 1)

    def test_node_insert_after(self):
        self.node.insert_after(2)
        self.assertEqual(self.node.next.value, 2)

    def test_list_move_to_end(self):
        self.dll.add_to_head(40)
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(self.dll.head.value, 40)

        self.dll.move_to_end(self.dll.head)
        self.assertEqual(self.dll.tail.value, 40)
        self.assertEqual(self.dll.tail.prev.value, 1)

    def test_list_move_to_front(self):
        self.dll.add_to_tail(3)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 3)

        self.dll.move_to_front(self.dll.tail)
        self.assertEqual(self.dll.head.value, 3)
        self.assertEqual(self.dll.head.next.value, 1)

    def test_get_max(self):
        self.assertEqual(self.dll.get_max(), 1)
        self.dll.add_to_tail(100)
        self.assertEqual(self.dll.get_max(), 100)
        self.dll.add_to_tail(55)
        self.assertEqual(self.dll.get_max(), 100)
        self.dll.add_to_tail(101)
        self.assertEqual(self.dll.get_max(), 101)


if __name__ == '__main__':
    unittest.main()
