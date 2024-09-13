#Ashtin Gage Huntington
#9-12-24
#5th Hour
#HW4
print("Hello World!!!")

homeDict = {
    "Size" : "Large",
    "Quality" : "OK",
    "Price" : [12000,20000,17000]
}
print(homeDict["Price"][2])
homeDict.update({"Rooms" : 3})
print(homeDict)

homeDict.clear()
print(homeDict)

fifthHour = {
    "Classmate1" : {
        "Name" : "Sammy",
        "Age" : [7],
        "IQ" : [-1]  },
    "Classmate2" : {
        "Name": "Eric",
        "Age": [14],
        "IQ": [96] },

    "Classmate3" : {
        "Name": "Mac",
        "Age": [1000000000],
        "IQ": [1000000000],}
}
print(fifthHour["Classmate1"]["Name"],fifthHour["Classmate2"]["Name"],fifthHour["Classmate3"]["Name"])


