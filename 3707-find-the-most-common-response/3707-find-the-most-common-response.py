from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        ans = []
        for i in responses:
            ans.extend(set(i))
        # print(ans)
        count = Counter(ans)
        # print(count)
        a = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        # print(a)
        return a[0][0]