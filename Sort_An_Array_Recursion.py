class Solution:
    def sortArr(self, nums):
        if len(nums) == 1:
            return
        last_elem = nums.pop()
        self.sortArr(nums)
        self.insert(last_elem, nums)

    def insert(self, n, nums):
        if len(nums) == 0 or nums[-1] <= n:
            nums.append(n)
            return
        last_elem = nums.pop()
        self.insert(n, nums)
        nums.append(last_elem)

    def sortArray(self, nums):
        nums_copy = nums.copy()  # Create a copy of the input list
        self.sortArr(nums_copy)
        return nums_copy