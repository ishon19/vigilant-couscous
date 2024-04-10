class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # work backwards to create the array from the sorted position
        # simulate the array index movement
        indexes = collections.deque(range(len(deck)))
        sorted_deck = sorted(deck)
        res = [0] * len(deck)

        for card in sorted_deck:
            # move the index to simulate the order
            res[indexes.popleft()] = card
            if indexes:
                indexes.append(indexes.popleft())
        
        return res








