"""
    355. Design Twitter

    Total Accepted: 2111 Total Submissions: 9626 Difficulty: Medium
    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

        1.postTweet(userId, tweetId): Compose a new tweet.
        2.getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        3.follow(followerId, followeeId): Follower follows a followee.
        4.unfollow(followerId, followeeId): Follower unfollows a followee.

"""

import heapq
class Twitte(object):
    def __init__(self,timestamp,val):
        self.val = val
        self.time = timestamp
        self.next = None

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user = {}
        self.timestamp = 0


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        tw = Twitte(self.timestamp,tweetId)
        self.timestamp -= 1

        if userId not in self.user:
            head = Twitte(1,tweetId)
            self.user[userId] = ({},head)
        f , h = self.user[userId]
        tw.next = h.next
        h.next = tw


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.user:
            return []

        hq = []
        res = []
        count = 0

        for friend , _ in self.user[userId][0].iteritems():
            friendP = self.user[friend][1]
            if friendP.next:
                heapq.heappush(hq,(friendP.next.time, friendP.next))
        myH = self.user[userId][1]

        if myH.next:
            heapq.heappush(hq,(myH.next.time, myH.next))

        while hq and count < 10:
            t = heapq.heappop(hq)
            res.append(t[1].val)
            if t[1].next:
                heapq.heappush(hq,(t[1].next.time, t[1].next))
            count += 1
        return res

