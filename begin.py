def start_question (question):
    #def = define
    # levelcheck is the name of my fucntion in python
    # question - will be the question asked to the user
    # low and high boundaries will be set up by the progarmmer
    valid = False
    while not valid:
        yes_no = (input(question))
        if yes_no == "yes":
                print('Ok, lets get racing!')
                # I am happy with the loop
                break
        else: #the number is out of bounds
                print("Please enter 'yes' when you would like to begin!")
                continue

start_question("Would you like to begin?")
