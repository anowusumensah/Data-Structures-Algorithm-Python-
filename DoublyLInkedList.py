# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 22:22:42 2022

@author: Tony
"""

class Node:
    def __init__(self, data = None, prev = None, next = None):
        #__slots__ = data ,next
        self.data = data
        self.prev = prev
        self.next = next 


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail # Head comes before the tail
        self.tail.prev = self.head # Tail is after the head
        self.size = 0
        
    def appendL(self,element):
       prev_ = self.head
       next_ = self.head.next 
       newest = Node(element,prev_,next_)
       prev_.next = newest
       next_.prev = newest
       self.size += 1
       #return   self.size
      
    def appendR(self,element):
       prev_ = self.tail.prev
       next_ = self.tail 
       newest = Node(element,prev_,next_)
       prev_.next = newest
       next_.prev = newest
       self.size += 1
       
    def del_first(self):
        if self.size == 0:
            return(print("Doublylinkedlist is empty"))
        elem = self.head.next.data
        prev_ = self.head
        next_ = self.head.next.next
        prev_.next = next_
        next_.prev = prev_
        self.size += -1
        return elem
    
    def del_last(self):
        if self.size == 0:
            return(print("Doublylinkedlist is empty"))
        elem = self.tail.prev.data
        prev_ = self.tail.prev.prev
        next_ = self.tail
        prev_.next = next_
        next_.prev = prev_
        self.size += -1
        return elem
    
    def len(self):
        return self.size
    
    
    def display(self): #Display elements in the linkedlist
        elems = []
        cur = self.head
        cout = 0
        if self.size == 0:
             return print("Linked list is empty", end = "\n")
        while cur.next != None:
            cur = cur.next
            cout += 1
            elems.append(cur.data)
            if cout == self.size:
                break
        return print(f"The elements are : ({elems})")      
              
       
    
        
if __name__ == '__main__':
    my_list = DoublyLinkedList()     
    my_list.appendL("A")
    my_list.appendL("B")
    my_list.appendL("C")
    my_list.appendL("D")
    my_list.appendL("E")
    my_list.appendL(2)
    my_list.appendL(3)
    my_list.appendR(4)
    my_list.appendR(5)
    my_list.appendR(6)
    
    
    print('After appending')
    my_list.display() 
    #print(my_list.len())
    print()
    
    
    print('After deletion of first element')
    
    my_list.del_first()
    my_list.display() 
    #print(my_list.len())
    print()
    
    print('After deletion of first element')
    my_list.del_first()
    my_list.display()
    
    #print(my_list.len())
    
    
    print()
    
    print('After deletion of last element')
    my_list.del_last()
    my_list.display()
   
    #print(my_list.len())
    print()
    print('After deletion of last element')
    my_list.del_last()
    my_list.display()
    
    #print(my_list.len())
    
    #print(my_list.len())
    
    