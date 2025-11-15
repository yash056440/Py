num = int(input("Enter number:"))


for r in range(1,num+1):

    if r==1 or r==num-1:
        for c in range(1,num+1):
            print("*",end="")
    elif ((num//2)+1)==r:
        for c in range(1,num+1):
            if c==1 or c==((num//2)+1) or c==num:
                print("*")
    else:
        for c in range(1,num+1):
            if c==1 or c==num:
                print("*")
