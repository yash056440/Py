p1 = input("Enter person1 name : ")
d1 = int(input("Enter day (Birth day): "))
m1 = input("Enter month (Birth month): ")

p2 = input("Enter person2 name : ")
d2 = int(input("Enter day (Birth day): "))
m2 = input("Enter month (Birth month): ")

one = "Aries"
two = "Taurus"
three = "Gemini"
four = "Cancer"
five = "Leo"
six = "Virgo"
seven = "Libra"
eight = "Scorpio"
nine = "Sagittarius"
ten = "Capricorn"
eleven = "Aquarius"
twelve = "Pisces"

zs1 = ""
zs2 = ""

if m1 == "march":
    if d1 >= 21:
        zs1 = one
    else:
        zs1 = twelve
elif m1 == "april":
    if d1 <= 19:
        zs1 = one
    else:
        zs1 = two
elif m1 == "may":
    if d1 <= 20:
        zs1 = two
    else:
        zs1 = three
elif m1 == "june":
    if d1 <= 21:
        zs1 = three
    else:
        zs1 = four
elif m1 == "july":
    if d1 <= 22:
        zs1 = four
    else:
        zs1 = five
elif m1 == "august":
    if d1 <= 22:
        zs1 = five
    else:
        zs1 = six
elif m1 == "september":
    if d1 <= 22:
        zs1 = six
    else:
        zs1 = seven
elif m1 == "october":
    if d1 <= 22:
        zs1 = seven
    else:
        zs1 = eight
elif m1 == "november":
    if d1 <= 21:
        zs1 = eight
    else:
        zs1 = nine
elif m1 == "december":
    if d1 <= 21:
        zs1 = nine
    else:
        zs1 = ten
elif m1 == "january":
    if d1 <= 19:
        zs1 = ten
    else:
        zs1 = eleven
elif m1 == "february":
    if d1 <= 18:
        zs1 = eleven
    else:
        zs1 = twelve
else:
    zs1 = "Invalid month"

print(f"{p1}'s zodiac sign is {zs1}")

if m2 == "march":
    if d2 >= 21:
        zs2 = one
    else:
        zs2 = twelve
elif m2 == "april":
    if d2 <= 19:
        zs2 = one
    else:
        zs2 = two
elif m2 == "may":
    if d2 <= 20:
        zs2 = two
    else:
        zs2 = three
elif m2 == "june":
    if d2 <= 21:
        zs2 = three
    else:
        zs2 = four
elif m2 == "july":
    if d2 <= 22:
        zs2 = four
    else:
        zs2 = five
elif m2 == "august":
    if d2 <= 22:
        zs2 = five
    else:
        zs2 = six
elif m2 == "september":
    if d2 <= 22:
        zs2 = six
    else:
        zs2 = seven
elif m2 == "october":
    if d2 <= 22:
        zs2 = seven
    else:
        zs2 = eight
elif m2 == "november":
    if d2 <= 21:
        zs2 = eight
    else:
        zs2 = nine
elif m2 == "december":
    if d2 <= 21:
        zs2 = nine
    else:
        zs2 = ten
elif m2 == "january":
    if d2 <= 19:
        zs2 = ten
    else:
        zs2 = eleven
elif m2 == "february":
    if d2 <= 18:
        zs2 = eleven
    else:
        zs2 = twelve
else:
    zs2 = "Invalid month"

print(f"{p2}'s zodiac sign is {zs2}")

print(p1, "->", zs1)
print(p2, "->", zs2)



# 1
if (zs1 == "Aries" and zs2 == "Aries") or (zs2 == "Aries" and zs1 == "Aries"):
    print("Great")
elif (zs1 == "Aries" and zs2 == "Leo") or (zs2 == "Aries" and zs1 == "Leo"):
    print("Great")
elif (zs1 == "Aries" and zs2 == "Sagittarius") or (zs2 == "Aries" and zs1 == "Sagittarius"):
    print("Great")
elif (zs1 == "Aries" and zs2 == "Taurus") or (zs2 == "Aries" and zs1 == "Taurus"):
    print("No")
elif (zs1 == "Aries" and zs2 == "Virgo") or (zs2 == "Aries" and zs1 == "Virgo"):
    print("Good")
