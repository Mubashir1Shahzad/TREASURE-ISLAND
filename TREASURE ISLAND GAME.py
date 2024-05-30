print(r'''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
#for adding ascII arts in python it is better to write it in print(r"""    """)
#because the other format is for writing simple strings and r is added to print the ASCII art in
#a better way only """ can sometimes give a different art as compared to the needed one
#r is a raw string and reads\ as a character rather than escape character
direction = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")
direction_lower = direction.lower()
if direction_lower == "left":
          print("You have come to a lake .There is an island in the middle of the lake.")
          lake = input('Type "wait" to wait for the boat.Type "swim" to swim across\n')
          lake_lower = lake.lower() 

          if lake_lower == "wait":
                    print("You have arrived to the island unharmed. There is a house with 3 doors.") 
                    door = input("One red, One yellow and one blue. Which colour do you choose?\n")
                    door_lower = door.lower()
                    if door_lower == "yellow":
                              print("You win")
                    elif door_lower == "red":
                              print("Burned by fire. Game over")
                    elif door_lower == "blue":
                              print("Eaten by beasts. Game over")
                    else:
                              print("Game over")


          else: 
                    print("You got attacked by angry trout.Game over!")

else:
          print("Fall into a hole. Game over")

