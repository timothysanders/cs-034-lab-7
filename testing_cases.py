#Name(s): Michael Jung ID:10680322, Timothy Sanders ID:, Megan Yu ID:

import unittest

class TestTicketSystem(unittest.TestCase):

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

    def test_queue_FIFO_behavior(self):
        queue = Queue()
        queue.enqueue("Call from customer A")
        queue.enqueue("Call from customer B")
        queue.enqueue("Call from customer C")

        self.assertEqual(queue.get_size(), 3)
        self.assertEqual(queue.front(), "Call from customer A")

        self.assertEqual(queue.dequeue(), "Call from customer A")
        self.assertEqual(queue.dequeue(), "Call from customer B")
        self.assertEqual(queue.dequeue(), "Call from customer C")
        self.assertTrue(queue.is_empty())


unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTicketSystem))
