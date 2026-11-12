class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        raise NotImplementedError("Implement push")

    def pop(self):
        raise NotImplementedError("Implement pop")
