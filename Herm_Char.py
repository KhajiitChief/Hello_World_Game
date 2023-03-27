import random
class Hero:
    name = "Herm"
    cLvl = 1
    skill_evade = 1
    health = 5
    damage = 3
    block = 1
    protection = 0
    isAlive = True

    def __init__(self, **kwargs):
        self.name = kwargs["name"] if "name" in kwargs else "Herm"
        self.health = kwargs["health"] if "health" in kwargs else 5
        self.protection = kwargs["protection"] if "protection" in kwargs else 0
        self.damage = kwargs["damage"] if "damage" in kwargs else 3
        self.skill = kwargs["skill"] if "skill" in kwargs else 0

    def attack(self, value, dType = "Future"):
        value = self.damage
        total = value + self.skill
        return total

    def hit(self, ALv, ACH, dType = "Future"):
        DLv = self.cLvl
        DAC = self.skill_evade
        return 100 * ACH / (ACH + DAC) * 2 * ALv / (ALv + DLv)

    def hard_Def(self, value, dType = "Future"):
        return value < self.block

    def mit_Def(self, value, dType = "Future"):
        return value - self.protection

    def resist(self): pass
        #-damage = res < 100% : +health = res >= 100%

    def apply_damage(self, pool, value):
        pool_damage = getattr(self, pool) - value
        setattr(self, pool, pool_damage)
        return value

    def damage_health(self, value, dType = "Future"):
        return self.apply_damage("health", value)

    def alive(self):
        return 0 < self.health

    def die(self):
        self.isAlive = False
        self.health = 0
        print("You Died...")

    def recieve_attack(self, ALv, ACH, DMG, dType = "Future"):
        chance = self.hit(ALv, ACH)
        roll = random.randrange(1, 7)
        if roll > (chance * 6)/100:
            hp_dmg = self.damage_health(DMG)
            alive = self.alive()
            return(roll, "Hit!", alive, hp_dmg)
        else:
            return(roll, "Missed!")

        result = self.mit_Def(DMG, dType)
        if not self.alive():
            self.die()

if __name__ == "__main__":

    char = Hero(health= 10, )
    chance_hit = char.recieve_attack(1, .5, 8)
    print(chance_hit)
    print(char.__dict__)
