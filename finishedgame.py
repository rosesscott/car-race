# create an introduction and ask what car number the user would like to choose.

print("Welcome to my car game! :)")
print("_______________________")

difficult_car = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']


def carcheck(question, min, max):
    # carcheck is the name of my function in python
    # easy and hard boundaries will be set up by the programmer
    valid = False
    while not valid:
        try:  # convert input to interger
            initial_car = int(input(question))
            if min <= initial_car <= max:
                print('You chose car', initial_car)

                break
            else:  # the number is invalid
                print("Please enter a valid car number \nBetween 1 and 12")
                continue
        except ValueError:
            print("Please enter a valid number\nThis must be a number, please try again")


# run function - call
carcheck("Choose a car number... (1-12)? ", 1, 12)

print("_______________________")


# level = input('which level would you like to play, easy or hard?')
# print('you have chosen: {}'. format(level))
def level(question):
    # def = define
    # level is the name of my function in python

    valid = False
    while not valid:
        try:  # convert input to integer
            race_difficulty = (input(question))
            if race_difficulty == "easy":
                print('You chose level', race_difficulty)
                # loop is successful
                break
            if race_difficulty == "hard":
                print('You chose level', race_difficulty)
                # loop is successful
                break
            else:  # the number is invalid
                print("Please enter a valid level \nChoose 'easy' or 'hard'")
                continue
        except ValueError:
            print("Please enter a valid answer\n This must be easy or hard, please try again")


# run function
level("Choose a race difficulty... 'easy' or 'hard'? ")

print("_______________________")


def distancecheck(question, min, max):
    # def = define
    # distancecheck is the name of my function in python

    valid = False
    while not valid:
        try:  # convert input to integer
            race_distance = int(input(question))
            if min <= race_distance <= max:
                print('You chose race distance', race_distance)
                # I am happy with the loop
                break
            else:  # the number is invalid
                print("Please enter a valid race distance\nBetween 5 and 15")
                continue
        except ValueError:
            print("Please enter a valid race distance\nThis must be a number, please try again")


# run function - call
distancecheck("Choose a race distance... (5-15) ", 5, 15)

# ask if they would now like to begin
print("_______________________")


def start_question(question):
    # def = define
    # start_question is the name of my function in python

    valid = False
    while not valid:
        yes_no = (input(question))
        if yes_no == "yes":
            print('Ok, lets get racing!')
            # I am happy with the loop
            break
        else:  # the number is invalid
            print("Please enter 'yes' when you would like to begin!")
            continue


start_question("Would you like to begin?")

print("_______________________")

import random

cars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# show distances travelled
# inital distance_travelled = [0,0,0,0,0,0]

distance_traveled = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# distance_travelled[add_car] +=1
# print(distance_travelled)

# 1st place
# add_car=""
valid = False
while not valid:
    # choose a number from cars list, 1-12
    place_1st = random.choice(cars)
    # print(add_car)
    distance_traveled[place_1st - 1] += 1

    if distance_traveled[place_1st - 1] == 15:

        break
    else:
        continue

print(cars)
print(distance_traveled)


# check who has won

def print_snapshot(mylist):
    counter = 1
    for car_distance in mylist:
        print('car {} has moved \n'.format(counter) + "*" * car_distance)
        counter += 1
    # pass


print_snapshot(distance_traveled)

# 2nd place
# place_2nd=""
valid = False
while not valid:
    # choose a number from cars list, 1-12
    place_2nd = random.choice(cars)
    # print(add_car)
    distance_traveled[place_2nd - 1] += 1

    if distance_traveled[place_2nd - 1] == 15:

        if place_2nd == place_1st:
            continue
        break
    else:
        continue
# 3rd place
# place_3rd=""
valid = False
while not valid:
    # choose a number from cars list, 1-12
    place_3rd = random.choice(cars)
    # print(add_car)
    distance_traveled[place_3rd - 1] += 1

    if distance_traveled[place_3rd - 1] == 15:

        # print(add_car)
        if place_3rd == place_1st:
            continue
        if place_3rd == place_2nd:
            continue
        break
    else:
        continue

# 1st, 2nd, 3rd place winners, input
print("The car in 1st place is {}, Congratulations!".format(place_1st))
print("The car in 2nd place is {}, Congratulations!".format(place_2nd))
print("The car in 3rd place is {}, Congratulations!".format(place_3rd))
