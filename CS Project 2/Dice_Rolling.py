import random

class Fighter():
    player_health = 0
    dmg = 0

    def __init__(self, **kwargs):
        self.player_health = kwargs[player_health] if player_health in kwargs else 10
        self.dmg = kwargs[dmg] if dmg in kwargs else 2

    def damage_health(self, value, dType = "Future"):
        return self.apply_damage("health", value)

    def apply_damage(self, pool, value):
        pool_damage = getattr(self, pool) - value
        setattr(self, pool, pool_damage)
        return value

    def alive(self):
        return 0 < self.player_health

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

player_1 = Fighter(player_health= 8, dmg= 4)
print(player_1.__dict__)