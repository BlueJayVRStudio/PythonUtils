import os
import json
from queue import Queue

def setupDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def mapPathExt(key, path, hashSetsMap, _cacheCounter):
    cacheRoot = os.path.join(os.getcwd(), "cache/" + str(_cacheCounter))
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
                        temp = json.loads(f.read())
                        hashset = set(temp)
                else:
                    # create new hashset
                    hashset = set()
                hashSetsMap[substring] = hashset
                
            hashset.add(path) 

def main():
    currentDir = os.getcwd()

    cacheCounter = 0
    amountTraversed = 0

    q = Queue()
    # desired directory to traverse
    q.put("D:/")
    #q.enqueue("C:/")

    _hashSetsMap = {}

    while q.qsize() > 0:
        current = q.get()
        
        
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

            mapPathExt(i, fullPath, _hashSetsMap, cacheCounter)
            
            isdir = os.path.isdir(fullPath)
            if isdir:
                q.put(fullPath)
            else:
                amountTraversed += os.path.getsize(fullPath[0:-1])
        
        print (f"file size traversed: { amountTraversed / (1024*1024*1024) }")
        if (amountTraversed / (1024*1024*1024)) > 100 * (cacheCounter+1):
            keys = list(_hashSetsMap.keys())
            for i in keys:
                cacheRoot = os.path.join(os.getcwd(), "cache_new/" + str(cacheCounter))
                setupDir(cacheRoot)
                subfolder = os.path.join(cacheRoot, i)
                setupDir(subfolder)
                cacheFile = os.path.join(subfolder, "cache.json")
                
                with open(cacheFile, 'w') as f:
                    f.write(json.dumps(list(_hashSetsMap[i])))
            print("incrementing")    
            cacheCounter += 1
            print(cacheCounter)
            _hashSetsMap = {}
            
        # print (f"file size traversed in bytes: { amountTraversed }")

    keys = list(_hashSetsMap.keys())
    for i in keys:
        cacheRoot = os.path.join(currentDir, "cache_new/" + str(cacheCounter))
        setupDir(cacheRoot)
        subfolder = os.path.join(cacheRoot, i)
        setupDir(subfolder)
        cacheFile = os.path.join(subfolder, "cache.json")
        
        with open(cacheFile, 'w') as f:
            f.write(json.dumps(list(_hashSetsMap[i])))
            
    print("program finished")

print("CreateCache.py imported")

if __name__ == "__main__":
    main()
