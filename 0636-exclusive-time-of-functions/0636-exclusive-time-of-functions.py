class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev = 0
        for i in logs:
            Id, func, time = i.split(":")

            Id = int(Id)
            time = int(time)

            if func == "start":
                if stack:
                    top = stack[-1]
                    res[top] += time-prev
                stack.append(Id)
                prev = time                
            else:
                top = stack.pop()
                res[top] += time-prev+1
                prev = time+1
        return res