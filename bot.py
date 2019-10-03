import tweepy
import tkinter

consumer_key = 'ktiRHsGeFhwkbeJqqGjTpXtyN'
consumer_secret = 'JVlwk424wjpaIrL0hiaEr99Vx8UhK2eHlTvOsV7WuLia6I0und'

access_token = '51619384-BvK6yF9mYs6dxoCKU2neNGTEnWYHrkMgfLPbV3jXf'
access_token_secret = 'YnbrjOPyF6gAVm0lYY3wisX5KirbyeOYUTzRZzS8kQu0q'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)