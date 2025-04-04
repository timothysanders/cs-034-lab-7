#Name(s): Michael Jung ID:10680322, Timothy Sanders ID:, Megan Yu ID:

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
