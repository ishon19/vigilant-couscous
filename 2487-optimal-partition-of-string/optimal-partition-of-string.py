class Solution:
    def partitionString(self, s: str) -> int:
        # the number of partitions we need depends on the number of times
        # we see an existing character in the string

        seen_set = set()
        count = 1

        for i in range(len(s)):
            if s[i] in seen_set:
                seen_set.clear()
                count += 1
            seen_set.add(s[i])
       
        return count