"""datastruct.py

# Data Structures

This module defines the LinkedList abstract data type
"""
############################### 72 chars ###############################


class Node:
    """Represents a node in a linkedlist.

    Arguments
        - data
          The data encapsulated in the node.

    Attributes
        - next: Node | None
          The next node in the linkedlist, or None if the node is the tail.

    Methods
        - get() -> data
          Return the data stored in the node.
    """

    def __init__(self, data: tuple[int, int]):
        self._data = data
        self.next = None

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self) -> tuple[int, int]:
        """Return the data stored in the node.

        Arguments
            None

        Return
            tuple[int, int]
        """
        return self._data


class LinkedList:
    """Represents a sequence of data items.

    Arguments
        None

    Attributes
        None

    Methods
        - length() -> int
        - get(index) -> item
        - insert(index, item) -> None
        - append(item) -> None
        - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
            None

        Return
            length of linkedlist as an integer (zero or positive)
        """
        count = 0
        current = self._head
        while current is not None:
            current = current.next
            count += 1
        return count

    def get(self, n: int) -> tuple[int, int]:
        """Returns item at n-th node.

        Arguments
            - n: int
              sequence number of item to be retrieved (zero-indexed).

        Returns
            item

        Raises
            IndexError if n >= length
        """
        #Ensure index is 0 or positive
        if n < 0:
            raise IndexError("n must be 0 or positive.")
        if self._head is None:
            raise IndexError("linkedlist is empty.")
        else:
            current = self._head
            # Attempt to reach the Nth Node
            while (
                n > 0 #Nth node reached
                and current is not None
            ):
                current = current.next
                n -= 1
            
            #If passed the tail, raise IndexErrorL
            if current is None:
                raise IndexError("n >= length")
            #If nth node is reached, return item
            else:
                return current.get()
            
            
    def insert(self, n: int, item: tuple[int, int]) -> None:
        """Insert item into linkedlist at position n.

        If n == 0, inserts item at the head.
        If n == length, appends item at the tail of the linkedlist.

        Arguments
            - n: int
              sequence number of item to be inserted.

        Raises
            IndexError if n > length
        """
        if n > self.length():      #check whether index is invalid
            raise IndexError("Index out of range")

        # create a new node containing the item
        new_node = Node(item)

        # inserting at the head (front of linked list)
        if n == 0:
            new_node.next = self._head  # new node points to current head
            self._head = new_node       # move head to new node
            return

        # start from the head node
        current = self._head

        # move to the node before position n
        for i in range(n - 1):
            current = current.next

        # connect new node to the next node
        new_node.next = current.next

        # connect previous node to new node
        current.next = new_node
    

    def append(self, item: tuple[int, int]) -> None:
        """Append item at the end of linkedlist.

        Arguments
            - item
              The item to be appended.

        Returns
            None
        else:
        linked list is empty at the start, hence first time run is None and appends an item,
        then list no longer empty so not none, so 'else' function runs which then appends another item
        """
        if self._head is None:    #self._head first node of the linked list
            self._head = Node(item)  # appending
        else:
            # get last node
            current = self._head #current is not None, current.next is none
            while current.next is not None:  #Last node is None, hence While loop will stop at last node
                current = current.next   #append more
            current.next = Node(item)   #appending

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
            - n: int
              sequence number of item to be retrieved (zero-indexed).

        Raises
            IndexError if n >= length
        """
        # Replace the line below with your code
        raise NotImplementedError
       
    def contains(self, item: tuple[int, int]) -> bool:
        """Checks whether an item is in the linkedlist.
        Returns a boolean value to indicate the status of the search.

        Arguments
            - item
              The item to be searched for.

        Returns
            True if item is found in the linkedlist,
            otherwise False
        """
        # Replace the line below with your code
        raise NotImplementedError


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python datastruct.py`
    llist = LinkedList()
    llist.append("a")  # type: ignore
    llist.append("b")  # type: ignore
    llist.insert(1, 'A')
    print("Index 0:", llist.get(1))  # a