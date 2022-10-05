# LeetCode - Easy
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1Curr = list1
        l2Curr = list2
        mergeList = ListNode()
        while (True):
            if(l1Curr==None and l2Curr==None):
                break;
            if (l1Curr==None):
                if(mergeList.val==0):
                    mergeList.val = l2Curr.val
                else:    
                    mergeList.next = l2Curr
                l2Curr=l2Curr.next
                continue
            if (l2Curr==None):
                mergeList.next = l1Curr
                l1Curr=l1Curr.next
                continue
            

            if (l1Curr.val>l2Curr.val):
                if (mergeList.val==0):
                    mergeList.val = l2Curr.val
                    mergeList.next = l1Curr
                else:
                    mergeList.next = l2Curr
                    mergeList = mergeList.next
                    mergeList.next = l1Curr
                l1Curr = l1Curr.next
                l2Curr =l2Curr.next
            else:
                if (mergeList.val==0):
                    mergeList.val = l1Curr.val
                    mergeList.next = l2Curr
                else:
                    mergeList.next = l1Curr
                    mergeList = mergeList.next
                    mergeList.next = l2Curr
                l1Curr = l1Curr.next
                l2Curr =l2Curr.next            
        return mergeList        




#Testing Purposes not important for leetcode
def printList(ListNodeObj):
    temp = ListNodeObj
    while(temp!=None):
        print(temp.val)
        temp = temp.next

                        
ListNodeObj = ListNode(1)
ListNodeObj.next = ListNode(2) 
ListNodeObj.next.next = ListNode(3)    
ListNodeObj.next.next.next = ListNode(4)    
ListNodeObj.next.next.next.next = ListNode(5)   
ListNodeObj1 = ListNode(1)
ListNodeObj1.next = ListNode(3) 
ListNodeObj1.next.next = ListNode(3)    
ListNodeObj1.next.next.next = ListNode(4)    
ListNodeObj1.next.next.next.next = ListNode(6)   

lstFinal = Solution().mergeTwoLists(ListNodeObj,ListNodeObj1)

printList(lstFinal)
        