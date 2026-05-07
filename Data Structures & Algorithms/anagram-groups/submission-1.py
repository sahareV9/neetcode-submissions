class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = strs;
        sublist = [];
        result = [];
        new_temp = [];
        for str in strs:
            for val in temp:
                if "".join(sorted(str)) == "".join(sorted(val)):
                    sublist.append(val);
                else:
                    new_temp.append(val);
            temp = new_temp;
            new_temp = [];
            if sublist != []:
                result.append(sublist);
            sublist = [];
        return result;
