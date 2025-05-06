class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxe = releaseTimes[0]
        nmax = 0
        for i in range(1,len(releaseTimes)):
            diff = releaseTimes[i] - releaseTimes[i-1]
            if maxe < diff or ( maxe == diff and keysPressed[i] > keysPressed[nmax]):
                # print(maxe)
                maxe = diff
                # print(maxe)
                nmax = i
        
        return keysPressed[nmax]