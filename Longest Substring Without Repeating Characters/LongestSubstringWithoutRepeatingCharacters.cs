/* 
Intuition
The question asks us to return the longest substring that does not contain duplicates. Naturally, when we need to find the longest length, the sliding window approach comes to mind.

Approach
As discussed, we'll use Sliding Window with 2 pointers along with an Unordered Map.

Why do we use Sliding Window? Because we need to find the longest substring length efficiently.

Why do we use Two Pointers? Because we need to track both the start and end of our window.

Why do we need HashMap/UnorderedMap? To keep track of characters and their positions, helping us detect duplicates within our current window.

How it works:

We keep both the left and right pointers at the starting position initially.
We move the right pointer one by one all the way to the last index.
If the character at s[right] is not present in the map, the code directly goes to umap[ch] = right; and stores the character with its index.
If the character already exists in the map AND its previous position is within our current window (greater than or equal to left), we enter the if condition.
Inside the if condition, we update the left pointer to umap[ch] + 1, moving it just past the duplicate character.
Then we calculate maxi, which stores the longest substring length found so far.
We calculate it using right - left + 1.
Finally, we return maxi.


Complexity
Time complexity: O(n)
BreakDown:
For loop Time complexity :O(n)
find function TC: O(1) {Average case}
Space complexity: O(n)
BreakDown:
UnorderedMap Space: O(n)
*/

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
