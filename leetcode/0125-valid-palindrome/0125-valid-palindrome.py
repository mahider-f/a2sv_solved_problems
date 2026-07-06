class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed_chars = string.ascii_letters + string.digits
        t = s.lower()
        t = "".join([x for x in t if x in allowed_chars])
        return t == t[::-1]
