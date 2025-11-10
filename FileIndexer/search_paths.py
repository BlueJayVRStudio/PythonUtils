import sys, os
from collections import defaultdict
import json

if len(sys.argv) < 2:
    sys.exit(1)

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
PARENT_DIR = os.path.dirname(BASE_DIR)
cache_path = os.path.join(BASE_DIR, "cache")

path_cache = defaultdict(lambda: set())

def EnsureDir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
EnsureDir(cache_path)

search_term = sys.argv[1]

if len(search_term) == 1:
    sys.exit(1) # for now

key = search_term[:2].encode().hex()
cache = os.path.join(cache_path, key)
if not os.path.isfile(cache):
    sys.exit(1)

with open(cache, 'r') as f:
    res = set(json.loads(f.read()))

for i in range(1, len(search_term)-1):
    key = search_term[i:i+2].encode().hex()
    cache = os.path.join(cache_path, key)
    if not os.path.isfile(cache):
        sys.exit(1)

    with open(cache, 'r') as f:
        res = res.intersection(set(json.loads(f.read())))
    
print([path for path in list(res) if search_term in path])
sys.exit(0)