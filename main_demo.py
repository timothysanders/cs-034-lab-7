import Stack
import QueueArray



if __name__ == "__main__":
  print("\\n========== STACK DEMONSTRATION (LIFO: Ticket Cancellations) ==========")
  cancellation_stack = Stack()
  cancellations = ["Ticket-101", "Ticket-250", "Ticket-399"]

  for ticket in cancellations:
    print(f"[Action] Customer canceled ticket: {ticket}")
    cancellation_stack.push(ticket)

  print("\\n[Now processing returned tickets in LIFO order...]")
  while not cancellation_stack.is_empty():
    returned_ticket = cancellation_stack.pop()
    print(f"[Processed] Refunded ticket: {returned_ticket}")

  print("\\n========== QUEUE DEMONSTRATION (FIFO: Hotline Requests) ==========")
  customer_queue = Queue()
  customers = ["Michael", "Tim", "Megan"]

  for name in customers:
    print(f"[Call] {name} wants to purchase a ticket.")
    customer_queue.enqueue(name)

  print("\\n[Now processing customer calls in FIFO order...]")
  while not customer_queue.is_empty():
    customer = customer_queue.dequeue()
    print(f"[Processed] Assigned ticket to {customer}")
