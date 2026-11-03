# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head=[1, 2, 3, 4, 5]

       
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead




#At the last call, 5 -> None will be returned

#At the 4th call, reverseList(4), newHead= will be 5 -> none
#ANd it will return 5 -> 4 -> none

#So on and so on




   

               

