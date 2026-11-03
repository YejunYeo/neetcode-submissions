# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head=[1, 2, 3, 4, 5]
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head


#[Null,1,2,3, NULL]

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev