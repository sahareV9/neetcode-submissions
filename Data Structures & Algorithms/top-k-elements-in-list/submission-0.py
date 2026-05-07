class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = nums;
        new_temp = [];
        counter = {};
        key = 0;
        count = 0;
        for num in nums:
            for val in temp:
                if num == val:
                    count += 1;
                    if count == 1:
                        key = val;
                else:
                    new_temp.append(val);
            if count >= 1:
                counter[key] = count;
            temp = new_temp;
            new_temp = [];
            count = 0;
        frequent_element = sorted(counter, key = counter.get, reverse=True)[:k];
        return frequent_element;
        