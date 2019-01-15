from random import randint, choice

print("BATTLESHIP GAME\nThe objective is to sink the opponent's ships before the oppenent sinks yours.")
while True:
    try:
        x = int(input("Input 1 for 1-player game or 2 for 2-player game: "))
    except ValueError:
        print("Gametype doesn't exist. Please retry")
        continue
    if (x == 1 or x == 2):
        break
    else:
        print("Gametype doesn't exist. Please retry")

D1 = {"a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0,
      "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0,
      "c1": 0, "c2": 0, "c3": 0, "c4": 0, "c5": 0,
      "d1": 0, "d2": 0, "d3": 0, "d4": 0, "d5": 0,
      "e1": 0, "e2": 0, "e3": 0, "e4": 0, "e5": 0}

D2 = {"a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0,
      "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0,
      "c1": 0, "c2": 0, "c3": 0, "c4": 0, "c5": 0,
      "d1": 0, "d2": 0, "d3": 0, "d4": 0, "d5": 0,
      "e1": 0, "e2": 0, "e3": 0, "e4": 0, "e5": 0}

###############SINGLEPLAYER###############
if x == 1:
    for i in range(1,6):
        y = input("Player 1 enter the position of your ship no " + str(i) + ": ")
        if y in D1.keys() and D1[y] != 1:
            D1[y] =1
        else:
            while y not in D1.keys() or D1[y] == 1:
                y = input("Invalid position, or position already taken. Try again: ")
                if (y in D1.keys() and not D1[y] == 1):
                    D1[y] = 1
                    break
                elif y not in D1.keys() or D1[y] == 1:
                    pass
    for i in range(1,6):
        randomChar = choice('abcde')
        randomNum = str(randint(1,5))
        randomShip = randomChar + randomNum
        if (randomShip not in D2.keys() or D2[randomShip] == 1):
            randomChar = choice('abcde')
            randomNum = str(randint(1,5))
            randomShip = randomChar + randomNum
            if D2[randomShip] == 0:
                D2[randomShip] = 1
        else:
            D2[randomShip] = 1
    startingPlayer = randint(1,2)
    print("\n"*500)
    L1,L2,score1,score2 = [],[],0,0
    while not (score1 == 5 or score2 == 5):
        if startingPlayer == 1:
            print(" "*3 + "P1" + " "*8 + "P2\n" +" "*2 + "12345" + " "*5 + "12345\n" + "a" + " " + "%s"*5 % ("o" if D1["a1"] == 3 else "x" if D1["a1"] == 2 else " ", "o" if D1["a2"] == 3 else "x" if D1["a2"] == 2 else " ", "o" if D1["a3"] == 3 else "x" if D1["a3"] == 2 else " ", "o" if D1["a4"] == 3 else "x" if D1["a4"] == 2 else " ", "o" if D1["a5"] == 3 else "x" if D1["a5"] == 2 else " ") + " "*3 + "a " + "%s"*5 % ("o" if D2["a1"] == 3 else "x" if D2["a1"] == 2 else " ", "o" if D2["a2"] == 3 else "x" if D2["a2"] == 2 else " ", "o" if D2["a3"] == 3 else "x" if D2["a3"] == 2 else " ", "o" if D2["a4"] == 3 else "x" if D2["a4"] == 2 else " ", "o" if D2["a5"] == 3 else "x" if D2["a5"] == 2 else " ") + "\nb" + " " + "%s"*5 % ("o" if D1["b1"] == 3 else "x" if D1["b1"] == 2 else " ", "o" if D1["b2"] == 3 else "x" if D1["b2"] == 2 else " ", "o" if D1["b3"] == 3 else "x" if D1["b3"] == 2 else " ", "o" if D1["b4"] == 3 else "x" if D1["b4"] == 2 else " ", "o" if D1["b5"] == 3 else "x" if D1["b5"] == 2 else " ") + " "*3 + "b " + "%s"*5 % ("o" if D2["b1"] == 3 else "x" if D2["b1"] == 2 else " ", "o" if D2["b2"] == 3 else "x" if D2["b2"] == 2 else " ", "o" if D2["b3"] == 3 else "x" if D2["b3"] == 2 else " ", "o" if D2["b4"] == 3 else "x" if D2["b4"] == 2 else " ", "o" if D2["b5"] == 3 else "x" if D2["b5"] == 2 else " ") + "\nc" + " " + "%s"*5 % ("o" if D1["c1"] == 3 else "x" if D1["c1"] == 2 else " ", "o" if D1["c2"] == 3 else "x" if D1["c2"] == 2 else " ", "o" if D1["c3"] == 3 else "x" if D1["c3"] == 2 else " ", "o" if D1["c4"] == 3 else "x" if D1["c4"] == 2 else " ", "o" if D1["c5"] == 3 else "x" if D1["c5"] == 2 else " ") + " "*3 + "c " + "%s"*5 % ("o" if D2["c1"] == 3 else "x" if D2["c1"] == 2 else " ", "o" if D2["c2"] == 3 else "x" if D2["c2"] == 2 else " ", "o" if D2["c3"] == 3 else "x" if D2["c3"] == 2 else " ", "o" if D2["c4"] == 3 else "x" if D2["c4"] == 2 else " ", "o" if D2["c5"] == 3 else "x" if D2["c5"] == 2 else " ") + "\nd" + " " + "%s"*5 % ("o" if D1["d1"] == 3 else "x" if D1["d1"] == 2 else " ", "o" if D1["d2"] == 3 else "x" if D1["d2"] == 2 else " ", "o" if D1["d3"] == 3 else "x" if D1["d3"] == 2 else " ", "o" if D1["d4"] == 3 else "x" if D1["d4"] == 2 else " ", "o" if D1["d5"] == 3 else "x" if D1["d5"] == 2 else " ") + " "*3 + "d " + "%s"*5 % ("o" if D2["d1"] == 3 else "x" if D2["d1"] == 2 else " ", "o" if D2["d2"] == 3 else "x" if D2["d2"] == 2 else " ", "o" if D2["d3"] == 3 else "x" if D2["d3"] == 2 else " ", "o" if D2["d4"] == 3 else "x" if D2["d4"] == 2 else " ", "o" if D2["d5"] == 3 else "x" if D2["d5"] == 2 else " ") + "\ne" + " " + "%s"*5 % ("o" if D1["e1"] == 3 else "x" if D1["e1"] == 2 else " ", "o" if D1["e2"] == 3 else "x" if D1["e2"] == 2 else " ", "o" if D1["e3"] == 3 else "x" if D1["e3"] == 2 else " ", "o" if D1["e4"] == 3 else "x" if D1["e4"] == 2 else " ", "o" if D1["e5"] == 3 else "x" if D1["e5"] == 2 else " ") + " "*3 + "e " + "%s"*5 % ("o" if D2["e1"] == 3 else "x" if D2["e1"] == 2 else " ", "o" if D2["e2"] == 3 else "x" if D2["e2"] == 2 else " ", "o" if D2["e3"] == 3 else "x" if D2["e3"] == 2 else " ", "o" if D2["e4"] == 3 else "x" if D2["e4"] == 2 else " ", "o" if D2["e5"] == 3 else "x" if D2["e5"] == 2 else " "))
            p = input("Player " + str(startingPlayer) + " enter your position to throw your missile: ")
        if startingPlayer == 1:
            if p in D1.keys() and p not in L1:
                print("Missile thrown at " + p)
            else:
                while p not in D1.keys():
                    p = input("Invalid position, or missile already thrown there. Try again: ")
            while (p not in D1.keys()):
                p = input("Invalid position, or missile already thrown there. Try again: ")
            if startingPlayer == 1:
                if p in L1:
                    while p in L1 or p not in D1.keys():
                        p = input("Invalid position, or missile already thrown there. Try again: ")
                        if p not in L1 and p in D1.keys():
                            print("Missile thrown at " + p)
                            break

            if startingPlayer == 1:
                if p in D2.keys():
                    if D2[p] == 1:
                        D2[p] = 3
                        print("Target hit!")
                        score1 += 1
                    else:
                        D2[p] = 2
                        print("Target missed!")
                else:
                    p = input("Invalid position, or missile already thrown there. Try again: ")
            L1.append(p)

        if startingPlayer == 2:
            print(" "*3 + "P1" + " "*8 + "P2\n" +" "*2 + "12345" + " "*5 + "12345\n" + "a" + " " + "%s"*5 % ("o" if D1["a1"] == 3 else "x" if D1["a1"] == 2 else " ", "o" if D1["a2"] == 3 else "x" if D1["a2"] == 2 else " ", "o" if D1["a3"] == 3 else "x" if D1["a3"] == 2 else " ", "o" if D1["a4"] == 3 else "x" if D1["a4"] == 2 else " ", "o" if D1["a5"] == 3 else "x" if D1["a5"] == 2 else " ") + " "*3 + "a " + "%s"*5 % ("o" if D2["a1"] == 3 else "x" if D2["a1"] == 2 else " ", "o" if D2["a2"] == 3 else "x" if D2["a2"] == 2 else " ", "o" if D2["a3"] == 3 else "x" if D2["a3"] == 2 else " ", "o" if D2["a4"] == 3 else "x" if D2["a4"] == 2 else " ", "o" if D2["a5"] == 3 else "x" if D2["a5"] == 2 else " ") + "\nb" + " " + "%s"*5 % ("o" if D1["b1"] == 3 else "x" if D1["b1"] == 2 else " ", "o" if D1["b2"] == 3 else "x" if D1["b2"] == 2 else " ", "o" if D1["b3"] == 3 else "x" if D1["b3"] == 2 else " ", "o" if D1["b4"] == 3 else "x" if D1["b4"] == 2 else " ", "o" if D1["b5"] == 3 else "x" if D1["b5"] == 2 else " ") + " "*3 + "b " + "%s"*5 % ("o" if D2["b1"] == 3 else "x" if D2["b1"] == 2 else " ", "o" if D2["b2"] == 3 else "x" if D2["b2"] == 2 else " ", "o" if D2["b3"] == 3 else "x" if D2["b3"] == 2 else " ", "o" if D2["b4"] == 3 else "x" if D2["b4"] == 2 else " ", "o" if D2["b5"] == 3 else "x" if D2["b5"] == 2 else " ") + "\nc" + " " + "%s"*5 % ("o" if D1["c1"] == 3 else "x" if D1["c1"] == 2 else " ", "o" if D1["c2"] == 3 else "x" if D1["c2"] == 2 else " ", "o" if D1["c3"] == 3 else "x" if D1["c3"] == 2 else " ", "o" if D1["c4"] == 3 else "x" if D1["c4"] == 2 else " ", "o" if D1["c5"] == 3 else "x" if D1["c5"] == 2 else " ") + " "*3 + "c " + "%s"*5 % ("o" if D2["c1"] == 3 else "x" if D2["c1"] == 2 else " ", "o" if D2["c2"] == 3 else "x" if D2["c2"] == 2 else " ", "o" if D2["c3"] == 3 else "x" if D2["c3"] == 2 else " ", "o" if D2["c4"] == 3 else "x" if D2["c4"] == 2 else " ", "o" if D2["c5"] == 3 else "x" if D2["c5"] == 2 else " ") + "\nd" + " " + "%s"*5 % ("o" if D1["d1"] == 3 else "x" if D1["d1"] == 2 else " ", "o" if D1["d2"] == 3 else "x" if D1["d2"] == 2 else " ", "o" if D1["d3"] == 3 else "x" if D1["d3"] == 2 else " ", "o" if D1["d4"] == 3 else "x" if D1["d4"] == 2 else " ", "o" if D1["d5"] == 3 else "x" if D1["d5"] == 2 else " ") + " "*3 + "d " + "%s"*5 % ("o" if D2["d1"] == 3 else "x" if D2["d1"] == 2 else " ", "o" if D2["d2"] == 3 else "x" if D2["d2"] == 2 else " ", "o" if D2["d3"] == 3 else "x" if D2["d3"] == 2 else " ", "o" if D2["d4"] == 3 else "x" if D2["d4"] == 2 else " ", "o" if D2["d5"] == 3 else "x" if D2["d5"] == 2 else " ") + "\ne" + " " + "%s"*5 % ("o" if D1["e1"] == 3 else "x" if D1["e1"] == 2 else " ", "o" if D1["e2"] == 3 else "x" if D1["e2"] == 2 else " ", "o" if D1["e3"] == 3 else "x" if D1["e3"] == 2 else " ", "o" if D1["e4"] == 3 else "x" if D1["e4"] == 2 else " ", "o" if D1["e5"] == 3 else "x" if D1["e5"] == 2 else " ") + " "*3 + "e " + "%s"*5 % ("o" if D2["e1"] == 3 else "x" if D2["e1"] == 2 else " ", "o" if D2["e2"] == 3 else "x" if D2["e2"] == 2 else " ", "o" if D2["e3"] == 3 else "x" if D2["e3"] == 2 else " ", "o" if D2["e4"] == 3 else "x" if D2["e4"] == 2 else " ", "o" if D2["e5"] == 3 else "x" if D2["e5"] == 2 else " "))
            p = randomShip
            if p not in L2:
                print("Missile thrown at " + p)
            while p in L2:
                randomChar = choice('abcde')
                randomNum = str(randint(1,5))
                randomShip = randomChar + randomNum
                p = randomShip
                if p not in L2:
                    print("Missile thrown at " + p)
            if startingPlayer == 2:
                if p in D1.keys():
                    if D1[p] == 1:
                        D1[p] = 3
                        print("Target hit!")
                        score2 += 1
                    else:
                        D1[p] = 2
                        print("Target missed!")
                else:
                    p = randomShip
            L2.append(p)
        if startingPlayer == 1:
            startingPlayer = 2
        else:
            startingPlayer = 1
        if score2 == 5:
            print(" "*3 + "P1" + " "*8 + "P2\n" +" "*2 + "12345" + " "*5 + "12345\n" + "a" + " " + "%s"*5 % ("o" if D1["a1"] == 3 else "x" if D1["a1"] == 2 else " ", "o" if D1["a2"] == 3 else "x" if D1["a2"] == 2 else " ", "o" if D1["a3"] == 3 else "x" if D1["a3"] == 2 else " ", "o" if D1["a4"] == 3 else "x" if D1["a4"] == 2 else " ", "o" if D1["a5"] == 3 else "x" if D1["a5"] == 2 else " ") + " "*3 + "a " + "%s"*5 % ("o" if D2["a1"] == 3 else "x" if D2["a1"] == 2 else " ", "o" if D2["a2"] == 3 else "x" if D2["a2"] == 2 else " ", "o" if D2["a3"] == 3 else "x" if D2["a3"] == 2 else " ", "o" if D2["a4"] == 3 else "x" if D2["a4"] == 2 else " ", "o" if D2["a5"] == 3 else "x" if D2["a5"] == 2 else " ") + "\nb" + " " + "%s"*5 % ("o" if D1["b1"] == 3 else "x" if D1["b1"] == 2 else " ", "o" if D1["b2"] == 3 else "x" if D1["b2"] == 2 else " ", "o" if D1["b3"] == 3 else "x" if D1["b3"] == 2 else " ", "o" if D1["b4"] == 3 else "x" if D1["b4"] == 2 else " ", "o" if D1["b5"] == 3 else "x" if D1["b5"] == 2 else " ") + " "*3 + "b " + "%s"*5 % ("o" if D2["b1"] == 3 else "x" if D2["b1"] == 2 else " ", "o" if D2["b2"] == 3 else "x" if D2["b2"] == 2 else " ", "o" if D2["b3"] == 3 else "x" if D2["b3"] == 2 else " ", "o" if D2["b4"] == 3 else "x" if D2["b4"] == 2 else " ", "o" if D2["b5"] == 3 else "x" if D2["b5"] == 2 else " ") + "\nc" + " " + "%s"*5 % ("o" if D1["c1"] == 3 else "x" if D1["c1"] == 2 else " ", "o" if D1["c2"] == 3 else "x" if D1["c2"] == 2 else " ", "o" if D1["c3"] == 3 else "x" if D1["c3"] == 2 else " ", "o" if D1["c4"] == 3 else "x" if D1["c4"] == 2 else " ", "o" if D1["c5"] == 3 else "x" if D1["c5"] == 2 else " ") + " "*3 + "c " + "%s"*5 % ("o" if D2["c1"] == 3 else "x" if D2["c1"] == 2 else " ", "o" if D2["c2"] == 3 else "x" if D2["c2"] == 2 else " ", "o" if D2["c3"] == 3 else "x" if D2["c3"] == 2 else " ", "o" if D2["c4"] == 3 else "x" if D2["c4"] == 2 else " ", "o" if D2["c5"] == 3 else "x" if D2["c5"] == 2 else " ") + "\nd" + " " + "%s"*5 % ("o" if D1["d1"] == 3 else "x" if D1["d1"] == 2 else " ", "o" if D1["d2"] == 3 else "x" if D1["d2"] == 2 else " ", "o" if D1["d3"] == 3 else "x" if D1["d3"] == 2 else " ", "o" if D1["d4"] == 3 else "x" if D1["d4"] == 2 else " ", "o" if D1["d5"] == 3 else "x" if D1["d5"] == 2 else " ") + " "*3 + "d " + "%s"*5 % ("o" if D2["d1"] == 3 else "x" if D2["d1"] == 2 else " ", "o" if D2["d2"] == 3 else "x" if D2["d2"] == 2 else " ", "o" if D2["d3"] == 3 else "x" if D2["d3"] == 2 else " ", "o" if D2["d4"] == 3 else "x" if D2["d4"] == 2 else " ", "o" if D2["d5"] == 3 else "x" if D2["d5"] == 2 else " ") + "\ne" + " " + "%s"*5 % ("o" if D1["e1"] == 3 else "x" if D1["e1"] == 2 else " ", "o" if D1["e2"] == 3 else "x" if D1["e2"] == 2 else " ", "o" if D1["e3"] == 3 else "x" if D1["e3"] == 2 else " ", "o" if D1["e4"] == 3 else "x" if D1["e4"] == 2 else " ", "o" if D1["e5"] == 3 else "x" if D1["e5"] == 2 else " ") + " "*3 + "e " + "%s"*5 % ("o" if D2["e1"] == 3 else "x" if D2["e1"] == 2 else " ", "o" if D2["e2"] == 3 else "x" if D2["e2"] == 2 else " ", "o" if D2["e3"] == 3 else "x" if D2["e3"] == 2 else " ", "o" if D2["e4"] == 3 else "x" if D2["e4"] == 2 else " ", "o" if D2["e5"] == 3 else "x" if D2["e5"] == 2 else " "))
            print("GAME OVER. CPU wins!")
        elif score1 == 5:
            print(" "*3 + "P1" + " "*8 + "P2\n" +" "*2 + "12345" + " "*5 + "12345\n" + "a" + " " + "%s"*5 % ("o" if D1["a1"] == 3 else "x" if D1["a1"] == 2 else " ", "o" if D1["a2"] == 3 else "x" if D1["a2"] == 2 else " ", "o" if D1["a3"] == 3 else "x" if D1["a3"] == 2 else " ", "o" if D1["a4"] == 3 else "x" if D1["a4"] == 2 else " ", "o" if D1["a5"] == 3 else "x" if D1["a5"] == 2 else " ") + " "*3 + "a " + "%s"*5 % ("o" if D2["a1"] == 3 else "x" if D2["a1"] == 2 else " ", "o" if D2["a2"] == 3 else "x" if D2["a2"] == 2 else " ", "o" if D2["a3"] == 3 else "x" if D2["a3"] == 2 else " ", "o" if D2["a4"] == 3 else "x" if D2["a4"] == 2 else " ", "o" if D2["a5"] == 3 else "x" if D2["a5"] == 2 else " ") + "\nb" + " " + "%s"*5 % ("o" if D1["b1"] == 3 else "x" if D1["b1"] == 2 else " ", "o" if D1["b2"] == 3 else "x" if D1["b2"] == 2 else " ", "o" if D1["b3"] == 3 else "x" if D1["b3"] == 2 else " ", "o" if D1["b4"] == 3 else "x" if D1["b4"] == 2 else " ", "o" if D1["b5"] == 3 else "x" if D1["b5"] == 2 else " ") + " "*3 + "b " + "%s"*5 % ("o" if D2["b1"] == 3 else "x" if D2["b1"] == 2 else " ", "o" if D2["b2"] == 3 else "x" if D2["b2"] == 2 else " ", "o" if D2["b3"] == 3 else "x" if D2["b3"] == 2 else " ", "o" if D2["b4"] == 3 else "x" if D2["b4"] == 2 else " ", "o" if D2["b5"] == 3 else "x" if D2["b5"] == 2 else " ") + "\nc" + " " + "%s"*5 % ("o" if D1["c1"] == 3 else "x" if D1["c1"] == 2 else " ", "o" if D1["c2"] == 3 else "x" if D1["c2"] == 2 else " ", "o" if D1["c3"] == 3 else "x" if D1["c3"] == 2 else " ", "o" if D1["c4"] == 3 else "x" if D1["c4"] == 2 else " ", "o" if D1["c5"] == 3 else "x" if D1["c5"] == 2 else " ") + " "*3 + "c " + "%s"*5 % ("o" if D2["c1"] == 3 else "x" if D2["c1"] == 2 else " ", "o" if D2["c2"] == 3 else "x" if D2["c2"] == 2 else " ", "o" if D2["c3"] == 3 else "x" if D2["c3"] == 2 else " ", "o" if D2["c4"] == 3 else "x" if D2["c4"] == 2 else " ", "o" if D2["c5"] == 3 else "x" if D2["c5"] == 2 else " ") + "\nd" + " " + "%s"*5 % ("o" if D1["d1"] == 3 else "x" if D1["d1"] == 2 else " ", "o" if D1["d2"] == 3 else "x" if D1["d2"] == 2 else " ", "o" if D1["d3"] == 3 else "x" if D1["d3"] == 2 else " ", "o" if D1["d4"] == 3 else "x" if D1["d4"] == 2 else " ", "o" if D1["d5"] == 3 else "x" if D1["d5"] == 2 else " ") + " "*3 + "d " + "%s"*5 % ("o" if D2["d1"] == 3 else "x" if D2["d1"] == 2 else " ", "o" if D2["d2"] == 3 else "x" if D2["d2"] == 2 else " ", "o" if D2["d3"] == 3 else "x" if D2["d3"] == 2 else " ", "o" if D2["d4"] == 3 else "x" if D2["d4"] == 2 else " ", "o" if D2["d5"] == 3 else "x" if D2["d5"] == 2 else " ") + "\ne" + " " + "%s"*5 % ("o" if D1["e1"] == 3 else "x" if D1["e1"] == 2 else " ", "o" if D1["e2"] == 3 else "x" if D1["e2"] == 2 else " ", "o" if D1["e3"] == 3 else "x" if D1["e3"] == 2 else " ", "o" if D1["e4"] == 3 else "x" if D1["e4"] == 2 else " ", "o" if D1["e5"] == 3 else "x" if D1["e5"] == 2 else " ") + " "*3 + "e " + "%s"*5 % ("o" if D2["e1"] == 3 else "x" if D2["e1"] == 2 else " ", "o" if D2["e2"] == 3 else "x" if D2["e2"] == 2 else " ", "o" if D2["e3"] == 3 else "x" if D2["e3"] == 2 else " ", "o" if D2["e4"] == 3 else "x" if D2["e4"] == 2 else " ", "o" if D2["e5"] == 3 else "x" if D2["e5"] == 2 else " "))
            print("GAME OVER. You win!")
			
