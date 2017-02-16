""" This solution loops through a linked list by initializing the
counter at 1 and calculating the length of the linked list from there.
While making sure that m is a non-negative integer. """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # insert a new node at the beginning of Linked List.
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def element(ll, m):
        current = ll.head
        count = 1  # index of current node starts here

        while current:
            # if count is equal to m index return current
            if count == m:
                return current.data
            else:
                if m < 1 or not isinstance(m, int):
                    return 'm should be a non-negative integer'
            count += 1
            current = current.next


if __name__ == '__main__':

    ll = LinkedList()
    ll.insert(1)
    ll.insert(10000000)
    ll.insert(456)
    ll.insert(12)
    ll.insert(5648980)

mth = 1
print ll.element(mth)

mth = 2
print ll.element(mth)

mth = 89438
print ll.element(mth)

mth = 4
print ll.element(mth)

mth = 'a'
print ll.element(mth)

mth = ''
print ll.element(mth)
