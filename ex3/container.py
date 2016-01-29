class ContainerEmptyException(Exception):
    pass
class ContainerFullException(Exception):
    pass
class Bucket():
    ''' Class containing a bucket.
    '''

    def __init__(self):
        self._bucket = ""

    def put (self, item):
        '''(Bucket, str or int) -> NoneType
        puts an item in the bucket
        '''
        self._bucket = item

    def get(self):
        '''(Bucket) -> NoneType
        removes and returns an item from the the bucket
        '''
        temp = self._bucket
        self._bucket = ""
        return temp

    def is_empty(self):
        '''(Bucket) -> NoneType
        Checks if the bucket is empty
        '''
        if len(self._bucket) == 0:
            return True
        return False

class Stack():
    '''Class representing a stack
    '''

    def __init__ (self):
        self._rep = []

    def put(self, item):
        self._rep.append(item)

    def get(self):
        if self.is_empty():
            raise ContainerEmptyException
        else:
            return self._rep.pop()

    def is_empty(self):
       return (len(self._rep)==0)

class Queue(Stack):
    '''Class representing a queue
    '''
    def get(self):
        if self.is_empty():
            raise ContainerEmptyException
        else:
            return self._rep.pop(0)

