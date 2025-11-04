class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        umap: dict[str, int] = {}
        
        for right in range(len(s)):
            ch = s[right]

            if (ch in umap and umap[ch] >= left):
                left = umap[ch] + 1
            
            umap[ch] = right

            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
