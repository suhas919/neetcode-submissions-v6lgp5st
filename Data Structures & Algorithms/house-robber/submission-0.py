from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0 for _ in range(len(nums))]

        @cache
        def result(i):

            if i > len(nums)  -1:
                return 0

            else:

                return max(nums[i] + result(i+2), nums[i]+result(i+3))

        return max(result(0), result(1))