import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json #java script object notaion it is like dictionary
from textblob import TextBlob
import matplotlib.pyplot as plt
import re
"# -- coding: utf-8 --"
def calctime(a):
    return time.time()-a
positive=0
negative=0
compound=0
initime=time.time()
count=0
plt.ion()
ckey='n0Sfbq7ZVuTk68YP6s5H5n7sT'
csecret='TAV922KwgfhoBhhFdBzPMiuCuRQFAZtG9rHhxKlaLeACDKVe8v'
atoken='3101961192-muBYJnJF8bNVRDo11JPfRW324mqqIiX24F9MRG3'
asecret='B6f8v7HG5Hg8RzIS0LsB2NOH8mkq9X0HbD1gWzrzuX0Md'
class listener(StreamListener):
    def on_data(self,data):
        global initime
        
        t=int(calctime(initime))
        all_data=json.loads(data)
        tweet=all_data("text")
        tweet = " ".join(re.finadall("[a-zA-Z]+",tweet))#we need only words a to z and A to Z
        blol=TextBlob(tweet.strip())
        
        global positive
        global negative
        global compund
        global count
        
        count=count+1
        senti=0
        
        for sen in blob.sentences:
            senti=senti+sen.sentiment.polarity
            if sen.sentiment.polarity >= 0:
                positive = positive + sen.sentiment.polarity
            else:
                negative=negative+sen.sentiment.polarity
            compound = compound + senti
        
        print(count)
        print(tweet.strip())
        print(senti)
        print(t)
        print(str(positive)+' '+str(negative)+' '+str(compound))
        
        plt.axis([0,70,-20,20])
        plt.xlabel('Time')
        plt.ylabel('Sentiments')
        plt.plot([t],[positive],'go',[t],[negative],'ro',[t],[compound],'bo')
        plt.show()
        plt.pause(0.0001)
        if count == 200:
            return False
        else:
            return True
    
    def on_error(self,status):
        print(status)
        
auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

searchTerm = input("Enter keyword/tag to search about: ")
NoOfTerms=int(input("Enter how many tweets to search: "))

twiterStream = Stream(auth,listener(NoOfTerms))
twiterStream.filter(track=[searchTerm])