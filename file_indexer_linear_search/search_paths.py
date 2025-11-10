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

cache = os.path.join(cache_path, "paths")
if not os.path.isfile(cache):
    sys.exit(1)

with open(cache, 'r') as f:
    res = json.loads(f.read())

print([path for path in res if search_term.lower() in path.lower()])
sys.exit(0)