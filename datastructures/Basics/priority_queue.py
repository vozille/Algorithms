import heapq
class priority_queue:
    def __init__(self):
        self.queue = []
        self.index = 0
    def push(self,item,priority):
        heapq.heappush(self.queue,(-priority,self.index,item))
    def pop(self):
        return heapq.heappop(self.queue)[-1]
q = priority_queue()
q.push('aa',1)
q.push('fgff',2)
print q.pop()
