class MaxHeap:

    def __init__(self):
        self.queue = [None]

    def insert(self, value):
        ## Insert a new value into heap
        """
        Input:  value
        Output: None
        """
        index = len(self.queue)
        self.queue.append(value)
        while index // 2 != 0:
            if self.queue[index] > self.queue[index // 2]:
                temp = self.queue[index]
                self.queue[index] = self.queue[index // 2]
                self.queue[index // 2] = temp
                index = index // 2
            else:
                break

    def delete(self):
        ## Delete root node
        """
        Input:  None
        Output: if heap is empty print('Heap is empty')
                return deleted value
        """
        if len(self.queue) == 1:
            print("Heap is empty")
            return

        item = self.queue[1]
        self.queue[1] = self.queue[len(self.queue) - 1]
        self.queue[len(self.queue) - 1] = item

        self.queue.pop()

        i = 1
        while i * 2 + 1 <= len(self.queue) - 1:
            # -------------Fill in the blank
            # HINT- left = i*2
            #     - right = i*2 + 1
            if self.queue[i] < self.queue[i * 2]:
                temp = self.queue[i]
                self.queue[i] = self.queue[i * 2]
                self.queue[i * 2] = temp
                i = i * 2
            elif self.queue[i] < self.queue[i * 2 + 1]:
                temp = self.queue[i]
                self.queue[i] = self.queue[i * 2 + 1]
                self.queue[i * 2 + 1] = temp
                i = i * 2 + 1

        return item


def main():
    maxheap = MaxHeap()

    maxheap.insert(5)
    maxheap.insert(7)
    maxheap.insert(6)
    maxheap.insert(9)
    maxheap.insert(2)
    print(maxheap.queue)
    maxheap.insert(4)
    maxheap.insert(3)
    maxheap.insert(2)
    maxheap.insert(8)
    print(maxheap.queue)

    maxheap.delete()
    print(maxheap.queue)


main()