from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0

        for word in words:
            # Check if adding a new word exceeds maxWidth
            if num_of_letters + len(word) + len(cur) > maxWidth:
                # spaces to distribute
                spaces_to_distribute = maxWidth - num_of_letters
                
                # handle case with single word separately
                if len(cur) == 1:
                    line = cur[0] + ' ' * spaces_to_distribute
                else:
                    # multiple words: evenly distribute spaces
                    spaces_between_words, extra_spaces = divmod(spaces_to_distribute, len(cur)-1)
                    line = ''
                    for i in range(len(cur)-1):
                        line += cur[i] + ' ' * (spaces_between_words + (1 if i < extra_spaces else 0))
                    line += cur[-1]  # last word in line, no extra spaces after
                
                res.append(line)
                cur, num_of_letters = [], 0
            
            cur.append(word)
            num_of_letters += len(word)
        
        # Handle last line separately: left-justify
        last_line = ' '.join(cur)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res
