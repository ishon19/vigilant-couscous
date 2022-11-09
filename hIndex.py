# python program to determine the h-index of a researcher
from audioop import reverse


def hIndex(citations):
    # sort the list of citations
    citations.sort()
    # initialize the h-index to 0
    h_index = 0
    # loop through the list of citations
    for i in range(len(citations)):
        # if the h-index is less than the current citation
        if h_index < citations[i]:
            # set the h-index to the current citation
            h_index = citations[i]
        # if the h-index is equal to the current citation
        elif h_index == citations[i]:
            # set the h-index to the current citation
            h_index = citations[i]
        # if the h-index is greater than the current citation
        else:
            # break the loop
            break
    # return the h-index
    return h_index



citations = [1,4,1,4,2,1,3,5,6]
print(hIndex(citations))
