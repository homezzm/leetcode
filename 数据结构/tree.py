# 简单的文件系统实现
class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type  # dir or file
        # 文件夹相互的关联
        self.children = []  # 子文件夹
        self.parent = None  # 父文件夹 树的结构决定只能有一个父亲

    def __repr__(self):  # tostring()
        return self.name


class FileSystemTree:
    def __init__(self):
        # 文件系统要维护一个根，与链表一样，要维护头部
        # 我把头拎起来，就能拎出一长串数，根拎起来就是一整颗数
        self.root = Node('/')
        self.now = self.root  # 当前目录

    def mkdir(self, name):  # 创建目录
        # 规定name以'/'结尾
        if name[-1] != '/':
            name += '/'
        node = Node(name)  # 创建一个文件夹
        self.now.children.append(node)  # 与当前目录关联起来
        node.parent = self.now  # 关联子目录的父节点

    def cl(self):
        return self.now.children  # 查看当前目录的子目录

    def cd(self, name):  # 切换目录 目前只支持进入一级目录
        # 规定name以'/'结尾
        if name[-1] != '/':
            name += '/'

        if name == '../':  # 返回上一级
            self.now = self.now.parent
            return

        for child in self.now.children:
            if child.name == name:
                self.now = child  # 切换当前目录
                return
        raise ValueError('无效的目录！')


if __name__ == '__main__':
    tree = FileSystemTree()
    tree.mkdir('var/')
    tree.mkdir('bin/')
    tree.mkdir('usr/')

    tree.cd('bin/')  # 去bin目录
    tree.mkdir('python/')
    print(tree.cl())

    tree.cd('../')
    print(tree.cl())
