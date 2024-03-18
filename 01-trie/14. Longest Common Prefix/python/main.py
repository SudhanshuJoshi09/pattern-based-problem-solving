class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_len = min([len(x) for x in strs])
        for i in range(min_len):
            ref = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != ref:
                    return strs[0][:i]
        return strs[0][:min_len]


if __name__ == "__main__":
    solution = Solution()
    strs = ["Hello", "Hel", "He", "Hello, World"]
    print(solution.longestCommonPrefix(strs))
