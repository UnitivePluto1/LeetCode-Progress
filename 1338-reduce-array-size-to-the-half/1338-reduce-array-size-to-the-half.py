class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        heap = []
        n = len(arr)
        target = n/2
        for f in freq.values():
            heap.append(-f)
        heapq.heapify(heap)
        
        count = 0
        while n > target:
            freq=heapq.heappop(heap)
            n += freq
            count+=1
        return count