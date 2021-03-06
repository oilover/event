# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common import *


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return
        if not head.next: return TreeNode(head.val)
        s, f = head, head.next
        pre = None
        while f and f.next:
            pre = s
            s, f = s.next, f.next.next
        t = s.next
        s.next = None
        if pre: pre.next = None
        rt = TreeNode(s.val)
        if (s!=head): rt.left = self.sortedListToBST(head)
        rt.right = self.sortedListToBST(t)
        return rt


s = Solution()
p = arrToList([-10,-3,0,5,9])
s.sortedListToBST(p)