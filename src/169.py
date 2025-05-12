from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Use a dictionary to track a count of each number and then find the max count
        """
        counts = {}
        for num in nums:
            counts.setdefault(num, 0)
            counts[num]+=1
        max_value = 0
        max_key = None
        for key, value in counts.items():
            if value > max_value:
                max_key = key
                max_value = value
        return max_key