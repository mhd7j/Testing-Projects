answer = int(input("\"player1\"please insert the number (0-100) :"))

is_correct = False
try_count = 0

while try_count < 6 and is_correct == False:
    guess = int(input("\"player2\"please guess a number :"))
    if guess == answer:
        print("\"player2!\"\n\"YOU WON\"")
        is_correct = True
    elif guess > answer:
        print("your guess is greater than the target.")
        try_count += 1
    else:
        print("your guess is smaller than the target.")
        try_count += 1
if is_correct == False:
    print("\"player1!\"\n\"YOU WON\"")
