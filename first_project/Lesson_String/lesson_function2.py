def create_record(name, telephone, address):
    """create record"""
    record ={
        "name":name,
        "phone":telephone,
        "address": address
    }
    return record


user1 = create_record("valera", "+380676724464","Lviv")
user2 = create_record("petro ", "+380666666432", "Kiev")

#very importent *objects must be last parameters
def give_award(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print("person: " + person.title() + " award :"+ medal)



print(user1)
print(user2)
give_award("Za lviv", "valera", "petro", "oleg")


