import unittest

class Queue:
    def __init__(self, maximum_length=-1):
        self.queue_list = []  # Start with an empty list
        self.front_index = 0
        self.length = 0
        self.max_length = maximum_length

    def is_empty(self):
        return self.length == 0

    def get_size(self):
        return self.length

    def enqueue(self, new_item):    # "new_item" can be substituted by "call_details" in the actual implementation
        # If at max length, return False
        if self.max_length >= 0 and self.length == self.max_length:
            return False

        # Resize if length equals allocation size
        if self.length == len(self.queue_list):
            self.resize()

        # Enqueue the item
        item_index = (self.front_index + self.length) % len(self.queue_list)
        self.queue_list[item_index] = new_item
        self.length += 1
        return True

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        # Get the item at the front of the queue
        to_return = self.queue_list[self.front_index]

        # Decrement length and advance front_index
        self.length -= 1
        self.front_index = (self.front_index + 1) % len(self.queue_list)

        return to_return

    def front(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        return self.queue_list[self.front_index]

    def resize(self):
        # Create new list and copy existing items
        new_size = len(self.queue_list) * 2 if len(self.queue_list) > 0 else 1
        if self.max_length >= 0 and new_size > self.max_length:
            new_size = self.max_length
        
        new_list = [0] * new_size

        for i in range(self.length):
            old_index = (self.front_index + i) % len(self.queue_list)
            new_list[i] = self.queue_list[old_index]

        # Assign new list and reset front_index to 0
        self.queue_list = new_list
        self.front_index = 0


class TestQueue(unittest.TestCase):

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

# Test the general functionality of array-based Queue
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestQueue))