elif (zs1 == "Aries" and zs2 == "Capricorn") or (zs2 == "Aries" and zs1 == "Capricorn"):
    print("No")
elif (zs1 == "Aries" and zs2 == "Gemini") or (zs2 == "Aries" and zs1 == "Gemini"):
    print("Great")
elif (zs1 == "Aries" and zs2 == "Libra") or (zs2 == "Aries" and zs1 == "Libra"):
    print("Great")
elif (zs1 == "Aries" and zs2 == "Aquarius") or (zs2 == "Aries" and zs1 == "Aquarius"):
    print("Great")
elif (zs1 == "Aries" and zs2 == "Cancer") or (zs2 == "Aries" and zs1 == "Cancer"):
    print("No")
elif (zs1 == "Aries" and zs2 == "Scorpio") or (zs2 == "Aries" and zs1 == "Scorpio"):
    print("No")
elif (zs1 == "Aries" and zs2 == "Pisces") or (zs2 == "Aries" and zs1 == "Pisces"):
    print("Good")

# 2
elif (zs1 == "Leo" and zs2 == "Aries") or (zs2 == "Leo" and zs1 == "Aries"):
    print("Great")
elif (zs1 == "Leo" and zs2 == "Leo") or (zs2 == "Leo" and zs1 == "Leo"):
    print("Great")
elif (zs1 == "Leo" and zs2 == "Sagittarius") or (zs2 == "Leo" and zs1 == "Sagittarius"):
    print("Great")
elif (zs1 == "Leo" and zs2 == "Taurus") or (zs2 == "Leo" and zs1 == "Taurus"):
    print("Good")
elif (zs1 == "Leo" and zs2 == "Virgo") or (zs2 == "Leo" and zs1 == "Virgo"):
    print("No")
elif (zs1 == "Leo" and zs2 == "Capricorn") or (zs2 == "Leo" and zs1 == "Capricorn"):
    print("No")
elif (zs1 == "Leo" and zs2 == "Gemini") or (zs2 == "Leo" and zs1 == "Gemini"):
    print("Great")
elif (zs1 == "Leo" and zs2 == "Libra") or (zs2 == "Leo" and zs1 == "Libra"):
    print("Great")
elif (zs1 == "Leo" and zs2 == "Aquarius") or (zs2 == "Leo" and zs1 == "Aquarius"):
    print("Good")
elif (zs1 == "Leo" and zs2 == "Cancer") or (zs2 == "Leo" and zs1 == "Cancer"):
    print("Good")
elif (zs1 == "Leo" and zs2 == "Scorpio") or (zs2 == "Leo" and zs1 == "Scorpio"):
    print("Good")
elif (zs1 == "Leo" and zs2 == "Pisces") or (zs2 == "Leo" and zs1 == "Pisces"):
    print("Good")

# 3
elif (zs1 == "Sagittarius" and zs2 == "Aries") or (zs2 == "Sagittarius" and zs1 == "Aries"):
    print("Great")
elif (zs1 == "Sagittarius" and zs2 == "Leo") or (zs2 == "Sagittarius" and zs1 == "Leo"):
    print("Great")
elif (zs1 == "Sagittarius" and zs2 == "Sagittarius") or (zs2 == "Sagittarius" and zs1 == "Sagittarius"):
    print("Great")
elif (zs1 == "Sagittarius" and zs2 == "Taurus") or (zs2 == "Sagittarius" and zs1 == "Taurus"):
    print("No")
elif (zs1 == "Sagittarius" and zs2 == "Virgo") or (zs2 == "Sagittarius" and zs1 == "Virgo"):
    print("No")
elif (zs1 == "Sagittarius" and zs2 == "Capricorn") or (zs2 == "Sagittarius" and zs1 == "Capricorn"):
    print("No")
elif (zs1 == "Sagittarius" and zs2 == "Gemini") or (zs2 == "Sagittarius" and zs1 == "Gemini"):
    print("Great")
elif (zs1 == "Sagittarius" and zs2 == "Libra") or (zs2 == "Sagittarius" and zs1 == "Libra"):
    print("Great")
elif (zs1 == "Sagittarius" and zs2 == "Aquarius") or (zs2 == "Sagittarius" and zs1 == "Aquarius"):
    print("Great")
