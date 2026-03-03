class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        closest= []

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            if len(closest) < k:
                heapq.heappush(closest, [-dist,point])
            elif -dist > closest[0][0]:
                heapq.heappop(closest)
                heapq.heappush(closest, [-dist, point])
        
        ret = []
        #faster because o(1) to traverse through closest once
        for dist, point in closest:
            ret.append(point)
        return ret

        # this is slower since each pop uses o(log n) time.
        # return [heapq.heappop(closest)[1] for i in range(k)]