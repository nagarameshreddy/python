print("while loop")

#a=int(input("Enter any nunber"))
a=0

while a<5:
    print(a)
    a=a+1
print("while loop with break")
a=0
while a<5:
    a=a+1
    if a==3:
        break
    print(a)
    
print("while loop with continue")

a=0
while a<5:
    a=a+1
    if a==3:
        continue
    print(a)