class Node():
    def __init__(self, x):
        self.data = x
        self.next = None


class Linklist:
    def __init__(self):
        self.head = Node(None)

    def initList(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def deleteNode(self, index):
        node = self.head
        if index == 0:
            self.head = self.head.next.next
        else:
            while index - 1:
                node = node.next
                index -= 1
            node.next = node.next.next

    def get(self, index):
        node = self.head
        for i in range(index):
            if node.next is not None:
                node = node.next
        return node.data

    def printList(self):
        p = self.head
        while p:
            print(p.data, end='->')
            p = p.next


if __name__ == '__main__':
    data = [1, 2, 3, 4]
    l = Linklist()
    l.initList(data)
    print("删除节点前：\n")
    l.printList()
    print("\n")
    print(l.get(2))
    l.deleteNode(1)
    print("删除节点后：\n")
    l.printList()
