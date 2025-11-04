public class Solution 
{
    public int LengthOfLongestSubstring(string s) 
    {
        int maxLen = 0;
        int left = 0;
        var umap = new Dictionary<char, int>();

        for(int right = 0; right < s.Length; right++)
        {
            char ch = s[right];

            if (umap.ContainsKey(ch) && umap[ch] >= left) {
                left = umap[ch] + 1;
            }

            umap[ch] = right;

            maxLen = Math.Max(maxLen, (right - left + 1));
        }

        return maxLen;
    }
}
