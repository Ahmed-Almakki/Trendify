class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        curr = Node(value)
        if self.head is None:
            self.head = curr
            self.tail = self.head
        else:
            self.tail.next = curr
            self.tail = curr
        self.length += 1

    def __str__(self):
        curr = self.head
        lst = []
        while curr:
            lst.append(str(curr.value))
            curr = curr.next
        return '->'.join(lst)



lst = LinkedList()
lst.append(4)
lst.append(5)
print(lst)