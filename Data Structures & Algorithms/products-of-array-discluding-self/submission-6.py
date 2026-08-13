class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod,zero= 1,0
        result=[0]*len(nums)

        for num in nums:
            if num:
                prod=prod*num
            else:
                zero=zero+1
            
        if zero>1: return result

        for i,c in enumerate(nums):
            if zero==1:
                if c==0: result[i] = prod
                else: result[i] = 0
            else:
                result[i]= prod//c
        return result


        




        