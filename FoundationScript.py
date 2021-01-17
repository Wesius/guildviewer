import pprint
import requests
import json
import time

player = input("What player do you want to see guild average stats for?")

response = requests.get("https://api.slothpixel.me/api/guilds/" + player)

info = response.json()

member = info.get('members')
level = info.get('level')

print(level)


lvlList = []
achpList = []
questList = []

for i in range(0,len(member)):
    members = dict(member[i])
    print(i)
    uuid = members['uuid']
    time.sleep(1)
    lvlget = requests.get("https://api.slothpixel.me/api/players/" + uuid)
    lvlgetjson = lvlget.json()
    lvl = lvlgetjson['level']
    achp = lvlgetjson["achievement_points"]
    quests = lvlgetjson["quests_completed"]
    lvlList.append(lvl)
    achpList.append(achp)
    questList.append(quests)

LVL = sum(lvlList)/len(lvlList)
print("The average NWL is ", round(LVL,2))

AP = sum(achpList)/len(achpList)
print("The average AP is ", round(AP,2))

QST = sum(questList)/len(questList)
print("The average Quests are ", round(QST,2))






