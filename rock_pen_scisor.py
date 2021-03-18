player1 = input("A' Give your name = ")
choice1 = input(str(player1) + " (R)ock, (S)cissors=, (P)aper =").lower()
player2 = input("B' Give your name = ")
choice2 = input(str(player2) + " (R)ock, (S)cissors=, (P)aper = ").lower()
wins1 = wins2 = 0
while choice1 != 'end' and choice2 != 'end':
    #Update Score
    if choice1 == 'r':
        if choice2 == 's':
            wins1 += 1
        elif choice2 == 'p':
            wins2 += 1
        else:
            pass
    elif choice1 == 's':
        if choice2 == 'p':
            wins1 += 1
        elif choice2 == 'r':
            wins2 += 1
        else:pass
    elif choice1 == 'p':
        if choice2 == 'r':
            wins1 += 1
        elif choice2 == 's':
            wins2 += 1
        else:
            pass
    choice1= input(str(player1) + " (R)ock, (S)cissors=, (P)aper =").lower()
    choice2 = input(str(player2) + " (R)ock, (S)cissors=, (P)aper = ").lower()
print (player1, wins1)
print (player2, wins2)
