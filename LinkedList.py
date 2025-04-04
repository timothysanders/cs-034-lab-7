import Node

class LinkedList:
    """
    Implements a linked list data structure.

    Attributes
    ----------
    head : Node
    tail : Node

    Methods
    -------
    append(new_node)
        Add a new node to the end of the linked list.
    prepend(new_node)
        Add a new node to the beginning of the linked list.
    insert_after(current_node, new_node)
        Insert a new node after the specified node.
    remove_after(current_node)
        Remove the node after the specified node.
    """
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def append(self, new_node: Node) -> None:
        """
        Add a new node to the end of the linked list.

        Parameters
        ----------
        new_node : Node
            The node to add to the end of the linked list.

        Returns
        -------
        None
        """
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node: Node) -> None:
        """
        Add a new node to the beginning of the linked list.

        Parameters
        ----------
        new_node : Node
            The node to be added to the beginning of the linked list.

        Returns
        -------
        None
        """
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node: Node, new_node: Node) -> None:
        """
        Insert a new node after the specified node.

        If the list is empty, the new node becomes both the head and tail.

        Parameters
        ----------
        current_node : Node
            The anchor node after which the new node will be inserted.
        new_node : Node
            The new node to be inserted.

        Returns
        -------
        None
        """
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_after(self, current_node: Node) -> None:
        """
        Remove the node after the specified node.

        Note that passing None as current_node results in removing the head.

        Parameters
        ----------
        current_node : Node
            Node before the node to remove.

        Returns
        -------
        None
        """
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

