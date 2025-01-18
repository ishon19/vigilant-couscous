class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = [int(revision) for revision in version1.split(".")]
        v2_list = [int(revision) for revision in version2.split(".")]

        if len(v1_list) < len(v2_list):
            for i in range(len(v2_list) - len(v1_list)):
                v1_list.append(0)
        else:
            for i in range(len(v1_list) - len(v2_list)):
                v2_list.append(0)
        
        i = 0
        while i < len(v1_list):
            if v1_list[i] < v2_list[i]:
                return -1
            elif v1_list[i] > v2_list[i]:
                return 1            
            i += 1
        
        return 0