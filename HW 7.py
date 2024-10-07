#Ashting Gage Huntington
#5th Hour
#HW7

time = 0
wifi = True
login = True
admin = True
if wifi == True :
    if login == True:
        if admin == True:
            print("Welcome Bruv")
            time += 1
        else:
            print("error admin")
    else:
        print("error login")
else:
    print("error wifi")
