# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
inititialize a fast and a slow pointer
fast pointer moves by 2, slow moves by 1
if theres a cycle, eventually they will match up 
if theres no cycle, they will terminate and the loop stops 
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_node = head
        fast_node = head
        
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                return True
        return False