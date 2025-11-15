t=int(input("Enter a time :"))
if t>0:
    if t<=12:
        print(t,"AM")
if t>12:
    if t<=24:
        print(t-12,"PM")
if t>24:
    print("invalid")