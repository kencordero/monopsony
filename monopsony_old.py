# Monopsony - Python implementation
from random import randint

#noOfPlayers = int(raw_input('How many players? (2-8) '))
NUMBER_OF_PLAYERS = 10

class GameBoard(object):
    pass


def setup_players():
  players = []
  for i in range(noOfPlayers):
    players.append(Player())
    players[i].number = i
    players[i].piece = pieces[i]
    players[i].money = 1500
    players[i].position = 0
    print("Player " + str(i+1) + " will use the " + players[i].piece.lower() + ".")


if __name__ == '__main__':
    print
    round = 0
    consecutive_doubles = 0
    while True:
      round += 1
      print("ROUND " + str(round))
      for current in players:
        if (consecutive_doubles > 0):
          current = players[current.number-1]
          print("Player " + str(current.number+1) + " rolls again.")
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        if (die1 == die2):
          consecutive_doubles += 1
        else:
            consecutive_doubles = 0
        print("Player " +str(current.number+1) + " has rolled " + str(die1) + " and " + str(die2))
        current.position = (current.position + die1 + die2)
        print(current.piece + " lands on " + spaces[current.position%40])
        if (current.position >= 40):
          print("Player " + str(current.number+1) + " collects $200.")
          current.money += 200
          current.position -= 40
          showMoney()
        if (spaces[current.position] == "Chance"):
          print(C[0])
          if (Chance[C[0]] == 0):
            current.position = 0
            current.money += 200
            showMoney()
          elif( Chance[C[0]] == 6):
            current.money += 50
            showMoney()
          elif (Chance[C[0]] == 8):
            current.position -= 3
          elif (Chance[C[0]] == 11):
            if (current.money < 15):
              print("Insufficient funds!")
            else:
              current.money -= 15
          elif (Chance[C[0]] == 13):
            current.position == 39
          elif (Chance[C[0]] == 15):
            current.money += 150
            showMoney()
          C.append(C[0])
          del C[0]
        if (spaces[current.position] == "Community Chest"):
          print(CC[0])
          if (CommChest[CC[0]] == 0):
            current.position = 0
            current.money += 200
            showMoney()
          elif (CommChest[CC[0]] == 1):
            current.money += 200
            showMoney()
          elif (CommChest[CC[0]] == 2):
            current.money -= 50
            showMoney()
          elif (CommChest[CC[0]] == 3):
            current.money += 45
            showMoney()
          elif (CommChest[CC[0]] == 7):
            current.money += 20
            showMoney()
          elif (CommChest[CC[0]] == 8 or CommChest[CC[0]] == 12 or CommChest[CC[0]] == 15):
            current.money += 100
            showMoney()
          elif (CommChest[CC[0]] == 9):
            current.money -= 100
            showMoney()
          elif (CommChest[CC[0]] == 10):
            current.money -= 150
            showMoney()
          elif (CommChest[CC[0]] == 11):
            current.money += 25
            showMoney()
          elif (CommChest[CC[0]] == 14):
            current.money += 10
            showMoney()
          CC.append(CC[0])
          del CC[0]
        if (props[current.position].owned == 0):
          if (current.money < props[current.position].price):
              print("Player " + str(current.number+1) + " has insufficient funds to buy " + spaces[current.position])
          else:
            props[current.position].owned = current.number + 1
            print("Player " + str(current.number+1) + " buys " + spaces[current.position])
            current.money -= props[current.position].price
            showMoney()
        elif (props[current.position].owned > 0):
          if (props[current.position].owned == current.number+1):
            print("Player " + str(current.number+1) + " already owns " + spaces[current.position])
          else:
            owner = props[current.position].owned - 1
            print("Player " + str(owner + 1) + " owns this property.")
            if (props[current.position].color == "utility"):
              pass #TODO
            elif (props[current.position].color == "rail"):
              pass #TODO
            else:
              print("Player " + str(current.number+1) + " owes $" + str(props[current.position].rent) + " rent.")
              if (current.money < props[current.position].rent):
                "Insufficient funds to pay rent!"
              else:
                current.money -= props[current.position].rent
                print("Player " + str(current.number+1) + " now has $" + str(current.money))
                players[owner].money += props[current.position].rent
                print("Player " + str(owner + 1) + " now has $" +  str(players[owner].money))
        elif (current.position == 38):
          current.money -= 100
          print("Player " + str(current.number+1) + " now has $" + str(current.money))
        elif (current.position == 4):
          current.money -= 200
          print("Player " + str(current.number+1) + " now has $" + str(current.money))
        raw_input()
        if (consecutive_doubles > 0):
          print()

def showMoney():
    print("Player " + str(current.number+1) + " now has $" + str(current.money) + ".")
