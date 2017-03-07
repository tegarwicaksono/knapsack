import heapq
from recordclass import recordclass

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def empty(self):
        if (len(self._queue) is 0):
            return True
        else:
            return False

    def length(self):
        return len(self._queue)
        

PQNode = recordclass('PQNode', 'level value weight bound items')
Q = PriorityQueue()

v = PQNode(level = -1, value = 'a', weight = 0, bound = 0, items = [])
Q.push(v, 4)
v = PQNode(level = -1, value = 'b', weight = 0, bound = 0, items = [])
Q.push(v, 2)
v = PQNode(level = -1, value = 'c', weight = 0, bound = 0, items = [])
Q.push(v, 1)
v = PQNode(level = -1, value = 'd', weight = 0, bound = 0, items = [])
Q.push(v, 3)

abc = []

#print("Length abc empty ", abc.empty())

#print("length = ", Q.length())

print("Empty? ", Q.empty())

b = Q.pop()
print("b value = ", b.value)