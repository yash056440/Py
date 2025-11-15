num = int(input("Enter number:"))

for row in range(1,num+1):
   
    for col in range(num-row):
        print(" ", end="")
    for col in range(0,row):
        print("* ", end="")
    print(" ")

for r in range(1,num):
   
    for c in range(0,r):
        print(" ", end="")
    for c in range(num-r):
        print("* ", end="")
    print(" ")
