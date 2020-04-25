import tweepy
import requests
import datetime

def oauth():
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    ACCESS_TOKEN = ''
    ACCESS_SECRET = ''
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    #各種キーの設定
    return auth

def tweet(auth):
    api = tweepy.API(auth)
    now = datetime.datetime.now()
    user = ''    #対象のユーザーのID
    screen = ''    #対象のScreen name
    tweet = api.user_timeline(user)
    for i in tweet:
        when = i.created_at + datetime.timedelta(hours=9)
        dif = now -when
        print("{}\n{}\n{}\n".format(dif.seconds, i.text,when))
        if(dif.seconds < 60):
            msg = tweet.text + "\nhttps://twitter.com/{}/status/{}".format(screen,tweet.id)
            notify(msg)

def notify(msg):
    name = ''    #通知を送るBOTのなまえ
    icon = ''    #アイコンのURL
    data = {
        'username' : name,
        'avatar_url' : icon,
        'content' : msg
    }
    url = ''    #webhookのURL
    requests.post(url, data)

api = oauth()
tweet(api)