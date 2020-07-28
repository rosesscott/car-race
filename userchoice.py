#create an introduction and ask what car number the user would like to choose.

print("Welcome to my car game! :) simp")
print("_______________________")

difficult_car = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

level = input('which level would you like to play, easy or difficult?')
print('you have chosen: {}'. format(level))

def carcheck (question, min, max):
    #def = define
    # intcheck is the name of my fucntion in python
    # question - will be the question asked to the user
    # low and high boundaries will be set up by the progarmmer
    valid = False
    while not valid:
        try: #try to convet input to interger
            initial_car = int(input(question))
            if min<= initial_car<=max:
                print('You chose car', initial_car)
                # I am happy with the loop
                break
            else: #the number is out of bounds
                print("Please enter a valid car number\nsimp! \nBetween 1 and 12")
                continue
        except ValueError:
            print("Please enter a valid number\nPeasant! This must be a number, please try again")
#run function - call
carcheck("Choose a car number... (1-12)? ", 1 , 12)


def distancecheck (question, min, max):
    #def = define
    # intcheck is the name of my fucntion in python
    # question - will be the question asked to the user
    # low and high boundaries will be set up by the progarmmer
    valid = False
    while not valid:
        try: #try to convet input to interger
            race_distance = int(input(question))
            if min<= race_distance<=max:
                print('You chose race distance', race_distance)
                # I am happy with the loop
                break
            else: #the number is out of bounds
                print("Please enter a valid race distance\nsimp! \nBetween 5 and 15")
                continue
        except ValueError:
            print("Please enter a valid race distance\n This must be a number, please try again")
#run function - call
distancecheck("Choose a race distance... (5-15)? ", 5 , 15)














