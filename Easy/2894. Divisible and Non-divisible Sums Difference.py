class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        '''sum=0
        sum1=0
        for i in range(1,n+1):
            if i%m == 0:
                sum+=i
            elif i%m !=0 :
                sum1+=i
        return sum1-sum '''
        return sum(i for i in range(1,n+1) if i % m != 0) - sum(i for i in range(1,n+1) if i%m == 0)       