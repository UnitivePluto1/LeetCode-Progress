class Solution:
    def frequencySort(self, s: str) -> str:
        chars = [char for char in s]

        counter = Counter(chars)

        heap = []

        for c, f in counter.items():
            heapq.heappush(heap, [f, c])
        res = ""

        while heap:
            res = res + str(heap[0][0]*heap[0][1])
            heapq.heappop(heap)

        return res[::-1]
