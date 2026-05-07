class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "";
        for str in strs:
            encoded_string += str + "__";
        return encoded_string;

    def decode(self, s: str) -> List[str]:
        decoded_list = [];
        temp = "";
        count = 0;
        for char in s:
            if char == "_":
                count += 1;
                if count == 2:
                    decoded_list.append(temp);
                    temp = "";
                    count = 0;
            else:
                if count > 0:
                    temp = temp + "_";
                count = 0;
                temp = temp + char;
        return decoded_list;