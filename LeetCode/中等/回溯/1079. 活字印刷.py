class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        https://leetcode-cn.com/problems/letter-tile-possibilities/
        :type tiles: str
        :rtype: int
        你有一套活字字模tiles，其中每个字模上都刻有一个字母tiles[i]。返回你可以印出的非空字母序列的数目。
        注意：本题中，每个活字字模只能使用一次。
        示例 1：输入："AAB"   输出：8
        解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
        """
        res = 0
        if not tiles: return res
        length, tiles = len(tiles), sorted(tiles)

        def backtrack(used):
            nonlocal res

            for i in range(length):
                if used[i]:
                    continue
                # tiles[i] == tiles[i - 1] 同一层有重复
                # used[i - 1] 同一树枝的元素是否使用过
                # used[i - 1] == True，说明同一树支tiles[i - 1]使用过
                # used[i - 1] == False 说明同一树层tiles[i - 1]使用过
                #同一层前一个元素与当前元素相同，且，前一个元素使用过
                if i > 0 and tiles[i] == tiles[i - 1] and used[i - 1] == False:
                    continue
                used[i] = True
                res += 1
                backtrack(used)
                used[i] = False

        backtrack([False] * length)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.numTilePossibilities('AAABBC'))
