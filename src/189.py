from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        diff = k % len(nums)
        output = nums[-diff:] + nums[:-diff]
        for index in range(len(nums)):
            nums[index] = output[index]

if __name__ == "__main__":
    solution = Solution()
    test = [-1,-100,3,99]
    k = 1
    solution.rotate(test, k)
    print(test)
    test = [1,2,3,4,5,6,7]
    k = 3
    solution.rotate(test, k)
    print(test)
