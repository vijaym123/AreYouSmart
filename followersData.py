import tweepy
import password

def authorize(index):
    consumerKey = password.getPassword(index)["consumerKey"]
    consumerSecret = password.getPassword(index)["consumerSecret"]
	accessToken = password.getPassword(index)["accessToken"]
	accessTokenSecret = password.getPassword(index)["accessTokenSecret"]
	auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
	auth.set_access_token(accessToken, accessTokenSecret)
    return auth

if __name__ == '__main__':
    index = 1
    f = open("people","r")
    people = f.read().split("\n")
    auth = authorize(index)
    api = tweepy.API(auth)
    peopleID = [api.get_user(i).id for i in people]
