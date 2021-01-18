from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        https://leetcode-cn.com/problems/uncommon-words-from-two-sentences/
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        res = (A+' '+B).split()
        li,dicts=[],Counter(res)
        for k in dicts.keys():
            if dicts[k]>1:continue
            li.append(k)
        return li

        print()

if __name__ == '__main__':
    solution=Solution()
    solution.uncommonFromSentences('this apple is sweet','this apple is sour')