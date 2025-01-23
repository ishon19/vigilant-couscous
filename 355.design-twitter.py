#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
class Twitter:

    def __init__(self):
        self.clock = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.clock, tweetId))
        self.clock += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        users = self.followers[userId] | {userId}

        for user in users:
            for tweet in self.tweets[user]:
                heappush(minHeap, tweet)
                if len(minHeap) > 10:
                    heappop(minHeap)
        
        return [tweetId for _, tweetId in sorted(minHeap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

