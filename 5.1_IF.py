print("Enter 1st farm length and width")
l1 = int(input("Length: "))
w1 = int(input("Width: "))
area1 = l1 * w1
print("Farm 1 area is:", area1)

print("\nEnter 2nd farm length and width")
l2 = int(input("Length: "))
w2 = int(input("Width: "))
area2 = l2 * w2
print("Farm 2 area is:", area2)

if area1 > area2:
    print("Farm 1 is", area1 - area2, "square feet bigger than Farm 2.")
elif area1 < area2:
    print("Farm 2 is", area2 - area1, "square feet bigger than Farm 1.")
else:
    print("Both farms have the same area.")
