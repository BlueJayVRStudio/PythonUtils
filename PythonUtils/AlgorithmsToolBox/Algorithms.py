def TestFunction():
    print("Algorithms imported!")

class QueueNode:
    def __init__(self, obj):
        self.obj = obj
        self.next = None

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

# index starting from 1 to N
# WORK IN PROGRESS; This is a naive implementation and it will be modified to accomodate many different use cases
class MinBinHeap:
    def __init__(self):
        self.A = [None]
    
    def arrlen(self, A):
        return len(A) - 1

    def swap(self, A, i, j):
        A[i], A[j] = A[j], A[i]
    
    def left(self, i):
        return (2 * i)
    
    def right(self, i):
        return (2 * i + 1)
    
    def bubbleup(self, A, j):
        if j <= 1:
            return
        else:
            if (A[j] < A[j//2]):
                self.swap(A, j, j//2)
                self.bubbleup(A, j//2)
        return

    def bubbledown(self, A, j):
        n = self.arrlen(A)
        left = self.left(j)
        right = self.right(j)
        # no child
        if (left > n):
            return
        # 1 child
        if (left <= n and right > n):
            if (A[j] > A[left]):
                self.swap(A, j, left)
                self.bubbledown(A, left)
        # 2 children
        else:
            # find bigger child
            small = None
            if (A[left] < A[right]):
                small = left
            else:
                small = right
            if (A[j] > A[small]):
                self.swap(A, j, small)
                self.bubbledown(A, small)
    
    def find(self, A, val, curr):
        if A[curr] == val:
            return curr
        else:
            n = self.arrlen(A)
            left = self.left(curr)
            right = self.right(curr)
            # no child
            if (left > n):
                return None
            # 1 child (left)
            if (left <= n and right > n):
                return self.find(A, val, left)
            # 2 children
            else:
                leftChild = self.find(A, val, left)
                rightChild = self.find(A, val, right)
                if leftChild is not None:
                    return leftChild
                elif rightChild is not None:
                    return rightChild
                else:
                    return None

    # O(log(n))
    def insert(self, A, val):
        A.append(val)
        self.bubbleup(A, self.arrlen(A))
    # O(log(n))
    def deletemin(self, A):
        if (self.arrlen(A) == 0):
            return
        A[1] = A[self.arrlen(A)]
        A.pop()
        if (self.arrlen(A) > 1):
            self.bubbledown(1)
    # O(log(n))
    def deleteAt(self, A, j):
        if (self.arrlen(A) == 0):
            return
        A[j] = A[self.arrlen(A)]
        A.pop()
        if (self.arrlen(A) > 1):
            self.bubbleup(A, j)
            self.bubbledown(A, j)
    # O(log(n))
    def modifyPriorityAt(self, A, j):
        if (self.arrlen(A) > 1):
            self.bubbleup(A, j)
            self.bubbledown(A, j)
    
    def heapify(self, A):
        for i in range(self.arrlen(A), 0, -1):
            self.bubbledown(A, i)
    
    def heapsort(self, A):
        self.heapify(A)
        result = []
        while (self.arrlen(A) > 0):
            result.append(A[1])
            self.deletemin(A)
        return result

    def getmin(self, A):
        return A[1]
    
 

TestFunction()

