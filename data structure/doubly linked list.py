class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class linkedlist:
    def __init__(self):
        self.head=None

    def pushfirst(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
        newnode.prev=None
        if self.head is None:
            self.head.prev=newnode     #change prev of head node to new node 

    def push_after(self,prev_node,data):
        if prev_node is None:
            print('this node dosent exist in Dll')
            return
        newnode=node(data)
        newnode.next=prev_node.next
        prev_node.next=newnode
        newnode.prev=prev_node            
        if newnode.next is not None:
            newnode.next.prev=newnode

    def push_last(self,data):
        newnode=node(data)
        last=self.head
        newnode.next=None
        if self.head is None:
            newnode.prev=None
            self.head=newnode
            return
        while last.next is not None:
            last=last.next
        newnode.prev=last
        last.next=newnode
            

    def printlist(self):
        temp=self.head
        if temp is None: 
            print('Empty linked list')
        else:
            print('linked list in forward direction: ',end=' ')
            while temp is not None:
                print(temp.data,end='  ')
                temp=temp.next
            last=None
            while last is not None:
                print('linked list in reverse direction:',end=' ')
                print(last.data)
                last=last.prev              

                
if __name__=="__main__":
    llist=linkedlist()
    llist.pushfirst(10)
    llist.pushfirst(20)
    llist.pushfirst(30)
    llist.push_after(llist.head.next,99)
    llist.push_last(40)
    llist.push_last(50)
    llist.push_last(60)
    print('*'*50)
    llist.printlist()


             