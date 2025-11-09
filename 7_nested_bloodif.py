donor = input("Enter donor blood type : ")
receiver = input("Enter receiver blood type : ")

if donor == "O-":
    print("Donate")
elif receiver == "AB+":
    print("Donate")
elif donor == receiver:
    print("Donate")
elif donor == "O+" and (receiver == "O+" or receiver == "A+" or receiver == "B+" or receiver == "AB+"):
    print("Donate")
elif donor == "A-" and (receiver == "A+" or receiver == "A-" or receiver == "AB+" or receiver == "AB-"):
    print("Donate")
elif donor == "A+" and (receiver == "A+" or receiver == "AB+"):
    print("Donate")
elif donor == "B-" and (receiver == "B+" or receiver == "B-" or receiver == "AB+" or receiver == "AB-"):
    print("Donate")
elif donor == "B+" and (receiver == "B+" or receiver == "AB+"):
    print("Donate")
elif donor == "AB-" and (receiver == "AB+" or receiver == "AB-"):
    print("Donate")
elif donor == "AB+" and receiver == "AB+":
    print("Donate")
else:
    print("Not Donate")
