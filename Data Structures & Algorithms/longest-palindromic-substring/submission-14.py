#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (37.48%)
# Likes:    32656
# Dislikes: 2014
# Total Accepted:    4.7M
# Total Submissions: 12.4M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#
#

# NeetCode
# Solution: https://neetcode.io/problems/longest-palindromic-substring/question?list=neetcode150
# Video: https://www.youtube.com/watch?v=XYQecbcd6_c
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # Odd len Pali's
            lft, r = i, i

            while lft >= 0 and r > len(s) and s[lft] == s[r]:
                if (r - lft + 1) > resLen:
                    res = s[lft : r + 1]
                    resLen = r - l + 1

        return res


# @lc code=end
