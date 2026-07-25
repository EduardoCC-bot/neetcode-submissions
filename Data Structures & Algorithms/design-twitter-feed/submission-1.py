class Twitter:

    def __init__(self):
        self.tweetsMap = defaultdict(list) # User Id : set : tweet id
        self.followMap = defaultdict(set) # userID : set folowers user's ID's
        self.counter = 0
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsMap[userId].append([self.counter, tweetId])
        if len(self.tweetsMap[userId]) > 10:
            self.tweetsMap[userId].pop(0)
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetsMap:
                index = len(self.tweetsMap[followeeId]) - 1
                counter, tweetId = self.tweetsMap[followeeId][index]
                minHeap.append([counter, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                counter, tweetId = self.tweetsMap[followeeId][index]
                heapq.heappush(minHeap, [counter, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]: 
            self.followMap[followerId].remove(followeeId)