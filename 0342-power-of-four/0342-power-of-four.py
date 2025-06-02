class Solution:
    def isPowerOfFour(self, n: int) -> bool:
       
        if n not in [4**i for i in range(int(math.log(2**31,4))+1)]:
            return False
        return True

        # return n>0 and (n & (n-1)==0) and (n % 3 == 1)