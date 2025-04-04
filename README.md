# CS-034: Lab 7

## Lab Objectives
- Understand and implement Stack and Queue operations.
- Demonstrate proficiency with linked list and array-based data structure implementations.
- Develop clear and efficient code practices for handling data structures.

## Lab Instructions
### Project Scenario
Your team (2-3 students) has been hired by a ticketing service company that manages ticket sales for events. Your project will involve two distinct scenarios:
#### Part A: Stack Scenario (Ticket Cancellation Management)
- Customers often cancel tickets shortly before the event, and the company needs an efficient way to handle cancellations.
- Implement a Stack using a linked list to manage ticket cancellations where the most recent cancellations are addressed first.
- Clearly document your node structure and operations.
- Include the following methods: push(cancellation_details), pop(), peek(), is_empty(), and get_size().
- Demonstrate the stack functionality through example cancellations, showing clear output that accurately reflects the Last-In-First-Out (LIFO) processing.
#### Part B: Queue Scenario (Customer Service Call Handling)
- The ticketing company operates a customer service hotline to address queries. They require a system to manage incoming calls effectively, ensuring customers are attended in the order their calls are received.
- Implement a Queue using an array-based approach to manage customer calls.
- Clearly define and document array resizing if applicable.
- Include the following methods: enqueue(call_details), dequeue(), front(), is_empty(), and get_size().
- Demonstrate the queue functionality with example customer service calls, clearly showing the First-In-First-Out (FIFO) processing.

### Project Details
- Your implementation must clearly demonstrate proper handling of edge cases, such as operations on empty structures, dynamic resizing of arrays for queues, and robust error handling. Your program should include well-commented code, clear and informative print statements, and comprehensive example usage to showcase functionality.

## Deliverables
- Submit a Python file (module7_lab.py) containing:
  - Stack class with all required methods implemented.
  - Queue class with all required methods implemented.
  - Example usage demonstrating all class methods clearly and thoroughly in the provided project scenarios.
  - Documentation within the file clearly explaining your data structures, methods, and any design choices made.

## Running The Code
- To run the code, please follow the steps that are shown below
1. After cloning the repository, create a virtual environment and activate it
    ```shell
    python -m venv .venv
    
    source .venv/bin/activate
    ```
2. To run the test cases in `testing_cases.py`, run the following
    ```shell
    python -m unittest testing_cases.py
    ```
3. To run the main demo, which shows the Customer Service and Ticket Cancellation scenarios, run the following
    ```shell
    python main_demo.py
    ```
    - This will return something similar to the following
    ```text
    ========== STACK DEMONSTRATION (LIFO: Ticket Cancellations) ==========
    [Action] Customer canceled ticket: Ticket-101
    [Action] Customer canceled ticket: Ticket-250
    [Action] Customer canceled ticket: Ticket-399
    
    [Now processing returned tickets in LIFO order...]
    [Processed] Refunded ticket: Ticket-399
    [Processed] Refunded ticket: Ticket-250
    [Processed] Refunded ticket: Ticket-101
    
    ========== QUEUE DEMONSTRATION (FIFO: Hotline Requests) ==========
    [Call] Michael wants to purchase a ticket.
    [Call] Tim wants to purchase a ticket.
    [Call] Megan wants to purchase a ticket.
    
    [Now processing customer calls in FIFO order...]
    [Processed] Assigned ticket to Michael
    [Processed] Assigned ticket to Tim
    [Processed] Assigned ticket to Megan
    ```
4. Unit tests may be run on each module file as follows
    ```shell
    python ArrayQueue.py
    python Stack.py
    ```