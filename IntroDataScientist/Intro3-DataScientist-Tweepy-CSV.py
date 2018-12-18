import tweepy
from textblob import TextBlob
import pandas as pd

# Step 1 - Authenticate
consumer_key = 'SYIU2vNxmgu6BV9N10ybfzf5M'
consumer_secret = '1GEmYq6bQp4QG7HSBl8nVdz0JrxmcCLujm6mVYfoMTwG4G8JEX'
access_token = '1071479591699734528-0I9dRGfn0ElPFOZmg15aztVIhvcAHb'
access_token_secret = 'IF8xtLLV7NW9r4fgVDlSs46wfBSN3rhsNT1NN2fqHlgFq'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')

#create a empty dataframa with two columns
df = pd.DataFrame(columns=['Text','Sentiment_level'])
i = 0

for tweet in public_tweets:
    print(tweet.text)
    print(type(tweet.text))
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print(type(analysis.sentiment.polarity))
    print("")

#to create a dataFrame from each tweet with its type sentiment

    df.loc[i] = [tweet.text , round(analysis.sentiment.polarity,2)]
    i += 1
#print dataFrame
print(df)
