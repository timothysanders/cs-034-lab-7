from Node import Node
from LinkedList import LinkedList

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


'''

from Node import Node
from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)
        
        # Insert the node as the list head (top of stack)
        self.list.prepend(new_node)
    
    def pop(self):
        # Copy data from list's head node (stack's top node)
        popped_item = self.list.head.data
        
        # Remove list head
        self.list.remove_after(None)
        
        # Return the popped item
        return popped_item

    def push(self, cancellation_details):
        pass

'''

    def peek(self):
        pass

    def is_empty(self):
        pass

    def get_size(self):
        pass
