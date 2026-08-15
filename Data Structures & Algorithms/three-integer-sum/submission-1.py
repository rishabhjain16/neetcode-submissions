class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums)):
            seen = set()
            for j in range(i+1,len(nums)):
                target = -(nums[i]+nums[j])
                if target in seen: 
                    result.add((nums[i],target,nums[j]))
                seen.add(nums[j])
        return [i for i in result]