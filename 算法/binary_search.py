from cal_time import *


# 二分查找法
@cal_time
def binary_search(li, val):  # 输入【列表】【要查找的元素】 #返回的是下标这个方法
    li.sort()  # 排序
    left, right = 0, len(li) - 1  # 用L与R两个变量来维护候选区。初始时L=(下标)0，R=n-1(列表长度-1，也是下标值)
    while left <= right:  # 当L<=R的时候候选区是有值的
        mid = (left + right) // 2  # 中间值M是L与R指向的下标相加整除2 ==>M=（L+R）/2=（0+8）/2=4（下标）   下标为4的实际值为5
        if li[mid] == val:  # M与3进行比较，发现相等，算法终止
            return mid
        elif li[mid] > val:  # M与3进行比较，发现5比3大，说明候选区在左侧（移动R） 这里要更新R的值R=M-1 => R=4-1 => 3（下标），移动候选区
            right = mid - 1
        else:  # M与3进行比较，发现2比3小，说明候选区在右侧（移动L），这里要更新L的值L=M+1 => L=1+1 => 2（下标）
            left = mid + 1
    else:
        return None  # 但如果L>R候选区没有值，说明找不到这个值，结束


if __name__ == '__main__':
    print(binary_search([3, 6, 9, 5, 1, 2, 8, 4, 7], 3))
