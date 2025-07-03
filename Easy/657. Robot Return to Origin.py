class Solution:
    def judgeCircle(self, moves: str) -> bool:
      #  row=0
      #  col=0
      #  for i in moves:
       #     if i == "U":
        #        col+=1
         #   elif i == "D":
          #      col-=1
           # elif i == "R":
            #    row+=1
           # elif i == "L":
            #    row-=1
       # return (row==0) and (col==0) 
       

       #Better efficiency
       return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")                  
        