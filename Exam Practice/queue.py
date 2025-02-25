# queue.py

class Queue():
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue(self, data):
        if (self.tail == self.size - 1):  # Queue is full
            print("The queue is full")
        else:
            if self.head == -1:  # Set head to 0 when enqueuing the first element
                self.head = 0
            self.tail += 1
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1 or self.head > self.tail:  # Queue is empty
            print("The queue is empty")
            return None
        else:
            temp = self.queue[self.head]
            self.head += 1
            if self.head > self.tail:  # Reset the queue if empty
                self.head = self.tail = -1
            return temp  # Return the dequeued value

    # def printQueue(self):
    #     if self.head == -1:
    #         print("The queue is empty")
    #     else:
    #         for i in range(self.head, self.tail + 1):
    #             print(self.queue[i], end=" ")
    #         print()

custom_queue = Queue(5)

custom_queue.enqueue(5)
custom_queue.enqueue(6)
custom_queue.enqueue(7)
custom_queue.enqueue(8)

custom_queue.dequeue()

print(custom_queue.queue[custom_queue.head:custom_queue.tail+1])