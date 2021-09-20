from functools import wraps
from time import sleep


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList():

    def __init__(self, collection=None):
        self.head = None
        self._length = 0
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def traverse(self, action):
        current = self.head
        while current:
            action(current.value)
            current = current.next

    def __iter__(self):
        def generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return generator()

    def __str__(self):
        out = ""
        for value in self:
            out += f"[{value}] -> "
        return out + "None"

    def __len__(self):
        return self._length

    def insert(self, value):
        self.head = Node(value, self.head)
        self._length += 1

    def __getitem__(self, index):
        # loop through the linked list, keeep a counter, whent eh counter  = index return the item
        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError


def proclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return "On this day I do say, " + orig_val

    return wrapper


def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(2)
        return func(*args, **kwargs)

    return wrapper


@procrastinate
@proclaim
def say(txt):
    return txt


if __name__ == "__main__":
    print(say('spam goes best with eggs.'))
