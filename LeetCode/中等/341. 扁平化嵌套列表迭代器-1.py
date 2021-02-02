# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque


class NestedIterator(object):
    """
    https://leetcode-cn.com/problems/flatten-nested-list-iterator/
    给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
    列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
    输入: [[1,1],2,[1,1]]
    输出: [1,1,2,1,1]
    解释: 通过重复调用next 直到hasNext 返回 false，next返回的元素的顺序应该是: [1,1,2,1,1]。
    其实就是多叉树的遍历
    如果现在数据量非常多，那会严重影响性能，我们可以控制.hasNext()方法，让它变成有惰性的，参考的 拉不拉东
    """

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.q = deque()
        for li in nestedList: #先把所有的都放到队列中，然后在hasNext方法中依次展开
            self.q.append(li)

    def next(self):
        """
        :rtype: int
        """
        return self.q.popleft().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.q and self.q[0].isInteger() == False:
            tempLi = self.q.popleft().getList()  # 队列中第一个是列表，把他弹出并展开在放到队列里
            for i in tempLi[::-1]: #倒序放
                self.q.appendleft(i) #从队列头倒着放
        return len(self.q) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
# i = 10
# print(type(i) == int)

    i, v = NestedIterator([[1,2], 3, [4, 5]]), []
    while i.hasNext():
        v.append(i.next())

    print(v)