elif (zs1 == "Sagittarius" and zs2 == "Cancer") or (zs2 == "Sagittarius" and zs1 == "Cancer"):
    print("Good")
elif (zs1 == "Sagittarius" and zs2 == "Scorpio") or (zs2 == "Sagittarius" and zs1 == "Scorpio"):
    print("Good")
elif (zs1 == "Sagittarius" and zs2 == "Pisces") or (zs2 == "Sagittarius" and zs1 == "Pisces"):
    print("Good")

# 4
elif (zs1 == "Taurus" and zs2 == "Aries") or (zs2 == "Taurus" and zs1 == "Aries"):
    print("No")
elif (zs1 == "Taurus" and zs2 == "Leo") or (zs2 == "Taurus" and zs1 == "Leo"):
    print("Good")
elif (zs1 == "Taurus" and zs2 == "Sagittarius") or (zs2 == "Taurus" and zs1 == "Sagittarius"):
    print("No")
elif (zs1 == "Taurus" and zs2 == "Taurus") or (zs2 == "Taurus" and zs1 == "Taurus"):
    print("Great")
elif (zs1 == "Taurus" and zs2 == "Virgo") or (zs2 == "Taurus" and zs1 == "Virgo"):
    print("Great")
elif (zs1 == "Taurus" and zs2 == "Capricorn") or (zs2 == "Taurus" and zs1 == "Capricorn"):
    print("Great")
elif (zs1 == "Taurus" and zs2 == "Gemini") or (zs2 == "Taurus" and zs1 == "Gemini"):
    print("No")
elif (zs1 == "Taurus" and zs2 == "Libra") or (zs2 == "Taurus" and zs1 == "Libra"):
    print("Good")
elif (zs1 == "Taurus" and zs2 == "Aquarius") or (zs2 == "Taurus" and zs1 == "Aquarius"):
    print("No")
elif (zs1 == "Taurus" and zs2 == "Cancer") or (zs2 == "Taurus" and zs1 == "Cancer"):
    print("Great")
elif (zs1 == "Taurus" and zs2 == "Scorpio") or (zs2 == "Taurus" and zs1 == "Scorpio"):
    print("Great")
elif (zs1 == "Taurus" and zs2 == "Pisces") or (zs2 == "Taurus" and zs1 == "Pisces"):
    print("Great")

# 5
elif (zs1 == "Virgo" and zs2 == "Aries") or (zs2 == "Virgo" and zs1 == "Aries"):
    print("No")
elif (zs1 == "Virgo" and zs2 == "Leo") or (zs2 == "Virgo" and zs1 == "Leo"):
    print("Good")
elif (zs1 == "Virgo" and zs2 == "Sagittarius") or (zs2 == "Virgo" and zs1 == "Sagittarius"):
    print("No")
elif (zs1 == "Virgo" and zs2 == "Taurus") or (zs2 == "Virgo" and zs1 == "Taurus"):
    print("Great")
elif (zs1 == "Virgo" and zs2 == "Virgo") or (zs2 == "Virgo" and zs1 == "Virgo"):
    print("Great")
elif (zs1 == "Virgo" and zs2 == "Capricorn") or (zs2 == "Virgo" and zs1 == "Capricorn"):
    print("Great")
elif (zs1 == "Virgo" and zs2 == "Gemini") or (zs2 == "Virgo" and zs1 == "Gemini"):
    print("No")
elif (zs1 == "Virgo" and zs2 == "Libra") or (zs2 == "Virgo" and zs1 == "Libra"):
    print("No")
elif (zs1 == "Virgo" and zs2 == "Aquarius") or (zs2 == "Virgo" and zs1 == "Aquarius"):
    print("Good")
elif (zs1 == "Virgo" and zs2 == "Cancer") or (zs2 == "Virgo" and zs1 == "Cancer"):
    print("Great")
elif (zs1 == "Virgo" and zs2 == "Scorpio") or (zs2 == "Virgo" and zs1 == "Scorpio"):
    print("Great")
elif (zs1 == "Virgo" and zs2 == "Pisces") or (zs2 == "Virgo" and zs1 == "Pisces"):
    print("Good+No")

# 6
elif (zs1 == "Capricorn" and zs2 == "Aries") or (zs2 == "Capricorn" and zs1 == "Aries"):
    print("No")
