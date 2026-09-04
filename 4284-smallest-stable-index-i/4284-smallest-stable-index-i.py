class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            maxi=max(nums[:i+1])
            mini=min(nums[i:])
            if (maxi-mini) <= k:
                return i
        return -1