class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}

        for n in nums2:
            while stack and n > stack[-1]:
                d[stack.pop()] = n
            stack.append(n)
        for n in stack:
            d[n] = -1
        return [d[x] for x in nums1]


        # ans = []
        # count = 0
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):

        #         if (nums1[i] == nums2[j]) :
        #             count = j
        #             break
        #     print(f"count -> {count} | {nums2[count]} ")
        #     a = -1
        #     for j in range(count, len(nums2)):
        #         if nums2[j] > nums2[count]:
        #             print(f"----count -> {count} | {nums2[count]} | {j}")
        #             a = j
            
        #     ans.append(a)
            

            # print(i)
            # for j in range(count, len(nums2)):
            #     print(f"i -> {i} j -> {j}")
            #     if j == len(nums2):
            #         print("==")
            #         j = -1
            #         break
            #     if (nums1[i] <= nums2[j]):
            #         print("<=")
            #         j += 1
            #     if (nums1[i] > nums2[j]):
            #         print(f"{i} {nums1[i]} > found at {j} {nums2[j]}")
            #         ans.append(j)
            #         break
        
        # return ans