elif (zs1 == "Capricorn" and zs2 == "Leo") or (zs2 == "Capricorn" and zs1 == "Leo"):
    print("Good")
elif (zs1 == "Capricorn" and zs2 == "Sagittarius") or (zs2 == "Capricorn" and zs1 == "Sagittarius"):
    print("No")
elif (zs1 == "Capricorn" and zs2 == "Taurus") or (zs2 == "Capricorn" and zs1 == "Taurus"):
    print("Great")
elif (zs1 == "Capricorn" and zs2 == "Virgo") or (zs2 == "Capricorn" and zs1 == "Virgo"):
    print("Great")
elif (zs1 == "Capricorn" and zs2 == "Capricorn") or (zs2 == "Capricorn" and zs1 == "Capricorn"):
    print("Great")
elif (zs1 == "Capricorn" and zs2 == "Gemini") or (zs2 == "Capricorn" and zs1 == "Gemini"):
    print("No")
elif (zs1 == "Capricorn" and zs2 == "Libra") or (zs2 == "Capricorn" and zs1 == "Libra"):
    print("Good")
elif (zs1 == "Capricorn" and zs2 == "Aquarius") or (zs2 == "Capricorn" and zs1 == "Aquarius"):
    print("No")
elif (zs1 == "Capricorn" and zs2 == "Cancer") or (zs2 == "Capricorn" and zs1 == "Cancer"):
    print("Great")
elif (zs1 == "Capricorn" and zs2 == "Scorpio") or (zs2 == "Capricorn" and zs1 == "Scorpio"):
    print("Great")
elif (zs1 == "Capricorn" and zs2 == "Pisces") or (zs2 == "Capricorn" and zs1 == "Pisces"):
    print("Great")

# 7
elif (zs1 == "Gemini" and zs2 == "Aries") or (zs2 == "Gemini" and zs1 == "Aries"):
    print("Great")
elif (zs1 == "Gemini" and zs2 == "Leo") or (zs2 == "Gemini" and zs1 == "Leo"):
    print("Great")
elif (zs1 == "Gemini" and zs2 == "Sagittarius") or (zs2 == "Gemini" and zs1 == "Sagittarius"):
    print("Good")
elif (zs1 == "Gemini" and zs2 == "Taurus") or (zs2 == "Gemini" and zs1 == "Taurus"):
    print("No")
elif (zs1 == "Gemini" and zs2 == "Virgo") or (zs2 == "Gemini" and zs1 == "Virgo"):
    print("Good")
elif (zs1 == "Gemini" and zs2 == "Capricorn") or (zs2 == "Gemini" and zs1 == "Capricorn"):
    print("Good")
elif (zs1 == "Gemini" and zs2 == "Gemini") or (zs2 == "Gemini" and zs1 == "Gemini"):
    print("Great")
elif (zs1 == "Gemini" and zs2 == "Libra") or (zs2 == "Gemini" and zs1 == "Libra"):
    print("Great")
elif (zs1 == "Gemini" and zs2 == "Aquarius") or (zs2 == "Gemini" and zs1 == "Aquarius"):
    print("Great")
elif (zs1 == "Gemini" and zs2 == "Cancer") or (zs2 == "Gemini" and zs1 == "Cancer"):
    print("No")
elif (zs1 == "Gemini" and zs2 == "Scorpio") or (zs2 == "Gemini" and zs1 == "Scorpio"):
    print("No")
elif (zs1 == "Gemini" and zs2 == "Pisces") or (zs2 == "Gemini" and zs1 == "Pisces"):
    print("No")

# 8
elif (zs1 == "Libra" and zs2 == "Aries") or (zs2 == "Libra" and zs1 == "Aries"):
    print("Good")
elif (zs1 == "Libra" and zs2 == "Leo") or (zs2 == "Libra" and zs1 == "Leo"):
    print("Great")
elif (zs1 == "Libra" and zs2 == "Sagittarius") or (zs2 == "Libra" and zs1 == "Sagittarius"):
    print("Great")
elif (zs1 == "Libra" and zs2 == "Taurus") or (zs2 == "Libra" and zs1 == "Taurus"):
    print("Good")
elif (zs1 == "Libra" and zs2 == "Virgo") or (zs2 == "Libra" and zs1 == "Virgo"):
    print("No")
