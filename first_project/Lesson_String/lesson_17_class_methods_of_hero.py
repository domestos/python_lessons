from Lesson_String.lesson_17_class_hero import HeroOfWAA

hero1= HeroOfWAA("valera", 100, 80, "xz", "Orc")
hero2= HeroOfWAA("petro", 100, 10, "xz", "Human")

hero1.show_hero()
hero2.show_hero()

hero1.move()
hero1.level_up()
hero1.set_health(120)
hero1.show_hero()
