class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # n = len(arr)
        # heap = []
        # for i in range(0,n):
        #     for j in range(i,n):
        #         heapq.heappush(heap, [arr[i]/arr[j],[arr[i],arr[j]]])
        
        # while k>1:
        #     k-=1
        #     heapq.heappop(heap)
        # ans = heapq.heappop(heap)[1]
        # return ans

    # ANSWER
        n = len(arr)

        heap = []

        for j in range(1, n):
            heapq.heappush(heap, (arr[0] / arr[j], 0, j))

        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            if i + 1 < j:
                heapq.heappush(heap, (arr[i + 1] / arr[j], i + 1, j))

        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]
