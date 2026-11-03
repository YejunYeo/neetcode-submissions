class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_ver = list(s)
        arr = []
        for i in range (len(list_ver)):
            if not (list_ver[i].isalpha() or list_ver[i].isnumeric()):
                continue
            arr.append(list_ver[i].lower())

        if arr[::-1] == arr:
            return True
        else:
            return False

