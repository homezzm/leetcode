from cal_time import *


# 顺序查找
@cal_time
def linear_search(li, val):  # 输入：列表、待查找的元素
    for inx, v in enumerate(li):
        if v == val:
            return inx
    else:
        None


# 1.首先找n，这里的n就是li列表的长度（列表的规模）
# 2.是否有循环减半的过程？这里没有
# 3.是否有一个与n相关的循环？是的，有一个
# 4.所以当前算法的时间复杂度为O(n)
# 注释，顺序查找就是把列表从头到尾走一遍，最多走n步
if __name__ == '__main__':
    print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6))
