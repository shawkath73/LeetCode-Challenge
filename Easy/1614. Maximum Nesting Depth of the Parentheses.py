class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth=0
        count=0
        for i in s:
            if i == '(':
                count+=1
                if depth < count:
                    depth=count
            if i == ')':
                count-=1 
        return depth           
        