#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (39.87%)
# Likes:    6992
# Dislikes: 222
# Total Accepted:    584.6K
# Total Submissions: 1.5M
# Testcase Example:  '"()"'
#
# Given a string s containing only three types of characters: '(', ')' and '*',
# return true if s is valid.
#
# The following rules define a valid string:
#
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis
# ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string "".
#
#
#
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "(*)"
# Output: true
# Example 3:
# Input: s = "(*))"
# Output: true
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.
#
#
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0


# @lc code=end
