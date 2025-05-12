from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        forward_index = 0
        reverse_index = len(nums) - 1
        count = 0
        while forward_index < len(nums):
            current_num = nums[forward_index]
            if current_num is None:
                break
            if nums[forward_index] == val:
                nums[forward_index] = nums[reverse_index]
                nums[reverse_index] = None
                reverse_index -= 1
            else:
                count += 1
                forward_index += 1
        return count
