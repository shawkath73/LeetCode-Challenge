class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        #USING AN OPTIMIZED APPROACH
        lcount = moves.count('L')
        rcount = moves.count('R')
        ucount = moves.count('_')  
        return max(lcount-rcount+ucount,rcount-lcount+ucount) 

        """
        USING A BRUTE-FORCE APPROACH

        lmove=0
        rmove=0
        flex_move=0
        for i in moves:
            if i == "L":
                lmove+=1
            elif i == "R":
                rmove+=1
            elif i == "_":
                flex_move+=1
        fright=rmove-lmove+flex_move
        fleft=lmove-rmove+flex_move       
        return max(fright,fleft)  
        """
                       