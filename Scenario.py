#Ashtin Gage Huntington
#9-12-24
#5th Hour
#HW4
print("Hello World!!!")





videoGame = {
    "Zombies" : {
        "Attack":"65APM",
        "Size": "Medium",
        "Health": 150,
        "Damage": 15,},

    "Spitter" : {
        "Attack Speed" : "50AMP",
        "Size": "Medium",
        "Health": 175,
        "Damage": 20,},

    "Runner" : {
        "Attack Speed" : "80APM",
        "Size" : "Small",
        "Health" : 100,
        "Damage" : 20  },

    "Brute" : {
        "Attack Speed" : "10APM",
        "Size": "Large",
        "Health": 250,
        "Damage": 50 },

    "Mutated" : {
        "Attack Speed" : "5APM",
        "Size": "Large",
        "Health": 500,
        "Damage": 200},

}


print(videoGame["Zombies"]["Damage"],videoGame["Spitter"]["Damage"],videoGame["Runner"]["Damage"],videoGame["Brute"]["Damage"], videoGame["Mutated"]["Damage"])


videoGame["Zombies"]["Damage"] = int(input("New Zombie Damage:"))
videoGame["Spitter"]["Damage"] = int(input("New Spitter Damage:"))
videoGame["Runner"]["Damage"] = int(input("New Runner Damage:"))
videoGame["Brute"]["Damage"] = int(input("New Brute Damage:"))
videoGame["Mutated"]["Damage"] = int(input("New Mutated Damage:"))


print(videoGame["Zombies"]["Damage"],videoGame["Spitter"]["Damage"],videoGame["Runner"]["Damage"],videoGame["Brute"]["Damage"], videoGame["Mutated"]["Damage"])



