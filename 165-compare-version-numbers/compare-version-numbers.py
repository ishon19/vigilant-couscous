class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        for r1, r2 in zip(v1, v2):
            if int(r1) > int(r2):
                return 1
            elif int(r1) < int(r2):
                return -1
        
        # at this point we think both are equal
        # check the longer one for more revisions
        minLen = min(len(v1), len(v2))
        if len(v1) > len(v2):
            if any([int(val)!=0 for val in v1[minLen:]]):
                return 1
        elif len(v2) > len(v1):
            if any([int(val)!=0 for val in v2[minLen:]]):
                return -1

        return 0