elif (zs1 == "Libra" and zs2 == "Capricorn") or (zs2 == "Libra" and zs1 == "Capricorn"):
    print("No")
elif (zs1 == "Libra" and zs2 == "Gemini") or (zs2 == "Libra" and zs1 == "Gemini"):
    print("Great")
elif (zs1 == "Libra" and zs2 == "Libra") or (zs2 == "Libra" and zs1 == "Libra"):
    print("Great")
elif (zs1 == "Libra" and zs2 == "Aquarius") or (zs2 == "Libra" and zs1 == "Aquarius"):
    print("Great")
elif (zs1 == "Libra" and zs2 == "Cancer") or (zs2 == "Libra" and zs1 == "Cancer"):
    print("No")
elif (zs1 == "Libra" and zs2 == "Scorpio") or (zs2 == "Libra" and zs1 == "Scorpio"):
    print("No")
elif (zs1 == "Libra" and zs2 == "Pisces") or (zs2 == "Libra" and zs1 == "Pisces"):
    print("Good")

# 9
elif (zs1 == "Aquarius" and zs2 == "Aries") or (zs2 == "Aquarius" and zs1 == "Aries"):
    print("Great")
elif (zs1 == "Aquarius" and zs2 == "Leo") or (zs2 == "Aquarius" and zs1 == "Leo"):
    print("Great")
elif (zs1 == "Aquarius" and zs2 == "Sagittarius") or (zs2 == "Aquarius" and zs1 == "Sagittarius"):
    print("Great")
elif (zs1 == "Aquarius" and zs2 == "Taurus") or (zs2 == "Aquarius" and zs1 == "Taurus"):
    print("No")
elif (zs1 == "Aquarius" and zs2 == "Virgo") or (zs2 == "Aquarius" and zs1 == "Virgo"):
    print("No")
elif (zs1 == "Aquarius" and zs2 == "Capricorn") or (zs2 == "Aquarius" and zs1 == "Capricorn"):
    print("No")
elif (zs1 == "Aquarius" and zs2 == "Gemini") or (zs2 == "Aquarius" and zs1 == "Gemini"):
    print("Great")
elif (zs1 == "Aquarius" and zs2 == "Libra") or (zs2 == "Aquarius" and zs1 == "Libra"):
    print("Great")
elif (zs1 == "Aquarius" and zs2 == "Aquarius") or (zs2 == "Aquarius" and zs1 == "Aquarius"):
    print("Great")
elif (zs1 == "Aquarius" and zs2 == "Cancer") or (zs2 == "Aquarius" and zs1 == "Cancer"):
    print("No")
elif (zs1 == "Aquarius" and zs2 == "Scorpio") or (zs2 == "Aquarius" and zs1 == "Scorpio"):
    print("Good")
elif (zs1 == "Aquarius" and zs2 == "Pisces") or (zs2 == "Aquarius" and zs1 == "Pisces") :
    print("Good")

# 10
elif (zs1 == "Cancer" and zs2 == "Aries") or (zs2 == "Cancer" and zs1 == "Aries"):
    print("No")
elif (zs1 == "Cancer" and zs2 == "Leo") or (zs2 == "Cancer" and zs1 == "Leo"):
    print("Good")
elif (zs1 == "Cancer" and zs2 == "Sagittarius") or (zs2 == "Cancer" and zs1 == "Sagittarius"):
    print("Good")
elif (zs1 == "Cancer" and zs2 == "Taurus") or (zs2 == "Cancer" and zs1 == "Taurus"):
    print("Great")
elif (zs1 == "Cancer" and zs2 == "Virgo") or (zs2 == "Cancer" and zs1 == "Virgo"):
    print("Great")
elif (zs1 == "Cancer" and zs2 == "Capricorn") or (zs2 == "Cancer" and zs1 == "Capricorn"):
    print("Great")
elif (zs1 == "Cancer" and zs2 == "Gemini") or (zs2 == "Cancer" and zs1 == "Gemini"):
    print("No")
elif (zs1 == "Cancer" and zs2 == "Libra") or (zs2 == "Cancer" and zs1 == "Libra"):
    print("No")
