from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # No trades if less than 2 entries
        if len(prices) < 2:
            return 0
        best_profit = 0
        current_profit = 0
        for index in range(1, len(prices)):
            # Get daily change
            last = prices[index - 1]
            new = prices[index]
            diff = new - last
            current_profit += diff
            # Update best profit if needed
            if current_profit > best_profit:
                best_profit = current_profit
            # If the current_profit value is a loss then just start over count
            if current_profit < 0:
                current_profit = 0
        return best_profit


if __name__ == "__main__":
    solution = Solution()
    test = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(test))
