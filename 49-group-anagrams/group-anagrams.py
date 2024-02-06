class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)

        for s in strs:
            key = "".join(sorted(list(s)))
            groups[key].append(s)

       # print(groups)

        return [val for val in groups.values()] 