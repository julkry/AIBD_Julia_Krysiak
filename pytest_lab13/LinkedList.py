# skonczone
class LinkedList:
    def __init__(self):
        self.head = None

    def DestroyList(self):
        self.head = None

    def __str__(self):
        temp = self.head
        output = ''
        while temp:
            for el in temp.data:
                output += f'{el}, '
            output += '\n'
            temp = temp.next
        return output

    def AddAtStart(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def AddAtEnd(self, new_node):
        temp = self.head
        if self.head is not None:
            while temp.next:
                temp = temp.next

            temp.next = new_node
        else:
            self.head = new_node

    def RemoveAtEnd(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next:
                    temp = temp.next
                temp.next = None

    def RemoveAtStart(self):
        self.head = self.head.next

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        temp = self.head
        sum = 0
        while temp:
            sum += 1
            temp = temp.next
        return sum

    def GetFirst(self):
        return self.head.data

    def GetElement(self, n: int):
        if isinstance(n, int) and n <= self.length():
            temp = self.head
            for i in range(n - 1):
                temp = temp.next
            return temp.data
        else:
            raise Exception("wrong value of n")

    def drop(self, n):
        new_list = LinkedList()
        if n < self.length():
            el = 0
            for i in range(self.length()):
                if el < n:
                    el += 1
                else:
                    node = Node(self.GetElement(i + 1))
                    new_list.AddAtEnd(node)
        return new_list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


def create_LinkedList():
    linked_list = LinkedList()
    return linked_list


def create_Node(data):
    node = Node(data)
    return node


def get_LinkedList(linked_list):
    temp = linked_list.head
    output = ''
    while temp:
        for el in temp.data:
            output += f'{el}, '
        output += '\n'
        temp = temp.next
    return output


def main():
    pass


if __name__ == "__main__":
    main()
