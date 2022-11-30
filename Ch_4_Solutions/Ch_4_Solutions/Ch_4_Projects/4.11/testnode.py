"""
File: testnode.py
Project 4.11

Add a makeTwoWay function.

Tests the Node class.
"""

from node import Node, TwoWayNode

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    while probe != None:
        count += 1
        probe = probe.next
    return count
    
def insert(index, newItem, head):
    """Inserts newItem at position is the linked structure
    referred to by head.  Returns a reference to the new
    structure."""
    if index <= 0:
        # newItem goes at the head
        head = Node(newItem, head)
    else:
        # Search for node at position index - 1 or the last position
        probe = head
        while index > 1 and probe.next != None:   
            probe = probe.next;
            index -= 1
        # Insert new node after node at position index - 1 
        # or last position
        probe.next = Node(newItem, probe.next)
    return head

def pop(index, head):
    """Removes the item at index from the linked structure
    referred to by head and returns the tuple (head, item)
    Precondition: 0 <= index < length(head)"""
    if index < 0 or index >= length(head):
        raise IndexErro("Index out of bounds")
    # Assumes that the linked structure has at least one item
    if index == 0:
        removedItem = head.data
        head = head.next
    else:
        # Search for node at position index - 1 or 
        # the next to last position
        probe = head
        while index > 1 and probe.next.next != None:
            probe = probe.next
            index -= 1
        removedItem = probe.next.data
        probe.next = probe.next.next
    return (head, removedItem)

def makeTwoWay(head):
    """Creates and returns a doubly linked structure that
    contains the items in the structure referred to by head."""
    if head is None:
        # Empty structure
        return None
    else:
        # Set the first node
        twoWayHead = TwoWayNode(head.data)
        twoWayProbe = twoWayHead
        probe = head
        # Set remaining nodes, if any
        while probe.next != None:
            newNode = TwoWayNode(probe.next.data, twoWayProbe)
            twoWayProbe.next = newNode
            twoWayProbe = newNode
            probe = probe.next
        return twoWayHead

def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe != None:
        print(probe.data, end = " ")
        probe = probe.next
    print()


def main():
    """Tests modifications."""
    head = None

    # Add five nodes to the beginning of the linked structure
    for count in range(1, 6):
        head = Node(count, head)
    
    print("5 4 3 2 1:", end = " ")
    printStructure(head)
    
    print("5 4 3 2 1:", end = " ")
    twoWayHead = makeTwoWay(head)
    printStructure(twoWayHead)


if __name__ == "__main__": main()


