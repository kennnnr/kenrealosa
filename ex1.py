money = input("How much money do you have?")
print "The Price of a Nintedo Wii is 20,000"
afford = money / 20000
print ("You can afford") , afford, ("nintendo wii")
remaining = money % 20000
if money>20000:
    print ("You have sufficient money")
else:
    print (" The money you need is") , 20000- money
    
