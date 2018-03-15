class HeroOfWAA():
    """this class create the hero for our game"""

    def __init__(self, name, health, level, model, race):
        """Initiate our hero"""
        self.name = name
        self.health = health
        self.level = level
        self.model = model
        self.race = race


    def show_hero(self):
        """Print the hero"""
        discription = (self.name + " Level " + str(self.level) + " health "+str(self.health)+" model "+ self.model+" race "+self.race+"\n")
        print(discription)

    def level_up(self):
        """Upgrade the level of hero"""
        self.level +=1

    def move(self):
        """Start moving the hero"""
        print("Hero "+ self.name  + "is moving")

    def set_health(self, new_health):
        """Set new health"""
        self.health = new_health

#extend
class SuperHero(HeroOfWAA):
    """extended class """
    def __init__(self,  name, health, level, model, race, magiclevel):
        """Initiate the superhero"""
        super().__init__(name, health, level, model, race)
        self.magiclevel = magiclevel
        self.__magic =100

    def makemagic(self):
        """use magic"""
        self.__magic -=10

    #Overwrite super function
    def show_hero(self):
        discription = (self.name + " Level " + str(self.level) + " health "+str(self.health)+" model "+ self.model+" race "+self.race+" magic is: "+str(self.__magic)+"\n")
        print(discription)


