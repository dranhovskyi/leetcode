class Solution:

    def longestPalindrome(self, s: str) -> str:

        for length in range(len(s), 0,  -1):
            for start in range(len(s) - length + 1):
                if (self.check(s, start, start + length)):
                    return s[start: start + length]

        return ""
    
    def check(self, s: str, i: int, j: int) -> bool:
        left: int = i
        right: int = j - 1

        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True


solution = Solution()
result: str = solution.longestPalindrome('babad')
print(result)