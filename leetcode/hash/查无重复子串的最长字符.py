class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        hashset = set()
        maxlen = 0
        length = 0
        i = 0
        while i < len(s):
            if s[i] not in hashset:
                hashset.add(s[i])
                length += 1
                if length > maxlen:
                    maxlen = length
            else:
                while len(s[start:i + 1]) != len(set(s[start:i + 1])):
                    start += 1
                hashset = set(s[start:i+1])
                length = len(hashset)
            i += 1
        return maxlen


s = Solution()
print(s.lengthOfLongestSubstring("aab"))
