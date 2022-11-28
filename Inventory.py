class Inventory():
    def __init__(self):
        self.items = {}

    def append(self, item):
        self.items[item.name] = item
        if item.name in self.items:
            item.count = item.count + 1
        return item.count

    def remove(self, item):
        self.items[item.name] = item
        if item.name in self.items:
            item.count = item.count - 1

    def __str__(self):
        print("""-----------------------------------
***         |Inventory|         ***
-----------------------------------""")
        out = '\t'.join(["Name    ", "        Use"])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(c) for c in [item.name, "   ", item.use, "(", item.count, ")"]])
        return out


class Items():
    name = "name"
    use = "use"
    attack = 0
    armor = 0
    defense = 0
    count = 0
    magic = 0

    def __init__(self, **kwargs):
        self.name = kwargs['name'] if 'name' in kwargs else "item"
        self.use = kwargs['use'] if 'use' in kwargs else "This Item Has no Use..."
        self.attack = kwargs['attack'] if 'attack' in kwargs else "   "
        self.armor = kwargs['protection'] if 'protection' in kwargs else "   "
        self.defense = kwargs['block'] if 'block' in kwargs else "   "
        self.count = kwargs["count"] if "count" in kwargs else 0


inventory = Inventory()
leather_armour = Items(name= "Leather Armour", protection= .05, use= "Crappy Deflection Protection")
chain_mail = Items(name= "Chain Mail", protection= .20, use= "Meh Deflection Protection")
iron_armour = Items(name= "Iron Armour", protection= .30, use= "OK Deflection Protection")
steel_armour = Items(name= "Steel Armour", protection= .45, use= "Pretty Good Deflection Protection")
special_armour = Items(name= "Ridiculous Armour", protection= .65, use= "OP Deflection Protection")

Wood_shield = Items(name= "Wood Shield   ", block= .05, use= "Weak Bound Sticks")
Hide_shield = Items(name= "Hide Shield", block= .08, use= "Eeeh, It'll work for Blocking")
Iron_shield = Items(name= "Iron Shield", block= .10, use="Hey Now This'll Work to Block")
Steel_shield = Items(name= "Steel Shield", block= .25, use= "Oh yea, We're Awesome at Blocking Now")
Special_shield = Items(name= "Paper", block= .5, use= "A flimsy piece of paper")

wood_sword = Items(name="Wood Sword    ", attack= 5, block= .01, use= "Splinter City")
stone_sword = Items(name="Stone Sword   ", attack= 10, block= .02, use= "Better Than Throwing Throwing Rocks")
iron_sword = Items(name="Iron Sword    ", attack= 15, block= .025, use= "Iron Stabby Stabby")
steel_sword = Items(name="Steel Sword   ", attack= 25, block= .03, use= "Steel Slashy Slashy")
special_sword = Items(name="Simple Stick  ", attack= 40, block= .1, use= "A Stick?")

gold = Items()
inventory.append(wood_sword)
print(inventory)
inventory.remove(wood_sword)
print(inventory)