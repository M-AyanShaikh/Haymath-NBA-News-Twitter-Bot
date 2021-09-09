import tweepy
import time

auth = tweepy.OAuthHandler("k0tw4pLZisLj7iGdL0o9Khyw0",
                      "gVsVBDE2AfzHJvfVyWe2GJV0tBFd7QKH5a9u8v0oMKZDaZbxKQ")

auth.set_access_token("1342876564548177920-YGD468c8AuY4HxUzqovzgLmJrwLvNa",
                           "RdsJtVahcBDPP4K2qrYTWDQGRmhyF0bl7aD2AaVFHsdDr")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = "LaMelo", "lamelo", "melo", "LaMelo Ball", "Lamelo Ball", "Melo Ball", "lamelo ball", "lamelo Ball",\
         "Zion", "zion", "Zion Williamson", "zion williamson", "Zion williamson", "zion Williamson"
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print("Tweet Retweeted")
        tweet.retweet()
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

