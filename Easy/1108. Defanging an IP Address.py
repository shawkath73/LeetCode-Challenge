class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        output=""
        for i in range(0,len(address)):
            if address[i] == '.':
                output+='[.]'
            else:
                output+=address[i]
        return output 

        """
        //Another solution
        return address.replace('.', '[.]')
        """           