class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def peek(self):
        if self.head is None:
            raise IndexError("peek from empty stack")
        return self.head.value
    
    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        value = self.head.value
        self.head = self.head.next
        return value
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node       
        else:
            self.tail.next = new_node  

        self.tail = new_node           
        
    def dequeue(self):
        if self.head is None:
            raise IndexError("dequeue from empty queue")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value
    
    def peek(self):
        if self.head is None:
            raise IndexError("peek from empty queue")
        return self.head.value