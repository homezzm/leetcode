import random
from cal_time import *


# 基数排序
@cal_time
def radix_sort(li):
    # 确定循环的最大值，就是找到列表中的最大值
    max_num = max(li)
    # 以此来确定需要循环几次 比如列表中有20 200 2000最大值是2千就是要做4次
    # 最大值9->,99->,888->3,10000->5
    it = 0  # 循环几次
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]  # 分10个桶
        for var in li:  # 把元素放到对应的桶里
            # 要先确定把这个数放到几号桶内
            # 分到几号桶里是取决于当前是哪一位数 it=0个位 it=1十位 it=2百位 it=3千位
            # 写算法时不知道该怎么得到某值时，就举个例子
            # it=0[987%10=7(取到个位)] it=0是10的0次方=0
            # it=1[987//10=98 98%10=8(取到十位)] it=1是10的1次方=10
            # it=2[987//100=9 9%10=9(取到百位)] it=2是10的2次方=100
            # var是数 it=0是10的0次方
            digit = (var // 10 ** it) % 10
            # 把对应的数放到对应的桶里 分桶完成
            buckets[digit].append(var)
        li.clear()  # 清空源来的列表
        for buc in buckets:  # 把桶里数拿出来
            li.extend(buc)  # 把桶里的数重新写回li，已排好序
        it += 1


if __name__ == '__main__':
    li = list(range(1000))
    random.shuffle(li)
    radix_sort(li)
    print(li)
