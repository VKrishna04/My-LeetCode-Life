class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n = str(bin(n))[2:]
        # print(n)
    
        # if n[0] != '1':
        #     return False
        
        # for i in range(1,len(n)):
        #     if n[i] != '0':
        #         return False
        # return True

        return n > 0 and str(bin(n)).count('1') == 1