from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l, r = 0, 0

        q = deque()
        output = []
        for r in range(len(nums)):

            while q and nums[q[-1]] < nums[r]:
                popped = q.pop()
                print("popped index ",popped)

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                l+=1
                output.append(nums[q[0]])
        return output




            


        