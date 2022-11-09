# busy intersection

from sys import api_version


def getResult(arrival, street):
    hashmap = {}
    waiting = []

    for idx, time in enumerate(arrival):
        if not time - 1 in hashmap:
           hashmap[idx] = time
        else:
            waiting.append((idx, time))
            


