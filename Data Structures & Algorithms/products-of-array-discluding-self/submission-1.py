class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [];
        product = 1;
        for i in range(0,len(nums)):
            j=0;
            while j < len(nums):
                if j != i:
                    product *= nums[j];
                j += 1;
            result.append(product);
            product = 1;
        return result;
        