class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a,b = n-1,1
        while "0" in str(a) or "0" in str(b):
            a-=1
            b+=1
        return [a,b]
        '''for i in range(1,n):
            a,b = i,n-i
            if "0" not in str(a) and "0" not in str(b):
                return [a,b]''' 