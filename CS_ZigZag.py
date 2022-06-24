from datetime import datetime


def solution(numbers):
    ans = []

    for i in range(len(numbers)-2):
        if numbers[i] < numbers[i+1] > numbers[i+2] or numbers[i] > numbers[i+1] < numbers[i+2]:
            ans.append(1)
        else:
            ans.append(0)

    return ans


def stringQuestion(arr):
    if len(arr) == 1:
        return arr[0]
    size = len(arr)
    ans = ''
    maxElement = len(min(arr, key=len))
    print(maxElement)
    try:
        for j in range(0, maxElement):
            for i in range(size):
                ans += '' if not len(arr[i][j]) else arr[i][j]
    except:
        pass

    try:
        for j in range(maxElement, len(max(arr, key=len))):
            for i in range(size):
                ans += '' if not len(arr[i][j]) else arr[i][j]
    except:
        pass

    return ans


def totalCost(startuptimes, shutdowntime):
    timeformat = '%H:%M'
    startuptimes = [datetime.strptime(x, timeformat) for x in startuptimes]
    shutdowntime = datetime.strptime(shutdowntime, timeformat)
    totalCost = 0
    for i in range(len(startuptimes)):
        if startuptimes[i] < shutdowntime:
            totalCost += (shutdowntime - startuptimes[i]).seconds

    return int(totalCost/60)

# count all unique subarrays with sum atleast k
def countSubarrays(arr, k):
    count = 0
    counts = {0:1}
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum >= k:
                counts[sum] = 1

    # find the max val in the dict
    for i in counts:
        if i >= k:
            count += 1

    return count


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 1]
    names = ["Daisy", "Rose", "Hyacinth", "Poppy"]
    startuptimes = ["12:30", "14:00", "19:55"]
    # startuptimes = ["12:01", "00:00", "23:58", "23:59"]
    shutdowntime = "20:00"
    # print(zip(names))
    # print(solution(numbers))
    # print(stringQuestion(names))
    # print(totalCost(startuptimes, shutdowntime))
    print(countSubarrays(numbers, 3))
