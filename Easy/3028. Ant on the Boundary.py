class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos=0
        count=0
        for i in nums:
            pos+=i
            if pos == 0:
                count+=1
        return count      

        