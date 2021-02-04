# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


from collections import deque


class Solution(object):
    """
    https://leetcode-cn.com/problems/mini-parser/
    给定一个用字符串表示的整数的嵌套列表，实现一个解析它的语法分析器。
    列表中的每个元素只可能是整数或整数嵌套列表
    提示：你可以假定这些字符串都是格式良好的：
    字符串非空|字符串不包含空格|字符串只包含数字0-9、[、-、,、]

    给定 s = "[123,[456,[789]]]",
    返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
    1. 一个 integer 包含值 123
    2. 一个包含两个元素的嵌套列表：
        i.  一个 integer 包含值 456
        ii. 一个包含一个元素的嵌套列表
             a. 一个 integer 包含值 789
    """

    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        def dfs(elem):
            if type(elem) == int:
                return NestedInteger(elem)
            li = NestedInteger()  # 这个对象为空时是一个空列表
            for i in elem:
                li.add(dfs(i))
            return li

        return dfs(eval(s))

        # empty123 = NestedInteger()  # 空列表
        # num123 = NestedInteger(123)
        # empty123.add(num123)
        #
        # empty456 = NestedInteger()  # 空列表
        # num456 = NestedInteger(456)
        # empty456.add(num456)
        #
        # empty123.add(empty456)
        #
        # return empty123


if __name__ == '__main__':
    strs = "[123,[456,[789]]]"
    solution = Solution()
    solution.deserialize(strs)
