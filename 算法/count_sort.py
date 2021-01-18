# 计数排序
from cal_time import *
import random

@cal_time
def count_sort(li, max_count=100):  #时间复杂度O(n)
    count = [0 for _ in range(max_count + 1)]  # 生成计数容器
    for val in li:
        count[val] += 1  # 在count列表相同的下标处加1

    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)  # 写到原来的列表中

if __name__ == '__main__':
    li=[random.randint(0,100) for _ in range(1000)]
    print(li)
    count_sort(li)
    print(li)

