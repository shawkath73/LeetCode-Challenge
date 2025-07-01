class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        :for i in range(0,len(nums)):
            :for j in range(1,len(nums)):
               :if nums[i] + nums[j] == target:
                    :return [i,j]
                    """
        number_map={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in number_map:
                return [number_map[diff],i]            
            number_map[num]=i
                
        