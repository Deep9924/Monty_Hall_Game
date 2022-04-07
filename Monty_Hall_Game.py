import random

# variables
door_list = [1,2,3]
# randomizing each time to get different door
prize_door = random.randint(1,3)

# Taking input from user
while True:
    user_input = int(input("Pick a door number (1-3): "))
    if user_input in range(1,4):
        break
door_list.remove(user_input)

# if user did not picked the prize door then remove it so host will not pick the prize door
# if user picked the prize door then keep the list as we there will be two door for host to pick from
if (user_input != prize_door):
    door_list.remove(prize_door)

# Host is revealing another door
host = random.choice(door_list)
print("Let me help you.")
print("There is a goat behind door {} \n".format(host))
door_list.remove(host)

# Asking user if they want to switch their guess
choice = input("Would you still like to keep your choice? (y/n): ").lower()
if (choice == "y"):
    if (user_input == prize_door):
        print("You have won the car.\n")
    else:
        print("You have not won the car.\n")
elif (choice == "n"):
    if (user_input != prize_door):
        print("You have won the car.\n")
    else:
        print("You have not won the car.\n")