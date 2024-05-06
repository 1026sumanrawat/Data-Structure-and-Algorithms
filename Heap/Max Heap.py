# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2)//2
        for i in reversed(range(firstParentIdx+1)):
            self.siftDown(i, len(array) -1 , array)
        return array

    def siftDown(self, currentIdx ,lastIdx, heap):
        childOneIdx = (currentIdx * 2) + 1
        while childOneIdx <= lastIdx:
            childTwoIdx = (currentIdx * 2) + 2 if (currentIdx * 2) + 2 <= lastIdx else -1
            if childTwoIdx != -1 and heap[childOneIdx] < heap[childTwoIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[currentIdx] < heap[idxToSwap]:
                self.swap(heap, idxToSwap, currentIdx)
                currentIdx = idxToSwap
                childOneIdx = (currentIdx * 2) + 1
                
            else:
                return
        

    def siftUp(self, currentIdx, heap):
        parentIdx = ( currentIdx - 1)//2
        while currentIdx > 0 and heap[parentIdx] < heap[currentIdx]:
            self.swap(heap, currentIdx, parentIdx)
            currentIdx = parentIdx
            parentIdx = ( currentIdx - 1)//2
            
    def peek(self):
        return self.heap[0]

    def remove(self):
        lastIdx = len(self.heap) - 1
        self.swap(self.heap, lastIdx, 0)
        val = self.heap.pop(lastIdx)
        self.siftDown(0,len(self.heap)-1, self.heap)
        return val

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, heap, indexOne, indexTwo):
        heap[indexOne], heap[indexTwo] = heap[indexTwo], heap[indexOne]
