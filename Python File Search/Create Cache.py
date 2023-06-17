import os
import time
import json

class Node:
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
            self.front = Node(obj)
            self.back = self.front
        else:
            self.back.next = Node(obj)
            self.back = self.back.next
        self.count += 1
        
    def dequeue(self):
        front = self.front
        if self.front is not None:
            self.front = self.front.next
            self.count -= 1
            return front.obj
        return None

def mapPath(key, path, hashMap):
    k = len(key)
    for i in range(0, k):
        for j in range(1, k+1):
            if i+j > k:
                continue
            substring = key[i:i+j]
            substring = substring.lower()
            if substring not in hashMap:
                hashMap[substring] = set()
            hashMap[substring].add(path)

def setupDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def mapPathExt(key, path, cacheRoot):
    k = len(key)

    setupDir(cacheRoot)
    
    for i in range(0, k):
        for j in range(1, k+1):
            if i+j > k:
                continue
            substring = key[i:i+j]
            substring = substring.lower()

            try:
                subfolder = os.path.join(cacheRoot, substring)
                while subfolder[-1] in [" ", "."]:
                    subfolder = subfolder[0:-1]
                setupDir(subfolder)
            except:
                subfolder = os.path.join(cacheRoot, substring)
                while subfolder[-1] in [" ", "."]:
                    subfolder = subfolder[0:-1]
                subfolder += "---RESTRICTEDWORD---"
                setupDir(subfolder)

            cacheFile = os.path.join(subfolder, "cache.json")
            

            hashset = None
            
            if os.path.isfile(cacheFile):
                # deserialize into hashmap
                with open(cacheFile, 'r') as f:
                    hashset = set(json.loads(f.read()))
            else:
                # create new hashset
                hashset = set()
                
            hashset.add(path)

            with open(cacheFile, 'w+') as f:
                #print(subfolder)
                f.write(json.dumps(list(hashset)))

currentDir = os.getcwd()
cacheRoot = os.path.join(currentDir, "cache")
print(cacheRoot)

amountTraversed = 0

q = Queue()
# add desired directories to traverse
q.enqueue("D:/")
q.enqueue("C:/")

while q.count > 0:
    current = q.dequeue()
    if current in ["D:/$RECYCLE.BIN/", currentDir]:
        continue
    #print(current)
    
    items = None
    try:
        items = os.listdir(current)
    except:
        continue
    
    for i in items:
        fullPath = current + i + "/"

        # hash substrings(key):set(path)
        mapPathExt(i, fullPath, cacheRoot)
        
        isdir = os.path.isdir(fullPath)
        if isdir:
            q.enqueue(fullPath)
        else:
            amountTraversed += os.path.getsize(fullPath[0:-1])
            pass
    print (f"file size traversed: { amountTraversed /(1024*1024*1024) }")
    print (f"file size traversed in bytes: { amountTraversed }")


print("program finished")

