from cal_time import *
import random


# 桶排序
@cal_time
def bucket_sort(li, n=100, max_num=10000):
    """
    就是把列表中的数分成100个桶，且最大数是10000
    但如果我不知道数的最大范围，又要用桶排序来操作
    可以自己规定一个最大数，超过这个最大数就把剩余的数都放到最后一个桶里
    :param li: 列表
    :param n: 默认分成多少桶
    :param max_num: 数的范围
    :return:
    """

    # 创建了n个空桶
    buckets = [[] for _ in range(n)]  # 一个桶里会有很多个数(列表)，所以定义成二维列表，外层放桶里层放数的列表
    for var in li:  # 遍历列表中的所有数
        # 决定哪个数要放到哪个桶里
        # 现在有1百个桶，1万个数，那就是1个桶放1百个数
        # var // (max_num // n) = 86//100=0(号桶) 186//100=1(号桶)
        # i表示var放到几号桶里，通过整除得到桶号
        # 但有个问题是到了10000这个数时，整除i的值是100号桶，但生成的桶是0-99，这时会出现越界情况
        # 为防止越界，在外面又套了一层min()函数，正常情况下会返回var // (max_num // n)这个的结果
        # 如果i变成了100号桶里，就会返回n-1=99(号桶)，这样就不会越界了
        i = min(var // (max_num // n), n - 1)
        # 把var放到对应的桶里
        buckets[i].append(var)
        # 其实到这里就已经可以结束循环了，接下来就是对桶里的数进行排序
        # 但可以选择另外的一种方式，就是放到桶里的过程中顺便就把序给排了
        # 假设现在桶里有[0,2,4]我已经让他有序了，这时又插入了个3变成[0,2,4,3]
        # 可以使用个小冒泡把3与前面的数进行对比，遇到比它大的我就交换下，遇到比它小的就停止
        for j in range(len(buckets[i]) - 1, 0, -1):  # [0,2,4,3]倒着走到2的位置
            # buckets[i]就是当前插入的那个桶
            if buckets[i][j] < buckets[i][j - 1]:  # [0,2,4,3] 如果3比4小，交换
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:  # 后面的数比前面的数大，表示当前数已经插入到正确的位置上了，结束即可
                break

    # 到这里，所有数都已进入了对应的桶且都已排好序，直接输出即可
    sorted_li = []
    for buc in buckets:
        # buc就是每个桶，把桶里的数追加到列表中即可
        sorted_li.extend(buc)
    return sorted_li


if __name__ == '__main__':
    li = [random.randint(0, 10000) for i in range(10000)]
    #print(li)
    li = bucket_sort(li)
    print(li)
