class Node:
    """ Node """

    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:

    def __init__(self):
        self.head = None # Initializing the head to None

    def printList(self):
        """ List Traversal """

        current = self.head 
        while current != None:
            print(current.data)
            current = current.next

    def add_beginning(self, node):
        """ append at the beginning of the list"""

        node.next = self.head 
        self.head = node 

    def add_end(self, data):
        """ Push at the end of the list"""

        node = Node(data)

        if self.head == None:
            self.head = node 
            return 
        
        last = self.head 
        while last.next:
            last = last.next 
        last.next = node 

    def add_after_node(self, prev_node, new_data):

        """ Insert in between two Nodes """

        node = Node(new_data)

        if prev_node == None:
            print("The Node must be in a linkedlist.")
            return 

        node.next = prev_node.next 

        prev_node.next = node 

    def reverse_list(self):
        pass

        

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    # f = Node('f')

    llist.head.next = b
    b.next = c
    c.next = d 

    llist.add_beginning(e)
    llist.add_end('f')
    llist.add_after_node(c, 'w')

    llist.printList()
    