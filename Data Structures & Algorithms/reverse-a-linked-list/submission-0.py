# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newList = []
        cur = head
        while cur:
            newList.append(cur)
            cur = cur.next
        for i in range(len(newList) - 1, 0, -1):
            newList[i].next = newList[i - 1]
        newList[0].next = None
        return newList[-1]

# Time: O(n + m)
# Space: O(n)
