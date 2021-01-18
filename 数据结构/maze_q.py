from collections import deque

# 迷宫问题 队列解决
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 方向的函数列表
# x,y四个方向 [上=x-1,y]  [下=x+1,y]  [左=x,y-1]  [右=x,y+1]
dirs = [
    lambda x, y: (x + 1, y),  # 下
    lambda x, y: (x - 1, y),  # 上
    lambda x, y: (x, y - 1),  # 左
    lambda x, y: (x, y + 1)  # 右
]


def print_r(path):
    # path中最后一个元素就是终点，只要从最后一个走到第一个
    # 也就是从终点走到起点就是完整的路径了
    real_path = []  # 保存真实路径
    i = len(path) - 1
    while i >= 0:  # 等于-1就表示到起点了，循环结束，因为路径的第一个元素没有人带进来
        real_path.append(path[i][0:2])
        i = path[i][2]  # 带他进来的那个节点的下标
    real_path.reverse()  # 由于是倒着放进去的，所以要反转下

    for node in real_path:
        print(node)


def maze_path_queue(x1, y1, x2, y2):
    queue = deque()  # 从右边进
    path = []  # 保存是谁带它进来的
    queue.append((x1, y1, -1))  # 起点坐标进队(x坐标,y坐标,谁带进来的)
    while len(queue) > 0:  # 队空了说明没有通路
        # 看下有几个方案能走，把能走的方案全部入队
        curr_node = queue.popleft()  # 从左边出
        path.append(curr_node)  # 把出队的点记录一下
        # 拿到当前节点的时候就要判定下是否已经到达了终点
        if curr_node[0] == x2 and curr_node[1] == y2:
            print_r(path)  # 把路径输出
            return True  # 走通了

        # 看一下四个方向哪一个可以走
        for dir in dirs:
            next_node = dir(curr_node[0], curr_node[1])
            # 看一下下一个坐标是否可以走
            if maze[next_node[0]][next_node[1]] == 0:  # 0是路 1是墙
                # 如果可以走就进队
                # 元组中第三个参数是记录谁带进来的，带next_node进队的是curr_node
                # 所以直接拿curr_node在path列表中对应的下标即可len(path)-1
                queue.append((next_node[0], next_node[1], len(path) - 1))
                maze[next_node[0]][next_node[1]] = 2  # 2表示已经走过了 在地图中标识下

    print("没有路！")
    return False


if __name__ == '__main__':
    maze_path_queue(1, 1, 8, 8)
