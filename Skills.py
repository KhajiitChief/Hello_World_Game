import sys
import time
import Herm_Char
player = Herm_Char.char = {"lvl" : 1,
                  "xp" : 0,
                  "lvlnxt" : 25}
class Ability():
    def level(self):
        nStr = 0
        nDex = 0
        nInt = 0
        while player["xp"] >= player["lvlnxt"]:
            player["lvl"] += 1
            player["xp"] = player["xp"] - player["lvlnxt"]
            player["lvlnxt"] = round(player["lvlnxt"] * 1.5)
            for i in """What SKILL would you like to increase???
Intellect(I)
Strength(S)
Dexterity(D)
""":
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.05)
            skill_point = input("").lower()
            if skill_point == "i":
                nInt += 1
            elif skill_point == "s":
                nStr += 1
            elif skill_point == "d":
                nDex += 1