# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
        :type head: ListNode
        :rtype: ListNode
        给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
        删除完毕后，请你返回最终结果链表的头节点。
        """
        if not head: return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        dicts, sumVal = dict(), 0

        #若同一和出现多次会覆盖，即记录该sum出现的最后一次节点
        curNode = dummyNode
        while curNode:
            sumVal += curNode.val
            dicts[sumVal] = curNode
            curNode = curNode.next

        #若当前节点处sum在下一处出现了则表明两结点之间所有节点和为0 直接删除区间所有节点
        curNode, sumVal = dummyNode, 0
        while curNode:
            sumVal += curNode.val
            curNode.next = dicts[sumVal].next
            curNode = curNode.next
        return dummyNode.next


if __name__ == '__main__':
    pass
# dicts={1:11,2:22}
# print(k for k, v in dicts.items() if v == 22)

# if 22 in dicts.values():
#    dicts.k
# for inx,val in ll:
#     print(inx,val)
