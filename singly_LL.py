class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_beg(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_end(self, data):
        node = Node(data)
        if not self.head: # empty linked list
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def insert_pos(self, data, pos):
        if pos == 0:
            self.insert_beg(data)
        else:
            count = 0
            curr = self.head
            try:
                while count < pos:
                    if count == pos-1:
                        right_node = curr.next
                        node = Node(data)
                        curr.next = node
                        node.next = right_node
                        break
                    curr = curr.next
                    count += 1
            except Exception as e:
                """if empty linked list and pos=0 previous if-block is executed"""
                print("Position for Linked List's node out of bounds!", e)

    def del_beg(self):
        if not self.head: # empty linked list
            print("Linked list empty to delete")
            return
        curr = self.head
        self.head = curr.next
        curr = None

    def del_end(self):
        if not self.head: # empty linked list
            print("Linked list empty to delete")
        elif not self.head.next: # if only one node in the linked list
            self.del_beg()
        else:
            prev = self.head
            curr = self.head
            while curr.next:
                prev = curr
                curr = curr.next
            # print("here")
            curr = None
            prev.next = None

    def del_pos(self, pos):
        if not self.head: # empty linked list
            print("Linked list empty to delete")
        elif pos == 0: # if first position to delete
            self.del_beg()
        else:
            prev = self.head
            curr = self.head
            count = 0
            try:
                while count < pos:
                    prev = curr
                    curr = curr.next
                    if count == pos-1:
                        prev.next = curr.next
                        curr = None
                        break
                    count += 1
            except Exception as e:
                print("Position for Linked List's node out of bounds!", e)

    def display(self):
        if not self.head:
            print("Empty")
        else:
            curr = self.head
            while curr:
                print(curr.data, "-> ", end="")
                curr = curr.next
            print()

if __name__ == "__main__":
    ll1 = SinglyLinkedList()
    ll1.insert_beg(1)
    ll1.insert_pos(0, 0)
    ll1.insert_end(2)
    ll1.display()
    ll1.del_beg()
    ll1.display()
    ll1.del_end()
    ll1.display()
    ll1.del_pos(0)
    ll1.display()
                    