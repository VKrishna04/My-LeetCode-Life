class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            if i == 0:
                diff = arr[1] - arr[0]
            if (i != 0) and (i != len(arr)-1):
                if arr[i] - arr[i-1] != arr[i+1] - arr[i] != diff:
                    return False
        return True