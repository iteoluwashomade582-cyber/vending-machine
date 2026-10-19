
CODE_LENGTH = 8     
code = input("Wristband code: ")

valid = True
  
if len(code) != 8:
      valid = False

if code[0].isdigit()  or code[1].isdigit() :
      valid = False
  
for position in range(2, 8):
      if code[position].isalpha():
          valid = False

for position in range(0,8):
      if code[position] == "":
            valid = False

print(valid)


'''
PRICE = 12
total = 0
 
for ticket in range(4):
    discount = PRICE * 0.1
    total = total + (PRICE - discount)
 
print(total)
'''