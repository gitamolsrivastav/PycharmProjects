import requests

import twitter

Consumer_Key = 'jhOukeFotUMLr34bxS4L6bRZ7'
Consumer_Secret = '1N2WGrsJE4oNKYrBC6oxfUGvJEmFrySLT0HmPmROSJg0N7S66A'

Access_Token = '725828254272081920-6loYd4jka2vm4EIb9FPOlICYOpdsGiK'
Access_Token_Secret ='g6plq1xeGJFocJPKW7AmAGIwQVjncRFLUha3WR82wXc6G'

api = twitter.Api(consumer_key=Consumer_Key,
                  consumer_secret=Consumer_Secret,
                  access_token_key=Access_Token,
                  access_token_secret=Access_Token_Secret)

print(api.VerifyCredentials())

print(api.GetFollowerIDs())


print(api.GetFriendIDs())

api.PostUpdates(status)
api.PostDirectMessage(user, text)
api.GetUser(user)
api.GetReplies()
api.GetUserTimeline(user)
api.GetHomeTimeline()
api.GetStatus(status_id)
api.DestroyStatus(status_id)
api.GetFriends(user)
api.GetFollowers()
api.GetFeatured()
api.GetDirectMessages()
api.GetSentDirectMessages()
api.PostDirectMessage(user, text)
api.DestroyDirectMessage(message_id)
api.DestroyFriendship(user)
api.CreateFriendship(user)
api.LookupFriendship(user)
api.VerifyCredentials()
