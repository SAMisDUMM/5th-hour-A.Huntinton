#Ashting Gage Huntington
#5th Hour
#Scenario 2

print("Hello World!!!")

partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background": "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
    }
}


enemyDict = {
    "Mutated" : {
        "Attack Speed" : "5APM",
        "Size": "Large",
        "Health": 25,
        "Damage": 10}

}

print(enemyDict["Mutated"]["Health"] - partyDictionary["LaeZel"]["Damage"])
print(enemyDict["Mutated"]["Health"] - partyDictionary["Shadowheart"]["Damage"])
print(enemyDict["Mutated"]["Health"] - partyDictionary["Gale"]["Damage"])
print(enemyDict["Mutated"]["Health"] - partyDictionary["Astarion"]["Damage"])