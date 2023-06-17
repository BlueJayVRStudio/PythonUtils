import os
import time
import json

def setupDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def fileSearch(key, cacheRoot):
    k = len(key)
    setupDir(cacheRoot)

    hashSets = []
    
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

            with open(cacheFile, 'r') as f:
                temp = set(json.loads(f.read()))
                hashSets.append(temp)
            
    startSet = hashSets[0]
    for i in range(1, len(hashSets)):
        startSet = startSet.intersection(hashSets[i])
    
    for i in list(startSet):
        print(i)
    

while True:
    currentDir = os.getcwd()
    _cacheRoot = os.path.join(currentDir, "cache_new")
    fileSearch(input(), _cacheRoot)


