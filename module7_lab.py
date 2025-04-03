#Name(s): Michael Jung ID:10680322, Timothy Sanders ID:, Megan Yu ID:

#linked list based stack
StackPush(stack, item) {
   newNode = Allocate new linked list node
   newNode⇢next = null
   newNode⇢data = item

   // Insert as list head (top of stack)
   ListPrepend(stack, newNode)
}

StackPop(stack) {
   headData = stack⇢head⇢data
   ListRemoveAfter(stack, null)
   return headData
}

push(cancellation_details)
pop()
peek()
is_empty()
get_size()

#array based queue


def enqueue(self, item):
    if self.length == self.max_length:
        return False
  
    if self.length == len(self.queue_list):
        self.resize()
  
    item_index = (self.front_index + self.length) % len(self.queue_list)
    self.queue_list[item_index] = item
    self.length += 1
    return True

def dequeue(self):
    to_return = self.queue_list[self.front_index]
    self.length -= 1
    self.front_index = (self.front_index + 1) % len(self.queue_list)
    return to_return

def resize(self):
    new_size = len(self.queue_list) * 2
    if self.max_length >= 0 and new_size > self.max_length:
        new_size = max_length
    
    new_list = [0] * new_size
    for i in range(self.length):
        item_index = (self.front_index + i) % len(self.queue_list)
        new_list[i] = self.queue_list[item_index]


    self.queue_list = new_list
    self.front_index = 0
