class queue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.front=self.size=0
        self.rear=capacity-1
        self.Q=[None]*capacity

    def isfull(self):
        return self.size==self.capacity

    def isEmpty(self):
        return self.size==0

    def enqueue(self,item):
        if self.isfull():
            print('queue is full')
        self.rear=(self.rear+1)%(self.capacity)     #%هنا عشان الرير ميعديش طول الاريى اللى اليوز مدخلها لان لو عدى او بق = الير هيساوى صفر
        self.Q[self.rear]=item
        self.size=self.size+1
        print(item,'enqueued to queue')

    def dequeue(self):
        if self.isEmpty():
            return print('queue is empty')
            
        print(self.Q[self.front],'dequeued from queue')
        self.front=(self.front+1)%(self.capacity)
        self.size=self.size-1

    def getFront(self):
        if self.isEmpty():
            return print('queue is empty')
            
        print(self.Q[self.front],'is the front item')

    def getrear(self):
        if self.isEmpty():
            return print('queue is empty')

        print(self.Q[self.rear],'is the last item')


if __name__=="__main__":
    queue=queue(30)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.dequeue()
    queue.getFront()
    queue.getrear()
    queue.dequeue()
    queue.getFront()
    queue.getrear()
    queue.dequeue()
    queue.getFront()
    queue.getrear()
    queue.dequeue()
    queue.getFront()
    queue.getrear()
    queue.dequeue()
    queue.getFront()
    queue.getrear()            



