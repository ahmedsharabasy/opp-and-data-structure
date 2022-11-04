#ميزة اللينكد استاك ان اما معرفش عدد عناصر الاستاك مش محتاج اشيك على العناصر الستاك مليانة ولا لا
class node:
    def __init__(self,data):         #constructor for inttialize node 
        self.data=data
        self.Next=None             

class stack:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return True if self.head is None else False

    def push(self,element):
        newnode=node(element)
        newnode.Next=self.head        #عملية الربط بين الاتنين نود  pointer
        self.head=newnode        #جعل الهيد على النود الجديدة
        print(element,'pushed to stack')


    def pop(self):
        if self.isEmpty():
            print('stack is empty')
            return None
        temp=self.head
        self.head=self.head.Next
        popped=temp.data
        print(popped,'popped from stack')

    def peek(self):
        if self.isEmpty():
            print('stack is empty')
            return None 
        print(self.head.data,'is the top element')


if __name__=="__main__":
    
    stack=stack()       #object from class
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.pop()
    stack.peek()
    stack.pop()
    stack.peek()
    stack.pop()
    stack.peek()
    stack.pop()
    stack.peek()




                    
