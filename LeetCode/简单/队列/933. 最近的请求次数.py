import collections


class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)

if __name__ == '__main__':
    obj = RecentCounter()
    param_1 = obj.ping(3002)
    print(param_1)