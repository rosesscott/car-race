import random
cars = [1,2,3,4,5,6,7,8,9,10,11,12]

#show distances travelled for all cars
#inital distance_travelled = [0,0,0,0,0,0]

distance_travelled = [0,0,0,0,0,0,0,0,0,0,0,0]

#distance_travelled[add_car] +=1
#print(distance_travelled)

#1st place
#add_car=""
valid = False
while not valid:
    #choose a number from cars list, 1-12
    place_1st = random.choice(cars)
    #print(add_car)
    distance_travelled[place_1st-1] += 1

    if distance_travelled[place_1st-1] == 15:

        break
    else:
        continue

print(cars)
print(distance_travelled)
#check 1st, 2nd, 3rd

def print_snapshot(mylist):
    counter=1
    for car_distance in mylist:
        print('car {} has moved \n'.format(counter)+"*"*car_distance)
        counter+= 1
    #pass

print_snapshot(distance_travelled)

#2nd place
#place_2nd=" "
valid = False
while not valid:
    #choose a number from cars list, 1-12
    place_2nd = random.choice(cars)
    #print(add_car)
    distance_travelled[place_2nd-1] += 1

    if distance_travelled[place_2nd-1] == 15:

        if place_2nd==place_1st:
            continue
        break
    else:
        continue

#3rd place
#place_3rd=""
valid = False
while not valid:
    #choose a number from cars list, 1-12
    place_3rd = random.choice(cars)
    #print(add_car)
    distance_travelled[place_3rd-1] += 1

    if distance_travelled[place_3rd-1] == 15:
        #print(add_car)
        if place_3rd==place_1st:
            continue
        if place_3rd==place_2nd:
            continue
        break
    else:
        continue

#
print("The 1st place car {}" .format(place_1st))
print("The 2nd place car is {}" .format(place_2nd))
print("The 3rd place car is {}" .format(place_3rd))
