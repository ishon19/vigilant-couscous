class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total_count = 1

        freq_map = defaultdict(dict)

        # Calculate frequencies based on remainder
        for num in nums:
            remainder = num % k
            freq_map[remainder][num] = freq_map[remainder].get(num, 0) + 1

        # Iterate through each remainder group
        for fr in freq_map.values():
            n = len(fr)  # Number of elements in the current group

            subsets = sorted(fr.items())
            counts = [0] * (n + 1)  # Array to store counts of subsets
            counts[n] = 1  # Initialize count for the last subset

            # Calculate counts for each subset starting from the second last
            for i in range(n - 1, -1, -1):

                # Count of subsets skipping the current subset
                skip = counts[i + 1]
                # Count of subsets including the current subset
                take = 2 ** subsets[i][1] - 1

                # If next number has a 'difference', 
                # calculate subsets; otherwise, move to next
                if i + 1 < n and subsets[i + 1][0] - subsets[i][0] == k:
                    take *= counts[i + 2]
                else:
                    take *= counts[i + 1]

                # Store the total count for the current subset
                counts[i] = skip + take

            total_count *= counts[0]

        return total_count - 1