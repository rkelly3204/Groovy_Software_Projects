#File:     LinkListDemo.py
#Purpose:  Demo on how to create and use a link list
#Author:   Adelaida A. Medlock
#Date:     Febraury 18, 2019

# The Node class - to be used to create linked lists
# a Node is the basic unit in a linked list
from Employee import *
class Node():
    def __init__(self, Employee, next = None):
        self.Employee = Employee
        self.__next = next
    
    # getters
    def getEmployee(self):
        return self.Employee
    
    def getNext(self):
        return self.__next
    
    #setters
    def setEmployee(self,Emp):
        self.Employee = Emp

    def setNext(self,n):
        self.__next = n

    #overloaded operators
    def __str__(self):
        return "Employee ID: " + str(self.Employee) + "\n Hourly Wage: "  + str(self.getNext())+"\n Money: "  + str(self.getNext())+"\n Other: "  + str(self.getNext())


# The LinkedList class: a collection of nodes (Node: data
# and a link to the next node)
class LinkedList():
    def __init__(self):
        self.__head = None
    
    def isEmpty(self):
        return self.__head == None
    
    # add a node at the end of the linked list
    def append(self, Employee):
        newNode = Node(Employee)
        
        if self.isEmpty():       # if list is empty, head will point to newNode
            self.__head = newNode
            
        else:                     # list is not empty, go to end of list and add newNode there
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)
            
    # remove a node from the linked list
    def remove(self, item):
        current = self.__head
        previous = None
        found = False
        
        # first find item in the list
        while not found:
            if current.getEmployee() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:  # item was in the fist node
            self.__head = current.getNext()
        else:  # item was somewhere after the first node
            previous.setNext(current.getNext())
    
    # search for item in linked list
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getEmployee() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    #overloaded operators
    def __getitem__(self, index):   # used to suppport []
        current = self.__head
        
        for i in range(index):
            current = current.getNext()
        
        return current.getEmployee()
    
    def __str__(self):    # used to support print(myLinkedList)
        mystr = ''
        current = self.__head
            
        while current != None:
            mystr += str(current.getEmployee()) 
            current = current.getNext()
        
        return mystr
        
    def __len__(self):    # used to support len(myLinkedList)
        if self.__head == None:  # if list is empty return 0
            return 0
        
        current = self.__head   #list is not empty and has at least 1 Node
        counter = 1
        
        while current.getNext() != None:
            counter += 1
            current = current.getNext()
        return counter
    
    
# main script to test linked list class
if __name__ == "__main__":
    print('Linked List Demo')
    print('----------------')
    
    # create a new linked list
    myLinkedList = LinkedList()
    print('Empty linked list: ')
    #print(myLinkedList)
    
    # append a few elements to the list
    Emp_ID = '123'
    Emp_ID1 = '122'
    myLinkedList.append(Emp_ID)
    myLinkedList.append(Emp_ID1)
    
    print('The current list after adding a few elements:')
    print(myLinkedList)
    print()
    
    # check if linked list is empty, if not print how many nodes there are
    if myLinkedList.isEmpty() :
        print('This linked list is empty')
    else:
        print('There are', len(myLinkedList), ' elements in the list.')
     
    # access a node via the [] operator
    for index in range(0, len(myLinkedList)):
        print('At index', index, ': ', myLinkedList[index])
    print()
    
    # remove elements from the list
    '''print('Removing an element from the list')
    myLinkedList.remove(10)
    print(myLinkedList)
    print()'''
    
    # this next line will cause an error because item to be removed is no in the list
    #myLinkedList.remove(200)
    #print(myLinkedList)
    
    # a better approach to removing items
    item = 123
    myLinkedList.remove(item)
    print(myLinkedList)
   
