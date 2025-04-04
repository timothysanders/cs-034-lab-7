import unittest

class Queue:
    """
    Implement a Queue data structure.

    Parameters
    ----------
    maximum_length : int = -1

    Attributes
    ----------
    queue_list : list
    front_index : int
    length : int
    max_length : int

    Methods
    -------
    is_empty()
        Check if the queue is empty.
    get_size()
        Get the size of the queue.
    enqueue(new_item)
        Add a new item to the queue.
    dequeue()
        Remove and return the item from the queue.
    front()
        Get the front item from the queue.
    resize()
        Resize the queue.
    """
    def __init__(self, maximum_length: int=-1):
        self.queue_list = []  # Start with an empty list
        self.front_index = 0
        self.length = 0
        self.max_length = maximum_length

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns
        -------
        bool
        """
        return self.length == 0

    def get_size(self) -> int:
        """
        Get the size of the queue.

        Returns
        -------
        int
        """
        return self.length

    def enqueue(self, new_item) -> bool:
        """
        Add a new item to the queue.

        Parameters
        ----------
        new_item

        Returns
        -------
        bool
        """
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
        """
        Remove and return the item from the queue.

        Returns
        -------
        to_return
            The item from the front of the queue.

        Raises
        ------
        IndexError
            If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")

        # Get the item at the front of the queue
        to_return = self.queue_list[self.front_index]

        # Decrement length and advance front_index
        self.length -= 1
        self.front_index = (self.front_index + 1) % len(self.queue_list)

        return to_return

    def front(self):
        """
        Get the front item from the queue.

        Returns
        -------

        Raises
        ------
        IndexError
            If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Empty queue")
        return self.queue_list[self.front_index]

    def resize(self) -> None:
        """
        Resize the queue.

        Returns
        -------
        None
        """
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
