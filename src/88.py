from typing import List


class Solution:
    def merge(
        self, first: List[int], first_index: int, second: List[int], second_index: int
    ) -> None:
        """
        Merge Sorted Arrays
        """
        merge_index = len(first) - 1
        while merge_index >= 0:
            # Iterate from the back of the arrays
            if second_index < 1:
                # If second index is less than one then nothing else needs to change
                break
            elif first_index < 1 or first[first_index - 1] < second[second_index - 1]:
                # Use second list if first index is less than one or
                # second list has the larger number
                first[merge_index] = second[second_index - 1]
                second_index -= 1
            else:
                # Otherwise use the first list
                first[merge_index] = first[first_index - 1]
                first_index -= 1
            merge_index -= 1
