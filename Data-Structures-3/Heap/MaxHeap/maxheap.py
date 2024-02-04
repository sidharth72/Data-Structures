class MaxHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up()

    def delete(self):
        if len(self.heap) > 1:
            # First, we need to swap value index 0, and last
            self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
            popped = self.heap.pop()
            self._heapify_down()
        elif len(self.heap) == 1:
            popped = self.heap.pop()
        else:
            raise IndexError("Pop from an empty heap")
        return popped

    
    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_idx = 2 * index + 1
            right_child_idx = 2 * index + 2
            
            # Assume index is the largest initially
            largest = index

            if left_child_idx < len(self.heap) and self.heap[left_child_idx] > self.heap[largest]:
                largest = left_child_idx
            if right_child_idx < len(self.heap) and self.heap[right_child_idx] > self.heap[largest]:
                largest = right_child_idx

            if largest != index:
                self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
                index = largest
            else:
                break


    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
        
    

maxheap = MaxHeap()
maxheap.insert(5)
maxheap.insert(9)
maxheap.insert(1)
maxheap.insert(3)
maxheap.insert(9)
maxheap.insert(11)
maxheap.insert(31)

print(maxheap.heap)


    