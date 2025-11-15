num = int(input("Enter number:"))

for row in range(1,num+1):
   
    for col in range(num-row):
        print(" ", end="")
    for col in range(0,row):
        if (((num-row)+col)%2) == 0:
            print("1 ", end="")
        elif (((num-row)+col) %2) == 1:
            print("0 ", end="")
    
    print(" ")