class EmptyQueueException(Exception):
    pass
class Queue():
    class _Node():
        def __init__(self, item, nxt = None):
            self.item = item
            self.nxt = nxt

    def __init__(self, item = None):
        self._head = Queue._Node(item)

    def enque(self, item):
        new_node = Queue._Node(item)
        curr = self._head
        while curr.nxt  != None:
            curr = curr.nxt
        curr.nxt = new_node

    def is_empty(self):
        if self._head.nxt == None and self._head.item == None:
            return True
        return False

    def deque(self):
        if self.isempty():
            raise EmptyQueueException
        new_head = self._head.nxt
        old_head = self._head
        return old_head

