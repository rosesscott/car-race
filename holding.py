amount_initial = int(input ("Choose a car number... (1-12)? "))

if 1<= amount_initial <=12:
    print("great!")
else:
    print('You need a number between 1 and 12. Try again!')


#continue and ask how many rounds they would like to play
race_distance = int(input ("Choose a race distance... ()? "))
if 1<= amount_initial <=12:
    print("great!")
else:
    print('You need a number between 1 and 12. Try again!')
#print("What distance would you like to race? (10-100)")


#carlist ['car1', 'car2', 'car3', 'car4' 'car5' 'car6' 'car7' 'car8' 'car9' 'car10' 'car11' 'car12']
#for car in carlist:
    #print(car)


#ask da players to choose a distance
#keep track of distances
#initially distance_travelled = [0,0,0,0,0,0]
distances_travelled = [1,2,4,0,0,6]
distances_travelled = [4,2,5,4,2,10]


def print_snapshot(mylist):
    counter=1
    for car_distance in mylist:
        print ('car {} has moved \n'. format (counter) +'*'*car_distance)
        counter+=1

        if car_distance == 10:
            print(mylist[mylist.index(cardistance)])
        #pass


# call
#print_snapshot(distance_travelled)

