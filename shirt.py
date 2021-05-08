

waist = int(input("What is your waist measurement: "))

chest = int(input("What is your chest measurement: "))

if waist <= 32 and chest <= 36:
    print("size = S")
elif waist <= 35 and chest <= 40:
    print ("size = M")
elif waist <= 38 and chest <= 44:
    print ("size = L")
else: 
    print ("No size available")
