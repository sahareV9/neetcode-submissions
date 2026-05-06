class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        input_length = len(nums);
        input_target = target;
        
        for i in range(0,len(nums)-1):
            j = i+1;
            while(j < len(nums)):
                if nums[i] + nums[j] == input_target:
                    return [i,j]; 
                else:
                    j += 1; 