#Name(s): Michael Jung ID:10680322, Timothy Sanders ID:, Yu Yu Ng ID:
import unittest


class Node:
   def __init__(self, initial_data):
      self.data = initial_data
      self.next = None


class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def append(self, new_node):
      if self.head is None:
         self.head = new_node
         self.tail = new_node
      else:
         self.tail.next = new_node
         self.tail = new_node

   def prepend(self, new_node):
      if self.head is None:
         self.head = new_node
         self.tail = new_node
      else:
         new_node.next = self.head
         self.head = new_node

   def insert_after(self, current_node, new_node):
      if self.head is None:
         self.head = new_node
         self.tail = new_node
      elif current_node is self.tail:
         self.tail.next = new_node
         self.tail = new_node
      else:
         new_node.next = current_node.next
         current_node.next = new_node
   
   def remove_after(self, current_node):
     # Special case, remove head
     if (current_node is None) and (self.head is not None):
        succeeding_node = self.head.next
        self.head = succeeding_node  
        if succeeding_node is None:    # Removed last item
           self.tail = None
     elif current_node.next is not None:
        succeeding_node = current_node.next.next
        current_node.next = succeeding_node
        if succeeding_node is None:    # Removed tail
           self.tail = current_node


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
