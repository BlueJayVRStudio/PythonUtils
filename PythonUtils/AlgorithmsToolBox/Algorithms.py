class QueueNode:
    def __init__(self, obj):
        self.obj = obj
        self.next = None

# TO DO: try using min priority queue with subdirectories count as priority
class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.count = 0

    def enqueue(self, obj):
        if self.count == 0:
            self.front = QueueNode(obj)
            self.back = self.front
        else:
            self.back.next = QueueNode(obj)
            self.back = self.back.next
        self.count += 1
        
    def dequeue(self):
        front = self.front
        if self.front is not None:
            self.front = self.front.next
            self.count -= 1
            return front.obj
        return None

def testFunction():
    print("hello world!")

print("Algorithms imported!")
