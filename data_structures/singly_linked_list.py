# super simple singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def __repr__(self):
        return f"Node({self.data})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        return len(tuple(iter(self)))

    def __repr__(self):
        return "->".join([str(item) for item in self])

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise ValueError("index out of range")
        for i, node in enumerate(self):
            if i == index:
                return node

    def insert(self, data):
        new_node = Node(data=data)
        new_node.set_next(self.head)
        self.head = new_node


def tester():
    linked_list = SinglyLinkedList()
    linked_list.insert("node1")
    linked_list.insert("node2")
    linked_list.insert("node3")
    node = Node(data="test")
    print(repr(linked_list))
    print(len(linked_list))
    print(linked_list[1])
    print(repr(node))

    '''
    OUTPUT:
    
    print(repr(linked_list)):   node3->node2->node1
    print(len(linked_list)):    3
    print(linked_list[1]):      node2
    print(repr(node)):          Node(test)
    '''


if __name__ == '__main__':
    tester()
