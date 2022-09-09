import os 
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

from instabot import Bot

my_bot = Bot()

#accounts
usernames = ["username1"]   #add usernames
passwords = ["password"]  #add passwords
accounts = dict(zip(usernames, passwords))

for username, password in accounts.items():
    #login
    my_bot.login(username=username, password=password)

    #like a post
    try:
        my_bot.like_user("creative_kira", amount=1, filtration=False)
    except Exception:
        print(Exception)

    #comment
    try:
        user_id = my_bot.get_user_id_from_username("creative_kira")
        media_id = my_bot.get_last_user_medias(user_id, 1)
        my_bot.comment(media_id[0], "Hello, this is for test purpose only.") 
    except Exception:
        print(Exception)

    my_bot.logout()
