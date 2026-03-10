class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        for x in nums2:
            nums1.append(x)
        nums1.sort()

        if len(nums1) % 2 == 0:
            mid1 = (0+len(nums1)-1)//2
            mid2 = (0+len(nums1)+1)//2
            return (nums1[mid1] + nums1[mid2])/2
        else:
            mid = (0+len(nums1)-1)//2
            return nums1[mid]