###########MULTIPLAYER##########
if x == 2:
    for i in range(1,6):
        y = input("Player 1 enter the position of your ship no " + str(i) + ": ")
        if y in D1.keys() and D1[y] != 1:
            D1[y] =1
        else:
            while y not in D1.keys() or D1[y] == 1:
                y = input("Invalid position, or position already taken. Try again: ")
                if (y in D1.keys() and not D1[y] == 1):
                    D1[y] = 1
                    break
                elif y not in D1.keys() or D1[y] == 1:
                    pass

    print("\n"*500)
    for i in range(1,6):
        y = input("Player 2 enter the position of your ship no " + str(i) + ": ")
        if y in D2.keys() and D2[y] != 1:
            D2[y] =1
        else:
            while y not in D2.keys() or D2[y] == 1:
                y = input("Invalid position, or position already taken. Try again: ")
                if (y in D2.keys() and not D2[y] == 1):
                    D2[y] = 1
                    break
                elif y not in D2.keys() or D2[y] == 1:
                    pass
    print("\n"*500)
    startingPlayer = randint(1,2)
    print("Player %s starts first" % ("1" if startingPlayer == 2 else "2"))
    L1,L2,score1,score2 = [],[],0,0
    while not (score1 == 5 or score2 == 5):
        if startingPlayer == 1:
            startingPlayer = 2
        else:
            startingPlayer = 1
        print(" "*3 + "P1" + " "*8 + "P2\n" +" "*2 + "12345" + " "*5 + "12345\n" + "a" + " " + "%s"*5 % ("o" if D1["a1"] == 3 else "x" if D1["a1"] == 2 else " ", "o" if D1["a2"] == 3 else "x" if D1["a2"] == 2 else " ", "o" if D1["a3"] == 3 else "x" if D1["a3"] == 2 else " ", "o" if D1["a4"] == 3 else "x" if D1["a4"] == 2 else " ", "o" if D1["a5"] == 3 else "x" if D1["a5"] == 2 else " ") + " "*3 + "a " + "%s"*5 % ("o" if D2["a1"] == 3 else "x" if D2["a1"] == 2 else " ", "o" if D2["a2"] == 3 else "x" if D2["a2"] == 2 else " ", "o" if D2["a3"] == 3 else "x" if D2["a3"] == 2 else " ", "o" if D2["a4"] == 3 else "x" if D2["a4"] == 2 else " ", "o" if D2["a5"] == 3 else "x" if D2["a5"] == 2 else " ") + "\nb" + " " + "%s"*5 % ("o" if D1["b1"] == 3 else "x" if D1["b1"] == 2 else " ", "o" if D1["b2"] == 3 else "x" if D1["b2"] == 2 else " ", "o" if D1["b3"] == 3 else "x" if D1["b3"] == 2 else " ", "o" if D1["b4"] == 3 else "x" if D1["b4"] == 2 else " ", "o" if D1["b5"] == 3 else "x" if D1["b5"] == 2 else " ") + " "*3 + "b " + "%s"*5 % ("o" if D2["b1"] == 3 else "x" if D2["b1"] == 2 else " ", "o" if D2["b2"] == 3 else "x" if D2["b2"] == 2 else " ", "o" if D2["b3"] == 3 else "x" if D2["b3"] == 2 else " ", "o" if D2["b4"] == 3 else "x" if D2["b4"] == 2 else " ", "o" if D2["b5"] == 3 else "x" if D2["b5"] == 2 else " ") + "\nc" + " " + "%s"*5 % ("o" if D1["c1"] == 3 else "x" if D1["c1"] == 2 else " ", "o" if D1["c2"] == 3 else "x" if D1["c2"] == 2 else " ", "o" if D1["c3"] == 3 else "x" if D1["c3"] == 2 else " ", "o" if D1["c4"] == 3 else "x" if D1["c4"] == 2 else " ", "o" if D1["c5"] == 3 else "x" if D1["c5"] == 2 else " ") + " "*3 + "c " + "%s"*5 % ("o" if D2["c1"] == 3 else "x" if D2["c1"] == 2 else " ", "o" if D2["c2"] == 3 else "x" if D2["c2"] == 2 else " ", "o" if D2["c3"] == 3 else "x" if D2["c3"] == 2 else " ", "o" if D2["c4"] == 3 else "x" if D2["c4"] == 2 else " ", "o" if D2["c5"] == 3 else "x" if D2["c5"] == 2 else " ") + "\nd" + " " + "%s"*5 % ("o" if D1["d1"] == 3 else "x" if D1["d1"] == 2 else " ", "o" if D1["d2"] == 3 else "x" if D1["d2"] == 2 else " ", "o" if D1["d3"] == 3 else "x" if D1["d3"] == 2 else " ", "o" if D1["d4"] == 3 else "x" if D1["d4"] == 2 else " ", "o" if D1["d5"] == 3 else "x" if D1["d5"] == 2 else " ") + " "*3 + "d " + "%s"*5 % ("o" if D2["d1"] == 3 else "x" if D2["d1"] == 2 else " ", "o" if D2["d2"] == 3 else "x" if D2["d2"] == 2 else " ", "o" if D2["d3"] == 3 else "x" if D2["d3"] == 2 else " ", "o" if D2["d4"] == 3 else "x" if D2["d4"] == 2 else " ", "o" if D2["d5"] == 3 else "x" if D2["d5"] == 2 else " ") + "\ne" + " " + "%s"*5 % ("o" if D1["e1"] == 3 else "x" if D1["e1"] == 2 else " ", "o" if D1["e2"] == 3 else "x" if D1["e2"] == 2 else " ", "o" if D1["e3"] == 3 else "x" if D1["e3"] == 2 else " ", "o" if D1["e4"] == 3 else "x" if D1["e4"] == 2 else " ", "o" if D1["e5"] == 3 else "x" if D1["e5"] == 2 else " ") + " "*3 + "e " + "%s"*5 % ("o" if D2["e1"] == 3 else "x" if D2["e1"] == 2 else " ", "o" if D2["e2"] == 3 else "x" if D2["e2"] == 2 else " ", "o" if D2["e3"] == 3 else "x" if D2["e3"] == 2 else " ", "o" if D2["e4"] == 3 else "x" if D2["e4"] == 2 else " ", "o" if D2["e5"] == 3 else "x" if D2["e5"] == 2 else " "))
        p = input("Player " + str(startingPlayer) + " enter your position to throw your missile: ")
        if p in D1.keys() and p not in L2:
            pass
        else:
            while p not in D1.keys():
                p = input("Invalid position, or missile already thrown there. Try again: ")
        while (p not in D1.keys()):
            p = input("Invalid position, or missile already thrown there. Try again: ")
        if startingPlayer == 1:
            while p in L2:
                p = input("Invalid position, or missile already thrown there. Try again: ")

        if startingPlayer == 1:
            if p in D2.keys():
                print("Missile thrown at " + p)
                if D2[p] == 1 and p not in L2:
                    D2[p] = 3
                    print("Target hit!")
                    L2.append(p)
                    score1 += 1
                elif D2[p] == 0:
                    D2[p] = 2
                    print("Target missed")
                    L2.append(p)
            else:
                p = input("Invalid position, or missile already thrown there. Try again: ")
        elif startingPlayer == 2:
            if p in D1.keys() and p not in L1:
                print("Missile thrown at " + p)
                if D1[p] == 1 and p not in L1:
                    D1[p] = 3
                    print("Target hit!")
                    L1.append(p)
                    score2 += 1
                elif D1[p] == 0:
                    D1[p] = 2
                    print("Target missed")
                    L1.append(p)
            else:
                while p in L1:
                    p = input("Invalid position, or missile already thrown there. Try again: ")
                    if p in D1.keys() and D1[p] == 1:
                        D1[p] = 3
                        print("Target hit!")
                        L1.append(p)
                        score2 += 1
                        break
                    elif p in D1.keys() and D1[p] == 0:
                        D1[p] = 2
                        print("Target missed")
                        L1.append(p)
                        break
        if score2 == 5:
            print(" "*3 + "P1" + " "*8 + "P2\n" +" "*2 + "12345" + " "*5 + "12345\n" + "a" + " " + "%s"*5 % ("o" if D1["a1"] == 3 else "x" if D1["a1"] == 2 else " ", "o" if D1["a2"] == 3 else "x" if D1["a2"] == 2 else " ", "o" if D1["a3"] == 3 else "x" if D1["a3"] == 2 else " ", "o" if D1["a4"] == 3 else "x" if D1["a4"] == 2 else " ", "o" if D1["a5"] == 3 else "x" if D1["a5"] == 2 else " ") + " "*3 + "a " + "%s"*5 % ("o" if D2["a1"] == 3 else "x" if D2["a1"] == 2 else " ", "o" if D2["a2"] == 3 else "x" if D2["a2"] == 2 else " ", "o" if D2["a3"] == 3 else "x" if D2["a3"] == 2 else " ", "o" if D2["a4"] == 3 else "x" if D2["a4"] == 2 else " ", "o" if D2["a5"] == 3 else "x" if D2["a5"] == 2 else " ") + "\nb" + " " + "%s"*5 % ("o" if D1["b1"] == 3 else "x" if D1["b1"] == 2 else " ", "o" if D1["b2"] == 3 else "x" if D1["b2"] == 2 else " ", "o" if D1["b3"] == 3 else "x" if D1["b3"] == 2 else " ", "o" if D1["b4"] == 3 else "x" if D1["b4"] == 2 else " ", "o" if D1["b5"] == 3 else "x" if D1["b5"] == 2 else " ") + " "*3 + "b " + "%s"*5 % ("o" if D2["b1"] == 3 else "x" if D2["b1"] == 2 else " ", "o" if D2["b2"] == 3 else "x" if D2["b2"] == 2 else " ", "o" if D2["b3"] == 3 else "x" if D2["b3"] == 2 else " ", "o" if D2["b4"] == 3 else "x" if D2["b4"] == 2 else " ", "o" if D2["b5"] == 3 else "x" if D2["b5"] == 2 else " ") + "\nc" + " " + "%s"*5 % ("o" if D1["c1"] == 3 else "x" if D1["c1"] == 2 else " ", "o" if D1["c2"] == 3 else "x" if D1["c2"] == 2 else " ", "o" if D1["c3"] == 3 else "x" if D1["c3"] == 2 else " ", "o" if D1["c4"] == 3 else "x" if D1["c4"] == 2 else " ", "o" if D1["c5"] == 3 else "x" if D1["c5"] == 2 else " ") + " "*3 + "c " + "%s"*5 % ("o" if D2["c1"] == 3 else "x" if D2["c1"] == 2 else " ", "o" if D2["c2"] == 3 else "x" if D2["c2"] == 2 else " ", "o" if D2["c3"] == 3 else "x" if D2["c3"] == 2 else " ", "o" if D2["c4"] == 3 else "x" if D2["c4"] == 2 else " ", "o" if D2["c5"] == 3 else "x" if D2["c5"] == 2 else " ") + "\nd" + " " + "%s"*5 % ("o" if D1["d1"] == 3 else "x" if D1["d1"] == 2 else " ", "o" if D1["d2"] == 3 else "x" if D1["d2"] == 2 else " ", "o" if D1["d3"] == 3 else "x" if D1["d3"] == 2 else " ", "o" if D1["d4"] == 3 else "x" if D1["d4"] == 2 else " ", "o" if D1["d5"] == 3 else "x" if D1["d5"] == 2 else " ") + " "*3 + "d " + "%s"*5 % ("o" if D2["d1"] == 3 else "x" if D2["d1"] == 2 else " ", "o" if D2["d2"] == 3 else "x" if D2["d2"] == 2 else " ", "o" if D2["d3"] == 3 else "x" if D2["d3"] == 2 else " ", "o" if D2["d4"] == 3 else "x" if D2["d4"] == 2 else " ", "o" if D2["d5"] == 3 else "x" if D2["d5"] == 2 else " ") + "\ne" + " " + "%s"*5 % ("o" if D1["e1"] == 3 else "x" if D1["e1"] == 2 else " ", "o" if D1["e2"] == 3 else "x" if D1["e2"] == 2 else " ", "o" if D1["e3"] == 3 else "x" if D1["e3"] == 2 else " ", "o" if D1["e4"] == 3 else "x" if D1["e4"] == 2 else " ", "o" if D1["e5"] == 3 else "x" if D1["e5"] == 2 else " ") + " "*3 + "e " + "%s"*5 % ("o" if D2["e1"] == 3 else "x" if D2["e1"] == 2 else " ", "o" if D2["e2"] == 3 else "x" if D2["e2"] == 2 else " ", "o" if D2["e3"] == 3 else "x" if D2["e3"] == 2 else " ", "o" if D2["e4"] == 3 else "x" if D2["e4"] == 2 else " ", "o" if D2["e5"] == 3 else "x" if D2["e5"] == 2 else " "))
            print("GAME OVER. Player 2 Wins!")
        elif score1 == 5:
            print(" "*3 + "P1" + " "*8 + "P2\n" +" "*2 + "12345" + " "*5 + "12345\n" + "a" + " " + "%s"*5 % ("o" if D1["a1"] == 3 else "x" if D1["a1"] == 2 else " ", "o" if D1["a2"] == 3 else "x" if D1["a2"] == 2 else " ", "o" if D1["a3"] == 3 else "x" if D1["a3"] == 2 else " ", "o" if D1["a4"] == 3 else "x" if D1["a4"] == 2 else " ", "o" if D1["a5"] == 3 else "x" if D1["a5"] == 2 else " ") + " "*3 + "a " + "%s"*5 % ("o" if D2["a1"] == 3 else "x" if D2["a1"] == 2 else " ", "o" if D2["a2"] == 3 else "x" if D2["a2"] == 2 else " ", "o" if D2["a3"] == 3 else "x" if D2["a3"] == 2 else " ", "o" if D2["a4"] == 3 else "x" if D2["a4"] == 2 else " ", "o" if D2["a5"] == 3 else "x" if D2["a5"] == 2 else " ") + "\nb" + " " + "%s"*5 % ("o" if D1["b1"] == 3 else "x" if D1["b1"] == 2 else " ", "o" if D1["b2"] == 3 else "x" if D1["b2"] == 2 else " ", "o" if D1["b3"] == 3 else "x" if D1["b3"] == 2 else " ", "o" if D1["b4"] == 3 else "x" if D1["b4"] == 2 else " ", "o" if D1["b5"] == 3 else "x" if D1["b5"] == 2 else " ") + " "*3 + "b " + "%s"*5 % ("o" if D2["b1"] == 3 else "x" if D2["b1"] == 2 else " ", "o" if D2["b2"] == 3 else "x" if D2["b2"] == 2 else " ", "o" if D2["b3"] == 3 else "x" if D2["b3"] == 2 else " ", "o" if D2["b4"] == 3 else "x" if D2["b4"] == 2 else " ", "o" if D2["b5"] == 3 else "x" if D2["b5"] == 2 else " ") + "\nc" + " " + "%s"*5 % ("o" if D1["c1"] == 3 else "x" if D1["c1"] == 2 else " ", "o" if D1["c2"] == 3 else "x" if D1["c2"] == 2 else " ", "o" if D1["c3"] == 3 else "x" if D1["c3"] == 2 else " ", "o" if D1["c4"] == 3 else "x" if D1["c4"] == 2 else " ", "o" if D1["c5"] == 3 else "x" if D1["c5"] == 2 else " ") + " "*3 + "c " + "%s"*5 % ("o" if D2["c1"] == 3 else "x" if D2["c1"] == 2 else " ", "o" if D2["c2"] == 3 else "x" if D2["c2"] == 2 else " ", "o" if D2["c3"] == 3 else "x" if D2["c3"] == 2 else " ", "o" if D2["c4"] == 3 else "x" if D2["c4"] == 2 else " ", "o" if D2["c5"] == 3 else "x" if D2["c5"] == 2 else " ") + "\nd" + " " + "%s"*5 % ("o" if D1["d1"] == 3 else "x" if D1["d1"] == 2 else " ", "o" if D1["d2"] == 3 else "x" if D1["d2"] == 2 else " ", "o" if D1["d3"] == 3 else "x" if D1["d3"] == 2 else " ", "o" if D1["d4"] == 3 else "x" if D1["d4"] == 2 else " ", "o" if D1["d5"] == 3 else "x" if D1["d5"] == 2 else " ") + " "*3 + "d " + "%s"*5 % ("o" if D2["d1"] == 3 else "x" if D2["d1"] == 2 else " ", "o" if D2["d2"] == 3 else "x" if D2["d2"] == 2 else " ", "o" if D2["d3"] == 3 else "x" if D2["d3"] == 2 else " ", "o" if D2["d4"] == 3 else "x" if D2["d4"] == 2 else " ", "o" if D2["d5"] == 3 else "x" if D2["d5"] == 2 else " ") + "\ne" + " " + "%s"*5 % ("o" if D1["e1"] == 3 else "x" if D1["e1"] == 2 else " ", "o" if D1["e2"] == 3 else "x" if D1["e2"] == 2 else " ", "o" if D1["e3"] == 3 else "x" if D1["e3"] == 2 else " ", "o" if D1["e4"] == 3 else "x" if D1["e4"] == 2 else " ", "o" if D1["e5"] == 3 else "x" if D1["e5"] == 2 else " ") + " "*3 + "e " + "%s"*5 % ("o" if D2["e1"] == 3 else "x" if D2["e1"] == 2 else " ", "o" if D2["e2"] == 3 else "x" if D2["e2"] == 2 else " ", "o" if D2["e3"] == 3 else "x" if D2["e3"] == 2 else " ", "o" if D2["e4"] == 3 else "x" if D2["e4"] == 2 else " ", "o" if D2["e5"] == 3 else "x" if D2["e5"] == 2 else " "))
            print("GAME OVER. Player 1 Wins!")
