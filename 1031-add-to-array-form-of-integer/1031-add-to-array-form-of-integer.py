class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num[-1] += k
        if len(num) > 1:
            for i in range(len(num)-1,0,-1):
                if num[i] >= 10:
                    num[i-1] += num[i] // 10
                    num[i] = num[i] % 10

        while num[0] >= 10:
            num = [num[0] // 10] + num
            num[1] = num[1] % 10
        return num