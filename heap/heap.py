class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        last_index = self.get_size() - 1
        return self._bubble_up(last_index)

    def delete(self):
        last_index = self.get_size() - 1
        self.storage[0], self.storage[last_index] = self.storage[last_index], self.storage[0]
        deleted = self.storage.pop()
        self._sift_down(0)
        return deleted

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    # helper function for insert
    def _bubble_up(self, index):
        while (index - 1) // 2 >= 0:
            # compare child value against parent value
            if self.storage[(index - 1)//2] < self.storage[index]:
                # swap via indices
                self.storage[index], self.storage[(
                    index - 1)//2] = self.storage[(index - 1)//2], self.storage[index]
            # repeat
            index = (index - 1)//2

    # helper function for delete
    def _sift_down(self, index):
        last_index = self.get_size() - 1
        # while the left child > last index
        while index * 2 + 1 <= last_index:
            # if right child > last index
            if index * 2 + 2 > last_index:
                # larger child is left
                child = index * 2 + 1
            # if left child >= right child
            else:
                # if left child > right child
                if self.storage[index * 2 + 1] > self.storage[index * 2 + 2]:
                    # set child to left child
                    child = index * 2 + 1
                # if right child >= left child
                else:
                    # set child tp right child
                    child = index * 2 + 2
            # if current value < child, swap
            if self.storage[index] < self.storage[child]:
                self.storage[index], self.storage[child] = self.storage[child], self.storage[index]
            index = child
