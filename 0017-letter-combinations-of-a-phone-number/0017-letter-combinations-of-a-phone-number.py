class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        alpha = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
        }
        
        def back(i,cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for c in alpha[digits[i]]:
                back(i+1,cur+c)
        if digits:
            back(0,"")
        return res
