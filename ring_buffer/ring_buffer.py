class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.oldest_index = None

    def append(self, item):
        # what if the queue is UNDER capacity?
        if len(self.queue) < self.capacity:
            # if this is the first item to be added,
            # set oldest to this item if it's the first
            if len(self.queue) == 0:
                self.oldest_index = 0
            else:
                self.oldest_index +=1
            # append the item
            self.queue.append(item)
            
        # what if the queue is AT capacity?
        else:
            # update the oldest index
            
            # if the index was at the last item in
            # the array, move index to the front
            if self.oldest_index == self.capacity-1:
                self.oldest_index = 0
            # otherwise, just increment the oldest
            # index to the next item to the right
            else:
                self.oldest_index +=1
                
            # replace item at oldest index
            self.queue[self.oldest_index] = item
            

    def get(self):
        return self.queue
    