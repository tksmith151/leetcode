from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        assert len(nums) > 0
        place_index = 0
        search_index = 0
        for search_index in range(len(nums)):
            last_number = nums[place_index]
            search_number = nums[search_index]
            if last_number != search_number:
                place_index += 1
                nums[place_index] = search_number
        for replace_index in range(place_index + 1, len(nums)):
            nums[replace_index] = None
        return place_index + 1


if __name__ == "__main__":
    solution = Solution()
    test = [1, 1, 2, 3, 3, 3, 4, 4]
    output = solution.removeDuplicates(test)
    print(output)
    print(test)
