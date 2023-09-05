class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=0
        r=len(nums)-1
        while(l<r):
            if(nums[l]%2 !=0):
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
            else:
                l+=1
        return nums
        