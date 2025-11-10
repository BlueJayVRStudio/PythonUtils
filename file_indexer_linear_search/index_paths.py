import sys, os
from collections import defaultdict
import json

if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
    sys.exit(1)

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
PARENT_DIR = os.path.dirname(BASE_DIR)
cache_path = os.path.join(BASE_DIR, "cache")

paths = []

def EnsureDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
EnsureDir(cache_path)

for dirpath, dirnames, filenames in os.walk(sys.argv[1]): # This will take the directory path from commandline input
    if dirpath == cache_path:
        continue
    for dir in dirnames:
        curr_path = os.path.join(dirpath, dir)
        paths.append(curr_path)
    for file in filenames:
        curr_path = os.path.join(dirpath, file)
        paths.append(curr_path)

with open(os.path.join(cache_path, "paths"), "w") as f:
    f.write(json.dumps(paths))


