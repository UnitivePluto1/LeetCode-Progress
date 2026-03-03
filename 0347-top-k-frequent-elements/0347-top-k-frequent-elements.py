class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        counter = Counter(nums)
        heap = []
        for n, c in counter.items():
            heapq.heappush(heap, [c, n])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        while heap:
            res.append(heapq.heappop(heap)[1])
        return res

        