#create an introduction and ask what car number the user would like to choose.

print("Welcome to my car game! :)")
print("_______________________")

difficult_car = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']


def carcheck (question, min, max):
    # carcheck is the name of my function in python
    # easy and hard boundaries will be set up by the programmer
    valid = False
    while not valid:
        try: #convert input to interger
            initial_car = int(input(question))
            if min<= initial_car<=max:
                print('You chose car', initial_car)

                break
            else: #the number is invalid
                print("Please enter a valid car number \nBetween 1 and 12")
                continue
        except ValueError:
            print("Please enter a valid number\n This must be a number, please try again")
#run function - call
carcheck("Choose a car number... (1-12)? ", 1 , 12)


print("_______________________")

#level = input('which level would you like to play, easy or hard?')
#print('you have chosen: {}'. format(level))
def level (question):
    #def = define
    # level is the name of my function in python
    # question - will be the question asked to the user
    valid = False
    while not valid:
        try: #convert input to interger
            race_difficulty = (input(question))
            if race_difficulty == "easy":
                print('You chose level', race_difficulty)
                # loop is successful
                break
            if race_difficulty == "hard":
                print('You chose level', race_difficulty)
                # loop is successful
                break
            else: #the number is invalid
                print("Please enter a valid level \nChoose easy or hard")
                continue
        except ValueError:
            print("Please enter a valid answer\n This must be easy or hard, please try again")
#run function - call
level("Choose a race difficulty... 'easy' or 'hard'? ")



print("_______________________")

def distancecheck (question, min, max):
    #def = define
    # distancecheck is the name of my fucntion in python
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
            else: #the number is invalid
                print("Please enter a valid race distance\n Between 5 and 15")
                continue
        except ValueError:
            print("Please enter a valid race distance\n This must be a number, please try again")
#run function - call
distancecheck("Choose a race distance... (5-15)? ", 5 , 15)


#ask if they would now like to begin
print("_______________________")


def start_question (question):
    #def = define
    # start_question is the name of my function in python
    # question - will be the question asked to the user
    valid = False
    while not valid:
        yes_no = (input(question))
        if yes_no == "yes":
                print('Ok, lets start!')
                # I am happy with the loop
                break
        else: #the number is invalid
                print("Please enter 'yes' when you would like to start!")
                continue

start_question("Would you like to start?")

print("_______________________")
