class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = []
        for n in nums1:
            new_arr.append(n)
        for n in nums2:
            new_arr.append(n)
        x = sorted(new_arr)
        l = len(x)
        mid = l//2
        if l%2 == 1:
            return x[mid]
        else: 
            return (x[mid-1]+x[mid])/2

        