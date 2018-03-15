

x = 25

if x == 25:
    print("yes")
else:
    print("no")


age = 31
if (age <=4):
    print("You are baby!")
elif (age> 4) and (age<12):
    print("you are kid")
elif (age >=12) and (age < 19):
    print("you are teenager")
else:
    print("you are old")

    all_cars = ['chrusler', 'vm','dacia', 'bmv', 'kia', 'seat', 'skoda', 'lada', 'audi', 'ford']
    german_cars = ['bmw', 'vm', 'audi']

    if 'lada' in all_cars:
        print("Lada is in the list!")
    else:
        print("Not in the list")



for car in all_cars:
     if car in german_cars:
          print(car + " is German Car")
     else:
           print(car + " is not German car")