class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        l = len(nums)
        while i<l:
            if nums[i] == val:
                nums.remove(nums[i])
                l -=1
                continue
            i += 1
        
        return len(nums)
