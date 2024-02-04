import heapq


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def pop(self):
        if self.queue:
            priority, item = heapq.heappop(self.queue)
            return item
        else:
            raise IndexError("Pop from an empty priority Queue")
        
    def peek(self):
        if self.queue:
            return self.queue[0][1]
        else:
            return None
        
priority_queue = PriorityQueue()
priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)

print("Peek:", priority_queue.peek())  # Output: Task 2
print("Pop:", priority_queue.pop())    # Output: Task 2
print("Peek after pop:", priority_queue.peek())  # Output: Task 3
