from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items based on price
        items.sort()
        # Sort queries while keeping track of original indices
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        max_beauty = 0
        result = [0] * len(queries)
        item_index = 0
        n = len(items)

        # List to store the maximum beauty at each price point
        prices = []
        beauties = []

        for price, idx in sorted_queries:
            # Update max_beauty for items with price <= current query price
            while item_index < n and items[item_index][0] <= price:
                max_beauty = max(max_beauty, items[item_index][1])
                item_index += 1
            # Store the result for this query
            result[idx] = max_beauty

        return result