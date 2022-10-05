 #LeetCode
# Definition for singly-linked list.
from requests import head


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        index_to_delete = self.length(head)-n
        
        if index_to_delete==0:
            temp= head.next
            head.next = None
            head = temp
            return head
        temp = head
        for i in range(index_to_delete):
            
            if (i ==index_to_delete-1):
                temp.next = temp.next.next
                break
            temp = temp.next
        return head    
    def length(self,list):
        num = 0
        while (True):
            if list.next == None:
                num+=1
                break
            num+=1
            list = list.next
        return num

#Testing Purpose Not important for leetcode
ListNodeObj = ListNode(1)
ListNodeObj.next = ListNode(2) 
ListNodeObj.next.next = ListNode(3)    
ListNodeObj.next.next.next = ListNode(4)    
ListNodeObj.next.next.next.next = ListNode(5)            

ListNodeObj = Solution().removeNthFromEnd(ListNodeObj,5)

temp = ListNodeObj
while(temp!=None):
    print(temp.val)
    temp = temp.next