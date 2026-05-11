class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums));
        length_of_list = len(sorted_nums);
        if nums == []:
            return 0;
        elif length_of_list == 1:
            return 1;
        output = 1;
        sequence = [];
        prev_count = 0;
        for i in range(0, length_of_list):
            j = 0;
            count = 0;
            temp_sequence = [];
            val = sorted_nums[i];
            while j < length_of_list:
                if sorted_nums[j] == val + 1:
                    if count == 0:
                        temp_sequence.append(sorted_nums[i]);
                        temp_sequence.append(sorted_nums[j]);
                        count += 2;

                    else:
                        temp_sequence.append(sorted_nums[j]);
                        count += 1;
                    val = sorted_nums[j];
                    j = 0;
                    continue
                j += 1;
            if prev_count < count:
                sequence = [];
                sequence = temp_sequence;
                temp_sequence = [];
                prev_count = count;
                count = 0;
        if len(sequence) == 0 :
            return 1;
        else:
            return len(sequence);
        