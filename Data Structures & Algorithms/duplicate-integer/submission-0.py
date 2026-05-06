class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False;
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if(nums[j] == nums[i]):
                    result = True;
                    return result;
        return result;
