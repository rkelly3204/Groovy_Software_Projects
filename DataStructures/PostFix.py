#!/usr/bin/env python3

from lexer import *

def expressionFetch()
    expression = []
    while get_expression():
        t = get_next_token()
        while t:
            expression.append(t)
        t = get_next_token()

    print(expression)
    str1 = ''.join(str(e)for e in expression)




precedenceOp = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}

def postfix2infix(infix):
    stack = []
    postfix = []

    for char in infix:
        if char not in precedenceOp:
            postfix.append(char)

        else:
            if len(stack) == 0:
                stack.append(char)

            elif char == ")":
                while stack[len(stack) - 1] != "(":
                    postfix.append(stack.pop())
                stack.pop()

            elif precedenceOp[char] > precedenceOp[stack[len(stack) - 1]]:
                stack.append(char)

            else:
                while len(stack) != 0:
                    if stack[len(stack) -1 ] == '(':
                        break
                    postfix.append(stack.pop())
                stack.append(char)
    while len(stack) != 0:
        postfix.append(stack.pop())
    return postfix

class Nodes():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpandTree():
    def __init__(self, vertex = None):
        self.vertex = vertex



    def preorder(self):
        self.preorderHelp(self.vertex)

    def preorderHelp(self, node):
        if node:
            print(node.value, end='')
            self.preorderHelp(node.left)
            self.preorderHelp(node.right)

    def postorder(self):
        self.postorderHelp(self.vertex)


    def postorderHelp(self, node):
        if node:
            self.postorderHelp(node.left)
            self.postorderHelp(node.right)
            print(node.value, end='')

    def inorder(self):
        self.inorderHelp(self.vertex)

    def inorderHelp(self, node):
        if node:
            self.inorderHelp(node.left)
            print(node.value, end='')
            self.inorderHelp(node.right)

def nodeTree(infix):
    postfix = postfix2infix(infix)
    stack = []

    for i in postfix:
        if i not in precedenceOp:
            node = Nodes(i)
            stack.append(node)
        else:
            node = Nodes(i)
            left = stack.pop()
            right = stack.pop()
            node.right = right
            node.left = left
            stack.append(node)

    return ExpandTree(stack.pop())

expression = "(5+3)*6"
print("Inorder: ")
nodeTree(expression).inorder()
print("\nPost Order:")
nodeTree(expression).postorder()
print("\nPre Order:")
nodeTree(expression).preorder()
