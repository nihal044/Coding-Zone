class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class queue:
    def __init__(self):
        self.front=self.rear = None
    def isempty(self):
        return self.front == None
    def enqueue(self, item):
        temp = Node(item)
        if self.rear ==None:
            self.front = self.rear = temp
            return
        self.rear.next=temp
        self.rear=temp
    def dequeue(self):
        if self.isempty():
            return
        temp=self.front
        self.front=temp.next
        if(self.front == None):
            self.rear=None
#if __name == '__main__':
if __name__ == '__main__':
    q=queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.dequeue()
    q.dequeue()
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    q.dequeue()
    print("queue front"+str(q.front.data))
    
    print("queue rear"+str(q.rear.data))
    
    
        
        
        
