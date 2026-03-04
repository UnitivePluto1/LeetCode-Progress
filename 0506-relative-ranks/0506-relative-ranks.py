class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        pos = 0

        for i,v in enumerate(score):
            heap.append([-v,i])
        heapq.heapify(heap)


        n=len(score)
        for i in range(n):
            temp_ind = heapq.heappop(heap)[1]
            if pos == 0:
                score[temp_ind] = "Gold Medal"
            elif pos == 1:
                score[temp_ind] = "Silver Medal"
            elif pos == 2:
                score[temp_ind] = "Bronze Medal"
            else:
                score[temp_ind] = str(pos+1)
            pos+=1
        return score


