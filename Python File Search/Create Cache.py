import os
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

def setupDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def mapPathExt(key, path, hashSetsMap):
    cacheRoot = os.path.join(os.getcwd(), "cache_new")
    setupDir(cacheRoot)

    k = len(key)
    
    for i in range(0, k):
        for j in range(1, 3):
            if i+j > k:
                continue
            substring = key[i:i+j]
            substring = substring.lower()

            # or you can replace with some other character and deal with false positives, which may not be all that bad
            substring = substring.replace(" ", "_")
            if len(substring) == 1:
                substring += "_pad"

            subfolder = os.path.join(cacheRoot, substring)
            setupDir(subfolder)
            cacheFile = os.path.join(subfolder, "cache.json")

            hashset = None

            if substring in hashSetsMap:
                hashset = hashSetsMap[substring]
            else:
                if len(hashSetsMap) > 1000:
                    keys = list(hashSetsMap.keys())
                    
                    subfolder = os.path.join(cacheRoot, keys[0])
                    setupDir(subfolder)
                    cacheFile1 = os.path.join(subfolder, "cache.json")
                    
                    with open(cacheFile1, 'w') as f:
                        f.write(json.dumps(list(hashSetsMap[keys[0]])))

                    hashSetsMap.pop(keys[0])
                    
                if os.path.isfile(cacheFile):
                    # deserialize into hashmap
                    with open(cacheFile, 'r') as f:
                        hashset = set(json.loads(f.read()))
                else:
                    # create new hashset
                    hashset = set()
                hashSetsMap[substring] = hashset
                
            hashset.add(path) 

currentDir = os.getcwd()

amountTraversed = 0

q = Queue()
# desired directory to traverse
q.enqueue("D:/")
#q.enqueue("C:/")

_hashSetsMap = {}

while q.count > 0:
    current = q.dequeue()
    # filter out unwanted directories
    if current in ["D:/$RECYCLE.BIN/", "D:/Python Projects/Python File Search/", "C:/Windows/", "C:/Windows.old/"]:
        continue
    
    items = None
    try:
        items = os.listdir(current)
    except:
        continue

    for i in items:
        if len(i) > 40:
            continue
        
        fullPath = current + i + "/"

        mapPathExt(i, fullPath, _hashSetsMap)
        
        isdir = os.path.isdir(fullPath)
        if isdir:
            q.enqueue(fullPath)
        else:
            amountTraversed += os.path.getsize(fullPath[0:-1])
    
    print (f"file size traversed: { amountTraversed /(1024*1024*1024) }")
    # print (f"file size traversed in bytes: { amountTraversed }")

keys = list(_hashSetsMap.keys())
for i in keys:
    cacheRoot = os.path.join(currentDir, "cache_new")
    setupDir(cacheRoot)
    subfolder = os.path.join(cacheRoot, i)
    setupDir(subfolder)
    cacheFile = os.path.join(subfolder, "cache.json")
    
    with open(cacheFile, 'w') as f:
        f.write(json.dumps(list(_hashSetsMap[i])))
        
print("program finished")

