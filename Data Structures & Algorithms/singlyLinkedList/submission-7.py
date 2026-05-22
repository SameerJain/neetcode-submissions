class listNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = listNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        curr = listNode(val)
        curr.next = self.head.next
        self.head.next = curr
        if not curr.next:
            self.tail = curr

    def insertTail(self, val: int) -> None:
        self.tail.next = listNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index and curr:
            i+=1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False 

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next 
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
