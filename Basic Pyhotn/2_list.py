 friends = ["Raj", "Amit", "Samir", "Kiran", "Nisha"]                          # create list of friends
print("Original friends list:", friends)

friends.insert(0, "Ravi")                                                     # add 2 friend names at beginning
friends.insert(0, "Sneha")
print("After adding 2 friends at beginning:", friends)

friends.append("Mohan")                                                      # add 2 friends names at last
friends.append("Priya")
print("After adding 2 friends at last:", friends)

relatives = ["Uncle", "Aunty", "Cousin"]                                      # create another list of relatives

friends.extend(relatives)                                                    # append relative list into friend
print("After appending relatives list:", friends)

del friends[0]                                                               # remove 1st item in friend
print("After removing 1st item:", friends)
                                                     
    friends.remove("Samir")                                                  # remove friend whose name is 'Samir'
print("After removing 'Samir':", friends)


friends.clear()                                                             # clear
print("After clearing list:", friends)

