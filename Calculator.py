a=float(input("Enter the 1st No. :"))
b=float(input("Enter the 2nd No. :"))
string=str(input("what you want to do?")).lower()

if string=="sum"or"add"or"+":
    print(f"The Sum is {(a+b)}")
elif string=="minus"or"-"or"subtraction":
    print("The difference is",float(a-b))
    if a<b:
        print("Please place the bigger no. first")
elif string=="divide"or"/"or"division":
    print("The remainder is",float(a/b))
    if a<b:
        print("Please place the bigger no. first if u can for better results")
elif string=="multiply"or"*"or"multiplication":
    print("The product is",float(a*b))
else:
    print("Sorry, invalid command!")