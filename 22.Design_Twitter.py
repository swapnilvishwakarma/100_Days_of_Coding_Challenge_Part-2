# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweetUsers = {}   
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId in self.tweetUsers:
            self.tweetUsers[userId]["tweets"][tweetId] = self.timestamp
        else:
            self.tweetUsers[userId] = {}
            self.tweetUsers[userId]["tweets"] = {tweetId: self.timestamp}
            self.tweetUsers[userId]["following"] = {}
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        newsFeed = []
        if userId in self.tweetUsers:
            for tweetId in self.tweetUsers[userId]["tweets"]:
                newsFeed.append((tweetId, self.tweetUsers[userId]["tweets"][tweetId]))
            
            for followeeId in self.tweetUsers[userId]["following"]:
                for tweetId in self.tweetUsers[followeeId]["tweets"]:
                    newsFeed.append((tweetId, self.tweetUsers[followeeId]["tweets"][tweetId]))
        newsFeed.sort(key=lambda x: x[1], reverse=True)
        
        if len(newsFeed) >= 10:
            newsFeed = newsFeed[:10]
        
        newsFeed = [tweetId for tweetId, timestamp in newsFeed]
        
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId in self.tweetUsers:
                self.tweetUsers[followerId]["following"][followeeId] = True

                if followeeId not in self.tweetUsers:
                    self.tweetUsers[followeeId] = {"tweets": {}, "following": {}}
            else:
                self.tweetUsers[followerId] = {"tweets": {}, "following": {followeeId: True}}
                if not followeeId in self.tweetUsers:
                    self.tweetUsers[followeeId] = {"tweets": {}, "following": {}}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId in self.tweetUsers and followeeId in self.tweetUsers[followerId]["following"]:
                del self.tweetUsers[followerId]["following"][followeeId]


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)