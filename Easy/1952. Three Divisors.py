class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        root=int(n**0.5)
        return root*root == n and all(root % i for i in range(2,int(root**0.5)+1)) and root > 1 