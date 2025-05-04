class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        response_counts = defaultdict(int)

        for items in responses:
            unique_responses = list(set(items))
            for response in unique_responses:
                response_counts[response] += 1
        
        res = sorted([[count, response] for response, count in response_counts.items()], key=lambda x: (-x[0], x[1]))

        return res[0][-1]