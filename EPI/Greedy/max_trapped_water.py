def getMaxTrappedWater(heights):
    i, j, res = 0, len(heights)-1, 0
    while i<j:
        width = j - i
        res = max(res, width * min(heights[i], heights[j]))
        if heights[i]>heights[j]:
            j -= 1
        else:
            i += 1
    return res