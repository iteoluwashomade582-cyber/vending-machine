name = input("Your name: ")
while name == "":
    print("Invalid name")
    name = input("Your name: ")


 
ref = input("Booking reference:" )
while len(ref) > 10 or len(ref) < 4:
    print("Reference must be between 4 and 10")
    ref = input("Booking reference:" )

            
 
hours = input("Hours needed: ")
valid = False
while valid == False:
    if hours.isdigit() == False:
        print("Invalid number, try again")
        hours = input("Hours needed: ")
    else:
        if int(hours) > 8 or int(hours) < 1:
            print("Invalid number, try again")
            hours = input("Hours needed: ")
        else:
            valid = True



 
print("Booked:", name, ref, hours)
