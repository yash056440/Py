ttp = int(input("Enter train ticket price:"))
km = int(input("Enter KM :"))
person = int(input("Enter total person :"))
avg = int(input("Enter average of car :"))

tttp = ttp * person
tcc = (km/avg) * 97

print("total train ticket price:",tttp)
print("total car cost :",tcc)

if tttp> tcc:
    print("a car is cheaperthan train")
else :
    print("a train is cheaper than car")