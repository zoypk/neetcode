class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sHash = {}
        tHash = {}

        for char in s:
            if char in sHash:
                sHash[char] = sHash[char] + 1
            else:
                sHash[char] = 1

        for char in t:
            if char in tHash:
                tHash[char] = tHash[char] + 1
            else:
                tHash[char] = 1

        if sHash == tHash:
            return True
        else:
            return False

        