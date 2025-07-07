class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        a = [0]*26

        for task in tasks:
            a[ord(task) - ord('A')] += 1
        a.sort()
        chunk = a[25]-1
        idle = n*chunk

        for i in range(24,-1,-1):
            idle -= min(chunk, a[i])
        return len(tasks) + idle if idle >=0 else len(tasks)