class Solution:
    def interpret(self, command: str) -> str:
        temp=""
        result=""
        d = {"G":"G","()":"o","(al)":"al"}
        for i in range(len(command)):
            temp += command[i]
            if temp in d:
                result += d[temp]
                temp=""
        return result        