class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for n in nums1:
            if n not in d:
                d[n] = True
        out = []
        for n in nums2:
            if n in d and d[n]:
                d[n] = False
                out.append(n)
        return out