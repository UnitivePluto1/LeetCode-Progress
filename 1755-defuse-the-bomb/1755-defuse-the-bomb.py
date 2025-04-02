class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        #[1, 1, 1, 1]
        temp = 0
        tempArr = [0 for i in range(len(code))]
        if k == 0:
            return tempArr
        elif k > 0:
            ind = 0 
            while ind<len(code):
                
                for i in range(ind+1,ind + k+1):
                    tempArr[ind] += code[i%len(code)]
                ind+=1
        elif k < 0:
            ind = len(code) - 1
            while ind > -1:
                
                for i in range(ind-1, ind - abs(k) - 1, -1):
                    tempArr[ind] += code[i%len(code)]
                ind -= 1
        return tempArr