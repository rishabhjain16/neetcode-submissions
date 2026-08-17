class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')


        for i in range(len(nums)):
            current = 0
            for j in range(i, len(nums)):
                current += nums[j]
                if current >= target:
                    result = min(result, j-i+1)
                    break
        return 0 if result == float('inf') else result

        