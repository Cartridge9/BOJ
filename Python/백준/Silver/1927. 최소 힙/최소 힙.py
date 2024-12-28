import heapq as h
import sys

n = int(sys.stdin.readline())

heap = []
for i in range(n):
  a = int(sys.stdin.readline())
  if a == 0:
    if len(heap) != 0:  
      print(h.heappop(heap))
    else:
      print(0)
  else:
    h.heappush(heap, a)
    # h.heapify(heap)