import itertools
from heapq import *

class PriorityQueue:
    def __init__(self):
        self._pq = []
        self._entry_map = {}
        self._counter = itertools.count()

    def addtask(self, task, priority = 0):
        '''Add a new task or update the priority of an existing task'''
        if task in self._entry_map:
            self.removetask(task)
        count = next(self._counter)
        entry = [priority, count, task]
        self._entry_map[task] = entry
        heappush(self._pq, entry)

    def removetask(self, task):
        '''Mark an existing task as REMOVED.'''
        entry = self._entry_map.pop(task)
        entry[-1] = 'removed'

    def poptask(self):
        '''Remove and return the lowest priority task.'''
        while self._pq:
            priority, count, task = heappop(self._pq)
            if task is not 'removed':
                del self._entry_map[task]
                return task

    def __len__(self):
        return len(self._entry_map)

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.addtask(1, 3)
    pq.addtask(2, 4)
    pq.addtask(3, 5)
    pq.addtask(2, 1)
    pq.addtask(3, 0.5)
    while pq:
        print(pq.poptask())