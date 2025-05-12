class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(s.split())[::-1])


if __name__ == "__main__":
    solution = Solution()
    test = "  hello world  "
    output = solution.reverseWords(test)
    print(output)
