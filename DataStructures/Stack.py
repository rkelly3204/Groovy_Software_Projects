#!/usr/bin/env python3

class Stack:
    
    def __init__(self, iteml=[]):
        self.items = iteml

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[-1:][0]

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)
        return 0
