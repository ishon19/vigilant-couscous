"""
    CTCI 1.6
    String Compression: Implement a method to perform basic string compression
    using the counts of repeated characters. For example, the string aabcccccaaa
    would become a2b1c5a3. If the "compressed" string would not become smaller
    than the original string, your method should return the original string. You
    can assume the string has only uppercase and lowercase letters (a - z).
"""

# my solution
def compress(string):
    stack = []

    for char in string:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])

    res = ''
    for item in stack:
        res += item[0] + str(item[1])

    return res if len(res) < len(string) else string


print(compress("aaaabbcddeeee"))


# author's solution
def compress2(string):
    compressed = []
    count_consecutive = 0

    for i in range(len(string)):
        count_consecutive += 1

        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed.append(string[i])
            compressed.append(str(count_consecutive))
            count_consecutive = 0

    return min(string, ''.join(compressed), key=len)

print(compress2("aaaabbcddeeee"))