import tweepy

access_token_key = "2608811599-ecnAJholCTAQFlph1F30Ua6t5oBXNdqzilrfJcq"
access_token_secret = "pReRgSKkgjTGEAwImt8ZeNyjwaJlBmRyPiOoOMHNpOrm1"

consumer_key = "ZGMYiGs7MOoP6sBBm4oDAWqiN"
consumer_secret = "av7a3DxLuMWx9Lqi4uYNHA1v2uPJSxAEuYXQYGmzAQSd3FDUDw"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)
api=tweepy.API(auth)
public_tweets=api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

