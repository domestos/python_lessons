import json
filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='utf8')


player1 = {
    "PelayerName": "Donald Trump",
    "Score": 354,
    "awards": ["OR", "NV", "NY"]
}

player2 = {
    "PelayerName": "valera pelenskyi",
    "Score": 354,
    "awards": ["OR", "NV", "LV"]

}


myplayers = []
myplayers.append(player1)
myplayers.append(player2)

#--------------- SAVE JSON --------------------
json.dump(myplayers, myfile)
myfile.close()


#----------------LOAD JSON --------------------
myfile = open(filename, mode='r', encoding="utf8")
json_data = json.load(myfile)

for player in json_data:
    print("Playr Name is "+ str(player['PelayerName']))
    print("Score: "+str(player['Score']))
    print("awards:"+ str(player['awards']))