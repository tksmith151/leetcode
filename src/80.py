from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        current_count = 0
        place_index = 1
        search_index = 1
        previous_number = nums[0]
        current_count = 1
        while search_index < len(nums):
            search_number = nums[search_index]
            if previous_number == search_number:
                current_count += 1
                if current_count <= 2:
                    nums[place_index] = search_number
                    place_index += 1
            else:
                previous_number = search_number
                current_count = 1
                nums[place_index] = search_number
                place_index += 1
            search_index += 1
        for replace_index in range(place_index, len(nums)):
            nums[replace_index] = None
        return place_index
            

                    


if __name__ == "__main__":
    solution = Solution()
    test = [1, 1, 1, 2, 3, 3, 3, 4, 4]
    output = solution.removeDuplicates(test)
    print(output)
    print(test)
    test = [1,1,1,2,2,3]
    output = solution.removeDuplicates(test)
    print(output)
    print(test)
    test = [1,2]
    output = solution.removeDuplicates(test)
    print(output)
    print(test)