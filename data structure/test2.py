class Node:
    def __init__(self,data):
        self.data=data 
        self.Next=None

class stack:
    def __init__(self):
        self.head=None

    def push(self,item):
        newnode=Node(item)
        newnode.Next=self.head
        self.head=newnode
        print(item,"pushed to stack")

    def poped(self):
        if self.head is None:
            print("Empty stack")
        temp=self.head
        self.head=self.head.Next
        print(temp.data,"popped from stack")

    def peek(self):
        if self.head is None:
            print("Empty stack")
        print(self.head.data,"is the top value")

if __name__=="__main__":
    s=stack()
    s.push(1)
    s.push(2) 
    s.push(3) 
    s.push(4)
    s.poped()
    s.peek()                                                                  