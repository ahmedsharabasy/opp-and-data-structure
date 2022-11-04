class node:
    def __init__(self,data):       #كتبنا الداتا عشان دى حاجه موجوده فعلا وهنستخدمها اما النكست مؤشر فقط غير ملموس
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.front=self.rear=None

    def isEmpty(self):
        return self.front is None

    def enqueue(self,item):
        newnode=node(item)
        if self.rear is None:
            self.rear=self.front=newnode
        self.rear.next=newnode    #عمليه الربط نكست تكون قبل علامه اليساوى وليس قبلها لو قبلها لن يعد ربط
        self.rear=newnode
        print(item,'added to queue')

    def dequeue(self):
        if self.isEmpty():
            print('Empty queue')
            return
        temp=self.front
        self.front=self.front.next
        print(temp.data,'popped from queue')

if __name__=="__main__":
    q=queue()
    q.enqueue(10) 
    q.enqueue(20)  
    q.enqueue(30)  
    q.enqueue(40)
    q.dequeue()
    print(q.isEmpty())
    q.dequeue()         
    


