from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]
        
        dp = [0 for _ in range(len(nums))]

        @cache
        def result1(i):

            if i > len(nums1)  -1:
                return 0

            else:

                return max(nums1[i] + result1(i+2), nums1[i]+result1(i+3))

        @cache
        def result2(i):

            if i > len(nums2)  -1:
                return 0

            else:

                return max(nums2[i] + result2(i+2), nums2[i]+result2(i+3))

        return max(result1(0), result1(1), result2(0), result2(1))