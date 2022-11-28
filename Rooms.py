from Inventory import Items, special_sword, steel_sword, stone_sword, special_armour, steel_armour, leather_armour, iron_armour, chain_mail, iron_sword, wood_sword
from Buildings import castle, your_house, office


class Room:
    name = "Room"
    detail = "Inside Room"


    def __init__(self, **kwargs):
        self.name = kwargs["name"] if "name" in kwargs else "Room Unavailable"
        self.detail = kwargs["detail"] if "detail" in kwargs else "There is nothing here..."
        self.objects = {}

    def append(self, object):
        self.objects[object.name] = object


feild = Room(name= "Field of Flowers", detail= "Beautiful flowers in full bloom fill the valley of the large surrounding circle of monstrous mountains...")

carriage = Room(name= "Time Carriage     ", detail= "Out the window streaming colors sly by ar you zip through time and space...")

bedroom = Room(name= "Herm's Bedroom    ", detail= "Your bedroom is tidy and bland...")
your_house.append(bedroom)
living_room = Room(name= "Living Room       ", detail= """Your Living room has a TV and a couch...
                    The room is orderly and plain...""", )
your_house.append(living_room)
kitchen = Room(name= "Kitchen           ", detail= "The kitchen has a fridge, sink, and a trash bin...", )
your_house.append(kitchen)
cubicle = Room(name= "Herm's Cubicle   ", detail= "Your cubicle has white walls with a desk and a computer...", )
office.append(cubicle)
door = Room(name= "Office Door      ", detail= "You walk through the door unnoticed by all your coworkers...", )
office.append(door)
parkinglot = Room(name= "Parking lot       ", detail= "The parking-lot is large with many cars around...", )
office.append(parkinglot)

castle_bedroom = Room(name= 'Castle Barracks', detail="Where the Guards sleep...")
your_bedroom = Room(name= "Herm's Quarters", detail= "Your room at Actrusinial...")
castle_kitchen = Room(name= 'The Castle Kitchen', detail="Num Nums...")
jarl_quarters = Room(name= "Jarl Wolgenshire's Quarters", detail="The Jarl sleeps here... Duh...")

#Objects Already in rooms

