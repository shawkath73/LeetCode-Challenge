class Solution:
    def hammingWeight(self, n: int) -> int:
        #n=bin(n)
        #return n.count("1")

        #using Bit-wise operator
        count=0
        while n != 0:
            n = n & n-1
            count+=1
        return count    