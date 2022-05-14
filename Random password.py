import random

number = "0123456789"
symbol = "[](){}#*;.-_"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

all = lower + upper + number + symbol
length = 9
password = "".join(random.sample(all,length))
print("the password you generated is : " , password)
