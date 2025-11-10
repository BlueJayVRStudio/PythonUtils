import os
from collections import defaultdict
import json

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
PARENT_DIR = os.path.dirname(BASE_DIR)
cache_path = os.path.join(BASE_DIR, "cache")

path_cache = defaultdict(lambda: set())

def EnsureDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
EnsureDir(cache_path)

for dirpath, dirnames, filenames in os.walk("C://"): # Tested on windows with C drive. Change this to whichever directory you want to index
    if dirpath == cache_path:
        continue
    for dir in dirnames:
        curr_path = os.path.join(dirpath, dir)
        for i in range(len(dir)-1):
            path_cache[dir[i:i+2]].add(curr_path)
    for file in filenames:
        curr_path = os.path.join(dirpath, file)
        for i in range(len(file)-1):
            path_cache[file[i:i+2]].add(curr_path)

for key, value in path_cache.items():
    with open(os.path.join(cache_path, key.encode().hex()), "w") as f:
        f.write(json.dumps(list(value)))