elif (zs1 == "Cancer" and zs2 == "Aquarius") or (zs2 == "Cancer" and zs1 == "Aquarius"):
    print("No")
elif (zs1 == "Cancer" and zs2 == "Cancer") or (zs2 == "Cancer" and zs1 == "Cancer"):
    print("Great")
elif (zs1 == "Cancer" and zs2 == "Scorpio") or (zs2 == "Cancer" and zs1 == "Scorpio"):
    print("Great")
elif (zs1 == "Cancer" and zs2 == "Pisces") or (zs2 == "Cancer" and zs1 == "Pisces"):
    print("Great")

# 11
elif (zs1 == "Scorpio" and zs2 == "Aries") or (zs2 == "Scorpio" and zs1 == "Aries"):
    print("Good")
elif (zs1 == "Scorpio" and zs2 == "Leo") or (zs2 == "Scorpio" and zs1 == "Leo"):
    print("Good")
elif (zs1 == "Scorpio" and zs2 == "Sagittarius") or (zs2 == "Scorpio" and zs1 == "Sagittarius"):
    print("No")
elif (zs1 == "Scorpio" and zs2 == "Taurus") or (zs2 == "Scorpio" and zs1 == "Taurus"):
    print("Great")
elif (zs1 == "Scorpio" and zs2 == "Virgo") or (zs2 == "Scorpio" and zs1 == "Virgo"):
    print("Great")
elif (zs1 == "Scorpio" and zs2 == "Capricorn") or (zs2 == "Scorpio" and zs1 == "Capricorn"):
    print("Great")
elif (zs1 == "Scorpio" and zs2 == "Gemini") or (zs2 == "Scorpio" and zs1 == "Gemini"):
    print("No")
elif (zs1 == "Scorpio" and zs2 == "Libra") or (zs2 == "Scorpio" and zs1 == "Libra"):
    print("No")
elif (zs1 == "Scorpio" and zs2 == "Aquarius") or (zs2 == "Scorpio" and zs1 == "Aquarius"):
    print("No")
elif (zs1 == "Scorpio" and zs2 == "Cancer") or (zs2 == "Scorpio" and zs1 == "Cancer"):
    print("Great")
elif (zs1 == "Scorpio" and zs2 == "Scorpio") or (zs2 == "Scorpio" and zs1 == "Scorpio"):
    print("Great")
elif (zs1 == "Scorpio" and zs2 == "Pisces") or (zs2 == "Scorpio" and zs1 == "Pisces"):
    print("Great")

# 12
elif (zs1 == "Pisces" and zs2 == "Aries") or (zs2 == "Pisces" and zs1 == "Aries"):
    print("Good")
elif (zs1 == "Pisces" and zs2 == "Leo") or (zs2 == "Pisces" and zs1 == "Leo"):
    print("Good")
elif (zs1 == "Pisces" and zs2 == "Sagittarius") or (zs2 == "Pisces" and zs1 == "Sagittarius"):
    print("Good")
elif (zs1 == "Pisces" and zs2 == "Taurus") or (zs2 == "Pisces" and zs1 == "Taurus"):
    print("Great")
elif (zs1 == "Pisces" and zs2 == "Virgo") or (zs2 == "Pisces" and zs1 == "Virgo"):
    print("Good")
elif (zs1 == "Pisces" and zs2 == "Capricorn") or (zs2 == "Pisces" and zs1 == "Capricorn"):
    print("Great")
elif (zs1 == "Pisces" and zs2 == "Gemini") or (zs2 == "Pisces" and zs1 == "Gemini"):
    print("No")
elif (zs1 == "Pisces" and zs2 == "Libra") or (zs2 == "Pisces" and zs1 == "Libra"):
    print("No")
elif (zs1 == "Pisces" and zs2 == "Aquarius") or (zs2 == "Pisces" and zs1 == "Aquarius"):
    print("No")
elif (zs1 == "Pisces" and zs2 == "Cancer") or (zs2 == "Pisces" and zs1 == "Cancer"):
    print("Great")
elif (zs1 == "Pisces" and zs2 == "Scorpio") or (zs2 == "Pisces" and zs1 == "Scorpio"):
    print("Great")
elif (zs1 == "Pisces" and zs2 == "Pisces") or (zs2 == "Pisces" and zs1 == "Pisces"):
    print("Great")
