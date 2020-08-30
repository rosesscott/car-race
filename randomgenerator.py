import random
cars = [1,2,3,4,5,6,7,8,9,10,11,12]


#show distances travelled
#inital distance_travelled = [0,0,0,0,0,0]
distance_traveled = [0,0,0,0,0,0,0,0,0,0,0,0]

#distance_travelled[add_car] +=1
#print(distance_traveled)
#add_car=
valid = False
while not valid:
    #choose a number from cars list
    add_car = random.choice(cars)
    #print(add_car)
    distance_traveled[add_car-1] += 1
    if distance_traveled[add_car-1] == 15:

        break
    else:
        continue

def race_tracking(mylist):
    counter=1
    for car_distance in mylist:
        print('car {} has moved \n'.format(counter)+"*"*car_distance)
        counter+= 1
#pass
race_tracking(distance_traveled)
print("the 1st place car is {}" .format(add_car))


