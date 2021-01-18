class Solution(object):
    def removeDuplicates(self, S):
        """
        https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/
        :type S: str
        :rtype: str
        """
        if not S or len(S) == 1: return S

        output=[]   
        for ch in S:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
        return ''.join(output)

        # li = []
        # for i in range(len(S)):
        #     li.append(S[i])
        #     if len(li) > 1 and li[-1]==li[-2]:
        #         li.pop()
        #         li.pop()
        # return ''.join(li)


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates("abbabca"))
