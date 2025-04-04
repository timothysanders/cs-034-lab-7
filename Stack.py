from Node import Node
from LinkedList import LinkedList
import unittest


class Stack:
    """
    Implement a Stack data structure.

    Parameters
    ----------
    none

    Attributes
    ----------
    linked_list : LinkedList
    size : int

    Methods
    -------
    push(new_item)
        Prepends a new node to the stack.
    pop()
        Removes the data that the head node points to.
    peek()
        Returns the head node's data from the stack.
    is_empty()
        Check if the stack is empty.
    get_size()
        Returns the size of the stack.
    """
    def __init__(self):
        self.linked_list = LinkedList()
        self.size = 0

    def push(self, new_item):   # substitute "cancellation_details" for "new_item"
        new_node = Node(new_item)
        self.linked_list.prepend(new_node)
        self.size += 1
        """
        Prepends a new node to the stack.

        Returns
        -------
        None
        """
    def pop(self):
        """
        Removes the data that the head node points to.

        Returns
        -------
        
        """        
        popped_item = self.linked_list.head.data
        self.linked_list.remove_after(None)
        self.size -= 1
        return popped_item

    def peek(self):
        """
        Returns the head node's data from the stack

        Returns
        -------
        None
        """        
        if self.linked_list.head == None:
            raise IndexError("Peek from empty stack")
        return self.linked_list.head.data

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns
        -------
        bool
        """        
        return self.linked_list.head == None

    def get_size(self):
        """
        Returns the size of the stack.

        Returns
        -------
        int
        """        
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
