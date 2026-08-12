class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for i in s:
            if i.isalnum():
                newStr+=i

        return newStr.lower() == newStr[::-1].lower()
        