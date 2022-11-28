class Enemy:
    name = "Enemy"
    health = 1
    damage = 1
    protection = 0
    skill = 1
    def __init__(self, **kwargs):
        self.name = kwargs["name"] if "name" in kwargs else "Enemy"
        self.health = kwargs["health"] if "health" in kwargs else 5
        self.damage = kwargs["damage"] if "damage" in kwargs else 1
        self.protection = kwargs["protection"] if "protection" in kwargs else 0
        self.skill = kwargs["ALv"] if "ALv" in kwargs else 1

    def show(self):
        print(f"{self.name} has {self.health} hp, {self.protection} armour rating, and deals {self.damage} damage...")


ittan_momen = Enemy(name= "Cotton Roll of Death", health= 6, damage= 2)
draugr = Enemy(name= "Draugr", health= 8, damage= 4, proteciton= .1, ALv= 2)
