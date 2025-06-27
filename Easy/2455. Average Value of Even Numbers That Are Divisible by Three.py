class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer=0
        count=0
        for i in nums:
            if i % 6 == 0:
                answer+=i
                count+=1

        if count == 0:
            return 0
        else:
            return answer/count  


        