class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         for j in range(i, len(nums) - i -1):
        #             nums[j] = nums[j+1]

        # nums = [n for n in nums if n != val]

        while val in nums:
            nums.remove(val)
        
        return len(nums)