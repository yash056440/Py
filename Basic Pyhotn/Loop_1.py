num = int(input("Enter number :"))
c = 2

while (c > 1) and (c < num):                # c "count"
    if (num / c)  == (num // c):
        print("Not Prime")
        break                               # here, when if condition is over then count++ 
    c += 1
else :
    print("Prime")
       



