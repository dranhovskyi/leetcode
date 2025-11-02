class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return []
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [map[complement], i]
            map[nums[i]] = i
        
        return []