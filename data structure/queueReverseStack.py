class Stack:
    def __init__(node):
        node.data = []
    def Empty(node):
        return node.data == []
    def push(node, data):
        node.data.append(data)
    def pop(node):
        return node.data.pop()
class Queue:
    def __init__(node):
        node.data = []
    def Empty(node):
        return node.data == []
    def enQueue(node, data):
        node.data.insert(0,data)
    def deQueue(node):
        return node.data.pop()
def Reverse():
    while( not Q.Empty()):
        S.push(Q.deQueue())
    while( not S.Empty()):
        Q.enQueue(S.pop())
S = Stack() 
Q = Queue()
Q.enQueue(10)
Q.enQueue(20)
Q.enQueue(30)
Q.enQueue(40)
Q.enQueue(50)
print(Q.data)
Reverse()
print(Q.data)