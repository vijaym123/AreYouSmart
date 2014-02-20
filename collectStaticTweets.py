import tweepy
import os
import ssl
import password
import re
import json

def filterStatus(string):
    pun = "\n"
    regex=re.compile('[%s]' % re.escape(pun))
    return regex.sub("",string)

def authorize(index):
    consumerKey = password.getPassword(index)["consumerKey"]
    consumerSecret = password.getPassword(index)["consumerSecret"]
    accessToken = password.getPassword(index)["accessToken"]
    accessTokenSecret = password.getPassword(index)["accessTokenSecret"]

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    return auth

def getUserObjects(filename):
    f = open(filename,"r")
    people = f.read().split("\n")
    api = tweepy.API(authorize(1))
    people = [api.get_user(i) for i in people]            
    return people

def collectAndWriteData(person,numberOfPages):
    fWrite = open(str(person.screen_name)+".tweets","w")
    convertToStr = ['created_at']
    buildList = []
    for count in range(numberOfPages):
        tweets = person.timeline(page=count)
        if tweets == []:
            break
        for item in tweets:
            for i in convertToStr:
                item.__dict__[i] = str(item.__dict__[i])
            itemsToBeRemoved = [i for i in item.__dict__ if str(type(item.__dict__[i])).startswith("<class ")]
            [item.__dict__.pop(i) for i in itemsToBeRemoved]
            buildList.append(item.__dict__)
            print item
    fWrite.write(json.dumps(buildList))
    fWrite.close()
    return

if __name__ == "__main__":
    auth = authorize(1)
    filename = "people"
    numberOfPages = 10
    api = tweepy.API(auth)
    people = getUserObjects(filename)
    for person in people:
        collectAndWriteData(person,numberOfPages)