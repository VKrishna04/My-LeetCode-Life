class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # new = [[0], [1], [0]]
        
        # for i in range(numRows):
        #     new.append(list(new[i-1] + new[i]) for i in range(len(new)))
        
        
        if numRows == 1:
            return [[1]]
        
        prev = self.generate(numRows-1)
        pre = prev[-1]
        cur = [1]

        for i in range(1, numRows-1):
            cur.append(pre[i-1] + pre[i])
        
        cur.append(1)
        prev.append(cur)

        return prev


        return ans

