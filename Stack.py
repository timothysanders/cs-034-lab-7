from Node import Node
from LinkedList import LinkedList
import unittest


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()
        self.size = 0

    def push(self, new_item):   # substitute "cancellation_details" for "new_item"
        new_node = Node(new_item)
        self.linked_list.prepend(new_node)
        self.size += 1

    def pop(self):
        popped_item = self.linked_list.head.data
        self.linked_list.remove_after(None)
        self.size -= 1
        return popped_item

    def peek(self):
        if self.linked_list.head == None:
            raise IndexError("Peek from empty stack")
        return self.linked_list.head.data

    def is_empty(self):
        return self.linked_list.head == None

    def get_size(self):
        return self.size


class TestLinkedListStack(unittest.TestCase):

    def test_stack_LIFO_behavior(self):
        stack = Stack()
        stack.push("Cancel ticket #101")
        stack.push("Cancel ticket #102")
        stack.push("Cancel ticket #103")

        self.assertEqual(stack.get_size(), 3)
        self.assertEqual(stack.peek(), "Cancel ticket #103")

        self.assertEqual(stack.pop(), "Cancel ticket #103")
        self.assertEqual(stack.pop(), "Cancel ticket #102")
        self.assertEqual(stack.pop(), "Cancel ticket #101")
        self.assertTrue(stack.is_empty())

# Test the functionality of Stack
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestLinkedListStack))
