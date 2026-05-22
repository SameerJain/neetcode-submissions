class Node:

    def __init__(self,val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        tmp = Node(val)
        tmp.next = self.head.next
        self.head.next = tmp
        if not tmp.next:
            self.tail = tmp

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        tmp = self.head
        i = 0
        while i < index and tmp:
            i+=1
            tmp = tmp.next
        if tmp and tmp.next:
            if tmp.next == self.tail:
                self.tail = tmp
            tmp.next = tmp.next.next

            return True
        return False

    def getValues(self) -> List[int]:
        tmp = self.head.next
        val_list = []
        while tmp:
            val_list.append(tmp.val)
            tmp = tmp.next
        return val_list
