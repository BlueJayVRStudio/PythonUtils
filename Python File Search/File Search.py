import os
import time
import json

currentDir = os.getcwd()
cacheRoot = os.path.join(currentDir, "cache")
print(cacheRoot)

def setupDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def fileSearch(key, cacheRoot):

    setupDir(cacheRoot)

    try:
        subfolder = os.path.join(cacheRoot, key)
        while subfolder[-1] in [" ", "."]:
            subfolder = subfolder[0:-1]
        setupDir(subfolder)
    except:
        subfolder = os.path.join(cacheRoot, key)
        while subfolder[-1] in [" ", "."]:
            subfolder = subfolder[0:-1]
        subfolder += "---RESTRICTEDWORD---"
        

    cacheFile = os.path.join(subfolder, "cache.json")
    

    hashset = None
    
    if os.path.isfile(cacheFile):
        # deserialize into hashmap
        with open(cacheFile, 'r') as f:
            hashset = set(json.loads(f.read()))
    if hashset is not None:
        for i in sorted(list(hashset)):
            print(i)
    else:
        print(None)

while True:
    fileSearch(input(), cacheRoot)


