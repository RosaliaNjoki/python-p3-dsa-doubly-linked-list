class Node: 
    def __init__(self, data, next_node = None, prev_node =None):
        self.data = data 
        self.next_node = next_node
        self.prev_node = prev_node

class SinglyLinkedList: 
    def __init__(self, head=None, Tail=None):
        self.head=head

    def delete_tail(self):
        if self.head ==None:
            return 
        curr = self.head
        prev = None 
        while curr.next_node:
            prev = curr 
            curr = curr.next_node 
        prev.next_node = None 

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head=head
        self.tail=tail
    def append(self, node):
        if self.head==None:
            self.head=node
            self.tail=node
            return
        node.prev_node = self.tail
        self.tail.next_node = node 
        self.tail = node    


    def delete_tail(self):
        if self.head==self.tail:
            self.head=None 
            self.tail=None 
        else: 
            pre= self.tail.prev_node 
            prev.next_node = None 
            self.tail=prev    



