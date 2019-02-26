class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []  # could be LinkedList or 2 Stacks as alternative

    def enqueue(self, item):
        return self.storage.append(item)  # add_to_tail in LL, increment size

    def dequeue(self):
        if len(self.storage) == 0:  # if size = 0, return size
            return None
        else:
            # remove_from_head in LL, decrement size
            return self.storage.pop(0)

    def len(self):
        return len(self.storage)  # return size
