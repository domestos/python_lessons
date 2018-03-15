cars = ['bmv', 'lada', 'seat', 'skoda']

for car in cars:
    print(car.upper())


for x in range (0, len(cars)):
    print(x)
    print(cars[x])
    print("====================")



mynumber_list = list(range(0,10))
print(mynumber_list)

for x in mynumber_list:
        x = x *2
        print(x)


mynumber_list.sort(reverse=True)
print(mynumber_list)


print("My max number is: " + str(max(mynumber_list)))
print("My Min number is: " + str(min(mynumber_list)))
print("My Sum is: " + str(sum(mynumber_list)))
print("=============================================\n")

mycars = cars[1:3]  #start from 1 element and to 3
print(mycars)

mycars = cars[-3:]  #start from 1 element and to 3
print(mycars)

#copy list
mycars = cars[:]
print(mycars)
