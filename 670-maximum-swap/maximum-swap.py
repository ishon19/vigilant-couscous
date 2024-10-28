class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        
        # store the last occurance of each digit
        idx_map = {int(d): i for i, d in enumerate(num_list)}

        # for each digit check if a larger number exists at a later position
        for i, digit in enumerate(num_list):
            # starting from 9 to current digit check for the occurance of a greater number
            for d in range(9, int(digit), -1):
                # if there is a larger digit at later position, swap it
                if idx_map.get(d, -1) > i:
                    num_list[i], num_list[idx_map[d]] = num_list[idx_map[d]], num_list[i]
                    return int(''.join(num_list))
        
        return num