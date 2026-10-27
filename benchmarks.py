import time
from src.sorting import bubble_sort, merge_sort
import random

data = [random.randint(1, 1000) for _ in range(500)]
t0 = time.time(); bubble_sort(data); print(f"Bubble: {time.time()-t0:.4f}s")
t0 = time.time(); merge_sort(data); print(f"Merge: {time.time()-t0:.4f}s")
