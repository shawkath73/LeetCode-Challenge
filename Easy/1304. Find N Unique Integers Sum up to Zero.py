class Solution:
    def sumZero(self, n: int) -> List[int]:
        array = list(range(1,n))
        return array + [-sum(array)]

        #another method
        '''arr = []
        if n % 2 != 0:
            arr.append(0)
        for i in range(1,n//2 +1):
            arr.append(i)
            arr.append(-i)
        return arr'''

        #another method
        '''return list(range(1-n,n,2))'''       