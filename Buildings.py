
class Building:
    name = "Structure"
    health = 0

    def __init__(self, **kwargs):
        self.name = kwargs["name"] if "name" in kwargs else "Structure"
        self.health = kwargs["health"] if "health" in kwargs else 800
        self.rooms = kwargs["rooms"] if "rooms" in kwargs else 3
        self.container = {}

    def append(self, room):
        self.container[room.name] = room

    def __str__(self):
        if self.rooms == 5:
            print("""
                |~>|~>
                |/\|
                /{}\ 
             /\/    \/\ 
            /()\_[]_/()\ 
           /____\/\/____\ 
    |~>     |  |/{}\|  |       |~>
    | /\   /|  / /\ \  |\   /\ |
    |/  \ / | / /__\ \ | \ /  \|
    / {} \| |/__|()|__\| |/ {} \ 
     |  |____|________|____|  |
 /\  |()|  o | O /\ O | o  |()|   /\ 
/{}\ |  |    |  /__\  |    |  |  /{}\ 
|  |~~~~~~~~~~~| || |~~~~~~~~~~~~|  |
|  |    []    /| || |\    []     |  |
|__|__________|  ||  |___________|__|
""")
        elif self.rooms == 4:
            print("""
                ____
               /O\  \ 
         ___ __|_|__|__
        / () \         \ __
       /|    |\         \||
  __ ___|_[]_|_________|_||_
 /   \  _/o\         _/o\    \ 
/ {} \  |_|          |_|     \ 
|     | {}    ()     ()    {} |
| []  |_______________________|
""")
        elif self.rooms == 3:
            print("""
             ___
  ____ _____/_/ \_____
 /    \       |O|      \ 
/ |__| \________________\ 
|      |   []      []  |
|*\[]/*|_____&_####__%_|
""")
        elif self.rooms == 2:
            print("""
 ___ ____||__
/_   \_______\ 
 | /\ | ()  |
 | || |$ ## |
 """)
        elif self.rooms == 1:
            print("""
 ___ ____
/_()_\___\ 
| [] |* *|
""")
        elif self.rooms == 20:
            print("""
 _______________________
|      THE  OFFICE      |
|  []  []       []  []  |
|                       |
|  []  []  [_]  []  []  |
|                       |
|  []  []  ___  []  []  |  
|_________|_|_|_________|
""")
        elif self.rooms == 30:
            print("""
Welcome to your house navigate by typing which room you would like to go to
Each building will have a set of rooms you can enter and search
Blah blah blah....
  ________       
 /        \ 
/|  d()b  |\ 
 | * [] ? |
 """)
        out = '\t'.join(["Name    ", "        Detail"])
        for room in self.container.values():
            out += '\n' + '\t'.join([str(c) for c in [room.name, room.detail]])
        return out


office = Building(name= "Office", rooms= 20)
your_house = Building(name= "Your House", rooms= 30)
castle = Building(name= "Actrusinial", health= 100000, rooms= 5)
