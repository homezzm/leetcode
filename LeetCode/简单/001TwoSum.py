# nums = [2, 7, 11, 15], target = 9
def two_sum(nums, target):
    dict = {}
    li = []
    for inx, val in enumerate(nums):
        v = target - val
        if dict.__contains__(v):
            li.append(dict[v])
            li.append(inx)
            break
        else:
            dict[val] = inx
    print(li)


if __name__ == '__main__':
    two_sum([2, 7, 11, 15], 9)
