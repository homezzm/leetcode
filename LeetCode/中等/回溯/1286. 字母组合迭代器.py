from collections import deque


class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.q = deque()

        def backtrack(startInx, paths):
            if len(paths) == combinationLength:
                self.q.append(''.join(paths))
                return

            for i in range(startInx, len(characters)):
                paths.append(characters[i])
                backtrack(i + 1, paths)
                paths.pop()

        backtrack(0, [])

    def next(self):
        """
        题目保证每次调用函数 next 时都存在下一个字母组合。
        :rtype: str
        """
        return self.q.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator("abc", 2)
param_1 = obj.next()
param_2 = obj.hasNext()
