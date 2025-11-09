
friends = ["Y", "A", "S", "H", "YASH"]                                           #list


print("All friends:", friends)                                               # Display the list

print("First friend:", friends[0])                                           # Display 1st friend

print("Last friend:", friends[4])                                            # Display last friend

friends[0] = "yash"                                                         # Replace 1st friend
print("After replacing first friend:", friends)

del friends[4]                                                               # Remove last value
print("After removing last friend:", friends)

print("First 3 friends:", friends[:3])                                       # Display 1st 3 values 

print("Last 3 friends:", friends[1:])                                       # Display last 3 values 