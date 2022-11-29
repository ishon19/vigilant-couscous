def mergeSort(arr, inv, res):
    if len(arr) > 1:
        mid = len(arr)//2
        l, r = arr[:mid], arr[mid:]
        mergeSort(l, inv, res)
        mergeSort(r, inv, res)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                inv += len(l)-i
                res.append(inv)
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
    print(inv)
    return res


arr = [5, 4, 3, 2, 1]
print('inversions', mergeSort(arr, 0, []))
print(arr)
