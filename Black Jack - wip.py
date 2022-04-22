import random
print("Black Jack")
cash = 500
x = 0
print("you have", cash, "$")
while x == 0:
    bid = int(input("Enter the amount you want to bid: \n"))
    if cash<bid:
        print("You don't have enough cash")
    elif bid < 1:
        print("You have to bid some cash")
    else:
        cash = cash - bid
        print("you now have", cash, "$")
        x = x + 1
print("Dealing out your hand...")
s = random.randint(1,4)
if s == 1:
    s = "Spades"
elif s == 2:
    s = "Diamonds"
elif s == 3:
    s = "Hearts"
else:
    s = "Clubs"
c = random.randint(2,13)
if c < 10:
    print(c)
elif c == 10:
    c = "Jack"
elif c == 11:
    c = "Queen"
elif c == 12:
    c = "King"
else:
    c = "Ace"
print(c, "of", s)
