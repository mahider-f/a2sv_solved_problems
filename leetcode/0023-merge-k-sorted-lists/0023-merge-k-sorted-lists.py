# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        min_heap = []
        counter = 0 
        
        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, counter, node))
                counter += 1
                
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            val, _, smallest = heapq.heappop(min_heap)
            current.next = smallest
            current = current.next
            
            if smallest.next:
                heapq.heappush(min_heap, (smallest.next.val, counter, smallest.next))
                counter += 1
                
        return dummy.next
