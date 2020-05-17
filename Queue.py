class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]

    def en_queue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def de_queue(self):
        return self.storage.pop(0)


# Setup
q = Queue(1)
q.en_queue(2)
q.en_queue(3)

# Test peek
# Should be 1
print(q.peek())

# Test de_queue
# Should be 1
print(q.de_queue())

# Test enqueue
q.en_queue(4)
# Should be 2
print(q.de_queue())
# Should be 3
print(q.de_queue())
# Should be 4
print(q.de_queue())
q.en_queue(5)
# Should be 5
print(q.peek())
