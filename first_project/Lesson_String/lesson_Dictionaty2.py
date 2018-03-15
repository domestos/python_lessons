enemy = {
    'loc_x':70,
    'loc_y':50,
    'color': 'green',
    'health': 100,
    'name': 'valera',
    'awards': ['Za Kiev', 'Za Lviv', 'Za All'],
    'image' : ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg']
}


#create array
all_enemy = []

#add one object (link of object) into array
for x in range(0,5):
    all_enemy.append(enemy)

#edit vaule in object enemy
all_enemy[2]['health'] = 30

#print array
for en in all_enemy:
    print(en)

#======================================================================

print('\nnew array with different objects\n')

all_enemy2 = []

#add new object into array
for x in range(0,5):
    enemy['health'] = 100
    all_enemy2.append(enemy.copy())

#edit elements into array
all_enemy2[3]['health'] = 10
all_enemy2[4]['health'] -= 20
all_enemy2[2]['name'] = "igor"
all_enemy2[3]['name'] += " pelenskyi"


for en in all_enemy2:
    print(en)







