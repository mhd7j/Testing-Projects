a = float(input("enter your first number..."))
opt = input("whats your operator?")
b = float (input("enter your second number..."))

if opt == "+":
    print(a+b)
elif opt == "*":
    print(a*b)
elif opt == "-":
    print(a-b)
elif opt == "/":
    if b == 0:
        print("WRONG!")
    else:
        print(a/b)
elif opt == "**":
    print(a**b)
elif opt == "%":
    print(a%b)
else:
    print("THE OPERATION IS NOT :/")
