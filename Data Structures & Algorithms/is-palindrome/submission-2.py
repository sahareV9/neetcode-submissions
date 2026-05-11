class Solution:
    def isPalindrome(self, s: str) -> bool:
        input_string = re.sub(r'[^a-zA-Z0-9\s]', '', s).lower().replace(" ","");
        isPalandrome = True;
        i = 0;
        j = len(input_string) - 1;
        while j >= 0:
            if input_string[i] != input_string[j]:
                isPalandrome = False;
            j -= 1;
            i += 1;    
        return isPalandrome;