# num= int(input("Enter number:"))


# for r in range(1,num+1):
#         if r==1 or r==num:
#             for c in range(1,num+1):
#                 print("* ",end="")
        
#         elif ((num//2)+1)==r:
#             for c in range(1,num+1):
#                 if c==1 or c==((num//2)+1) or c==num:
#                     print("*",end="")
#                 else:
#                     print(" ",end="")
#         else:
#             for c in range(1,num+1):
#                 if c==1 or c==num:
#                     print("*",end="")
#                 else:
#                     print(" ",end="")
#         print()

n=5
for i in range(n):
    for j in range(n):
        if (i==(n//2) and j==(n//2)) or i==0 or i==n-1 or j==0 or j==n-1 :
            print("* ",end="")
        else:
            print("  ",end="")

    print()