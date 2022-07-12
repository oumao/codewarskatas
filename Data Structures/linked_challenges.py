
class Node:
    
    def __init__(self, data):
        self.data = data 
        self.next = None


def sum_list(head):

    """
    Question 2: Write a function, sum_list, that takes in the head of a 
    linked list containing numbers as an argument.
    The function should return the total sum of all values in the linked list.
    """

    current = head 
    sum = 0
    while current != None: 
        sum += current.data 
        current = current.next 
    return sum 


def find_item(head, target):
    """
    Write a function that takes in the head of a linked list and a target value.
    The function should return a boolean indicating whether or not the linked list
    contains the target.
    """
    current = head 
    while current != None:
        if target == current.data:
            return True 
        current = current.next  
    return False


def get_node(head, index):
    """
    Write a function that takes in the head of a linked list and an index.
    The function should return the value of the linked list at the specified
    index. If there is no node at the given index, then return null.
    """
    count = 0
    current = head 
    while current != None: 
        if count == index: return current.data
        count += 1
        current = current.next 

    