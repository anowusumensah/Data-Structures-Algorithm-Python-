## Testing my understanding of linked list
class Node:
    def __init__(self, data = None):
        #__slots__ = data ,next
        self.data = data
        self.next = None


class LinkedList: # Wrapper class for the Class Node
    def __init__(self):
        self.head = None
        #self.tail = Node()
        self.size = 0
    

    def appendL(self,element):#Append data to to the head of a linkedlist
        newest = Node(element)
        newest.next = self.head
        self.head = newest
        self.size += 1
        
    def appendR(self,element):#Append data to to the tail of a linkedlist
        newest = Node(element)
        newest.next = None
        cur = self.head
        while cur.next !=None:
            cur = cur.next
        cur.next = newest
        self.size += 1  
# =============================================================================
#         newest = Node(element)
#         newest.next = None
#         if self.size == 0:
#             self.head = newest
#         else:
#            self.tail.next = newest 
#         self. tail = newest   
#         self.size += 1    
# =============================================================================
    
    def len(self): #Return size of linkedlist
        return self.size
    
    def display(self): #Display elements in the linkedlist
        elems = []
        cur = self.head
        if self.size == 0:
             return print("Linked list is empty", end = "\n")
        while cur:
            elems.append(cur.data)
            cur = cur.next
        return print(f"The elements are : ({elems})")    
    
    def rev_first(self): #Remove first element in the linkedlist & return the value
        if self.size == 0:
             return print("Linked list is empty", end = "\n")       
        elem = self.head.data
        self.head = self.head.next
        self.size -= 1
        return elem
    
    
    def rev_last(self): #Remove last element in the linkedlist
        if self.size == 0:
           return print("Linked list is empty", end = "\n")
        checker = 1 # Used to count up to the last but one node
        cur_node = self.head
        while cur_node.next !=None:
            cur_node = cur_node.next
            checker += 1
            if checker == self.size - 1: # If we are at penultimate Node, 
            #set its next node to reference None
               cur_node.next = None
               #break
        self.size -= 1
       
        
        
if __name__ == '__main__':
    my_list = LinkedList()     
    my_list.appendL("A")
    my_list.appendL("B")
    my_list.appendL("C")
    my_list.appendL("D")
    my_list.appendL("E")
    my_list.appendL(1)
    my_list.appendL(2)
    my_list.appendL(3)
    my_list.appendR(4)
    my_list.appendR(5)
    my_list.appendR(6)
    print('After appending')
    my_list.display() 
    
    print()
    my_list.rev_first()
    print('After removing 1st element')
    my_list.display()
# #     
    print()
    
    my_list.rev_last()
    print('After removing last element')
    my_list.display()
    
    print()
    
    my_list.rev_last()
    print('After removing last element')
    my_list.display()
    

#my_list.head.data
        

