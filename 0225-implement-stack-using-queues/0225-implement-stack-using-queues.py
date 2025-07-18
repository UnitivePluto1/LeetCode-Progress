class MyStack:

    def __init__(self):
        self.queue1 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)


    def pop(self) -> int:
        self.queue1.reverse()
        pop = self.queue1.popleft()
        self.queue1.reverse()
        return pop

    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()