#Name:
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).

sport = {
    "sport1" : {
        "name" : "Soccer",
        "player#" : 22,
        "ball" : True,
    },
    "sport2" : {
        "name" : "Hockey",
        "player#" : 12,
        "ball" : False,
    },
    "sport3" : {
        "name" : "Tennis",
        "player#" : 2,
        "ball" : True,
    }
}
#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum

def players() :
    print(sport["sport1"]["player#"]+sport["sport2"]["player#"]+sport["sport3"]["player#"])

#3. Call the function with arguments here

players()