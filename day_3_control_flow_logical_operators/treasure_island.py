print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[JsChaux]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choise1 = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\" ").lower()
if choise1 != "left":
    print('Fall into a hole.\nGame Over.')
    quit()
choise2 = input('''You come to a lake. There is an island in the middle of the lake.
Type \"wait\" to wait for a boat or \"swim\" to swim across. ''').lower()
if choise2 != "wait":
    print('Attacked by trout.\nGame Over.')
    quit()
choise3 = input('''You arrive at the island unharmed. There is a house with 3 doors.
One red, one yellow and one blue. Whitch colour do  you choose? ''').lower()
if choise3 == "red":
    print("Burned by fire.\nGame Over.")
elif choise3 == "blue":
    print("Eaten by beasts.\nGame Over.")
elif choise3 == "yellow":
    print("You Win!")
else:
    print("Game Over.")