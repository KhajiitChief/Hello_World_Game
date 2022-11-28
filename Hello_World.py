import sys
import time
from Inventory import inventory
from Inventory import Items
from Store_Cart import cart

lab_key = Items(name= "Lab Key       ", use= "Obviously to get into your lab")
mp =  Items(name= "Map           ", use= "It's a map...")
map = ["Home", "Lab"]
map2 = ["Home", "Lab", "Store"]
options = ["Go OUTSIDE", "Check FRIDGE", "Open (I)nventory"]
inventory.append(mp)
FdgNte = Items(name= "Fridge Note   ", use= "To go shoppin'...")
fridge_note = ["soda", "crackers", "bread"]
lab_note = Items(name= "Note from Lab ", use= "Something to do in the lab...")
Note = "Password is 123456789"
wallet = Items(name= "Wallet        ", use= "To go broke...")
soda = Items(name= "Soda          ", use= "Drink")
crackers = Items(name= "Crackers      ", use= "Food")
bread = Items(name= "Bread         ", use= "Food")
metal_scraps = Items(name= "Metal Scraps  ", use= "Material")
feathers = Items(name= "Feathers      ", use= "Materials")
wood = Items(name= "Wood Material ", use= "Clearly for crafting...")
reactor_code = Items(name= "Reactor Code  ", use= "Start the reactor core...")
pie_code = Items(name= "Pie???        ", use= "I don't have a clue where a you would need a number to activate something...")
shny_trsh = Items(name= "Shiny Trash   ", use= "You just like to hoard stuff huh???")

def house():
    while True:
        print("""You are at home...
What would you like to do???
For list of commands type OPTIONS...""")
        do = input("").lower()
        if do == "outside":
            outside()
        elif do == "fridge":
            print("Your milk is soured...")
        elif do == "options":
            print(options)
        elif do == "i":
            while True:
                print(inventory)
                rturn = input("Open item or Exit...").lower()
                if rturn == "map":
                    for i in map:
                        print(i)
                elif rturn == "fridge note":
                    for i in fridge_note:
                        print(i)
                elif rturn == "note":
                    print(Note)
                elif rturn == "exit":
                    house()
        elif do == "search":
            if lab_key.name in inventory.items:
                print("You already have your LAB KEY...")
                house()
            print("Ahh there's your LAB KEY...")
            print("Do you pick it up???")
            key = input("").lower()
            if key == "yes":
                inventory.append(lab_key)
            elif key == "no":
                house()
        else:
            print("Use OPTIONS to help navigate...")

def house2():
    while True:
        print("""You are at home...
What would you like to do???
For list of commands type OPTIONS...""")
        do = input("").lower()
        if do == "outside":
            outside2()
        elif do == "fridge":
            print("Your milk is soured...")
            if FdgNte.name not in inventory.items:
                print("You notice a note on your fridge...")
                print("Do you take it???")
                fn = input("")
                if fn == "yes":
                    inventory.append(FdgNte)
            else:
                print("Your milk is soured...")
        elif do == "options":
            print(options)
        elif do == "i":
            print(inventory)
            rturn = input("Open item or Exit...").lower()
            if rturn == "map":
                for i in map2:
                    print(i)
            elif rturn == "fridge note":
                if "Fridge Note" in inventory.items:
                    for i in fridge_note:
                        print(i)
                else:
                    print("There is no item with that name in your Inventory...")
            elif rturn == "note":
                if "Note" in inventory.items:
                    print(Note)
                else:
                    print("There is no item with that name in your Inventory...")
            elif rturn == "exit":
                house2()
        elif do == "search":
            if "Wallet" in inventory.items:
                print("You already have your Wallet...")
                house2()
            print("Ahh there's your Wallet...")
            print("Do you pick it up???")
            key = input("").lower()
            if key == "yes":
                inventory.append(wallet)
            elif key == "no":
                house2()
        else:
            print("Use OPTIONS to help navigate...")

def outside():
    while True:
        print("""You look at your map...
You can go HOME or to the LAB""")
        out = input("").lower()
        if out == "home":
            house()
        elif out == "lab":
            labdoor()
        else:
            print("More options to come...")
def outside2():
    while True:
        print("""You notice the sign light on at the Superstore...
You look at your map...
You can go HOME, the STORE, or to the LAB""")
        out = input("").lower()
        if out == "home":
            house2()
        elif out == "store":
            store()
        elif out == "lab":
            labdoor2()
        else:
            print("More options to come...")

def store_soda():
    for w in """You arrive at the Drink Isle...
You search high and low until you find your favorite soda...
Do you grab it???
""":
        sys.stdout.write(w)
        sys.stdout.flush()
        time.sleep(.05)
    while True:
        take = input("").lower()
        if take == "yes":
            cart.append(soda)
            store_front()
        elif take == "no":
            store_front()
        else:
            for i in """Please Use YES and NO to Choose...""":
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.05)

def store_crackers():
    for i in """You are on the snack isle...
You see your preffered brand of crackers...
do you grab one???
""":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.05)
    while True:
        take = input()
        if take == "yes":
            cart.append(crackers)
        elif take == "no":
            store_front()
        else:
            for w in """Please Use YES and NO to Choose...""":
                sys.stdout.write(w)
                sys.stdout.flush()
                time.sleep(.05)

def store_bread():
    for i in """As you stroll through the isles you find they have your favorite bread in stock...
You contemplate and wonder if you should grab some...
Do you choose to take the bread???
""":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.05)
    while True:
        take = input()
        if take == "yes":
            cart.append(bread)
        elif take == "no":
            store_front()
        else:
            for w in """Please Use YES and NO to Choose...""":
                sys.stdout.write(w)
                sys.stdout.flush()
                time.sleep(.05)

def store_chckout():
    for c in """You pay for your groceries, but as you walk out 
you remember you forgot milk...""":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.05)
    store_milk()

def store_front():
    for w in """You are at the front of the store...
What are you looking for???
""":
        sys.stdout.write(w)
        sys.stdout.flush()
        time.sleep(.05)
    while True:
        go = input("").lower()
        if go == "soda":
            if "Soda" in cart.items:
                for v in """You already have Soda...""":
                    sys.stdout.write(v)
                    sys.stdout.flush()
                    time.sleep(.05)
            else:
                store_soda()
        elif go == "crackers":
            if soda.name in cart.items:
                for i in "You already have Crackers...":
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    time.sleep(.05)
            else:
                store_crackers()
        elif go == "bread":
            if bread.name in inventory.items:
                for g in """You already have Bread""":
                    sys.stdout.write(g)
                    sys.stdout.flush()
                    time.sleep(.05)
            else:
                store_bread()
        elif go == "milk":
            store_milk()
        elif go == "i":
            while True:
                print(inventory)
                rturn = input("Open item or Exit...").lower()
                if rturn == "map":
                    for i in map2:
                        print(i)
                elif rturn == "fridge note":
                    if FdgNte.name in inventory.items:
                        for i in fridge_note:
                            print(i)
                    else:
                        print("There is no item with that name in your Inventory...")
                elif rturn == "note":
                    if lab_note.name in inventory.items:
                        print(Note)
                    else:
                        print("There is no item with that name in your Inventory...")
                elif rturn == "exit":
                    store_front()
        else:
            for c in """I'm afraid that's not an item you need...""":
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(.05)

def store_milk():
    for c in """You approach the cooler where the milk is...
As you open the door a force pulls you into the darkness below...
""":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.05)
    import HtI
def store():
    print("""Welcome to the Supermarket...
If you have a grocery list you can buy items here...""")
    if FdgNte.name in inventory.items:
        if wallet.name in inventory.items:
            store_front()
    elif FdgNte.name not in inventory.items:
        print("You might have a grocery list at home...")
        if wallet.name not in inventory.items:
            print("""You'll need some way to buy stuff...
You probably left your wallet at home...""")
            outside2()

        
def labdoor():
    print("The Lab door is locked, you'll need your key to open it...")
    if lab_key.name in inventory.items:
        while True:
            print("Do you unlock the door???")
            ladoor = input("").lower()
            if ladoor == "yes":
                lab()
            elif ladoor == "no":
                outside()
            else:
                print("Use YES and NO to answer...")
    if lab_key.name not in inventory.items:
        print("""You must have left your key at home..."
You'll need to go search for it...""")
    outside()
def labdoor2():
    print("The Lab door is locked, you'll need your key to open it...")
    if lab_key.name not in inventory.items:
        while True:
            print("Do you unlock the door???")
            ladoor = input("").lower()
            if ladoor == "yes":
                lab2()
            elif ladoor == "no":
                outside2()
            else:
                print("Use YES and NO to answer...")
    if "Lab Key" not in inventory.items:
        print("""You must have left your key at home..."
You'll need to go search for it...""")
    outside2()
def lab():
    while True:
        print("""Welcome to your lab...
You can access your COMPUTER and see the REACTOR or go OUTSIDE...
Where would you like to go???""")
        laboratory = input("").lower()
        if laboratory == "reactor":
            print("Reactor is not running...")
        elif laboratory == "computer":
            computer()
        elif laboratory == "outside":
            outside()
        elif laboratory == "i":
            while True:
                print(inventory)
                rturn = input("Open item or Exit...").lower()
                if rturn == "map":
                    for i in map:
                        print(i)
                elif rturn == "fridge note":
                    if "Fridge Note" in inventory.items:
                        for i in fridge_note:
                            print(i)
                        else:
                            print("You do not have an item with that name...")
                elif rturn == "note":
                    if lab_note.name in inventory.items:
                        print(Note)
                    elif "Note from Lab" not in inventory.items:
                        print("You do not have an item with that name...")
                elif rturn == "exit":
                    lab()
        elif laboratory == "search":
            if "Note from Lab" in inventory.items:
                print("You look around, but don't see anything unusual...")
                lab()
            print("""You found a note...
Do you pick it up...""")
            note = input("").lower()
            if note == "yes":
                inventory.append(lab_note)
            else:
                print("You leave the note on the floor...")
            lab()
        else:
            for i in """Input not registered..."
Please try again...""":
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.03)

def lab2():
    while True:
        for i in """Welcome to your lab...
You can access your COMPUTER and see the REACTOR or go OUTSIDE...
Where would you like to go???""":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(.03)
        laboratory = input("").lower()
        if laboratory == "reactor":
            print("Reactor is running...")
        elif laboratory == "computer":
            computer()
        elif laboratory == "outside":
            outside2()
        elif laboratory == "i":
            while True:
                print(inventory)
                rturn = input("Open item or Exit...").lower()
                if rturn == "map":
                    for i in map2:
                        print(i)
                elif rturn == "fridge note":
                    if "Fridge Note" in inventory.items:
                        for i in fridge_note:
                            print(i)
                        print("You do not have an item with that name...")
                elif rturn == "note":
                    if "Note from Lab" in inventory.items:
                        print(Note)
                    else:
                        print("You do not have an item with that name...")
                elif rturn == "exit":
                    lab2()
        elif laboratory == "search":
            if "Note from Lab" in inventory.items:
                print("You look around, but don't see anything unusual...")
                lab2()
            print("""You found a note...
Do you pick it up...""")
            note = input("").lower()
            if note == "yes":
                inventory.append(lab_note)
            else:
                print("You leave the note on the floor...")
            lab2()
        else:
            print("""Input not registered..."
Please try again...""")

def pil2():
    while True:
        pie2 = input("Uhh You Probably Shouldn't Eat That...").lower()
        if pie2 == "eat":
            print("No You Can't Eat This...")
            pil3()
        elif pie2 == "ok":
            break
        else:
            print("Let's Go Back...")
def pil3():
    while True:
        pie3 = input("Go Back to Home...").lower()
        if pie3 == "eat":
            print("Fine...")
            print("I Guess I Can't Stop You...")
            print("*You Eat the Pie...")
            print("Suddenly...")
            print("You Feel Funny...")
            input("")
            print("Everything Goes Dark...")
            print("Goodbye, World...")
            print("Pie Ending Achieved!!!")
            time.sleep(5)
            for i in """.
.
.""":
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(.5)
            import HtI
        elif pie3 == "ok":
            break
        else:
            print("Just Go Back...")


def computer():
    print("This is your computer, you can access it with a password or exit using SHUTDOWN...")
    power = input("[Power Button]")
    list1 = ["[Games]  [Documents]  [Internet]  [Trash Bin]  [Reactor]"]
    games = ["[Minecraft]  [Skyrim]  [Warframe]  [DND]  [War Thunder]"]
    documents = ["[Lab Reports]  [Memes]  [H.W. Project] [Pie]  [Other Junk]"]
    password = ("123456789")
    if power == (""):
        print("Booting Power Systems...")
    boot = input("Enter Password. >")
    while boot != password:
        if boot == "shutdown":
            break
        print("      ERROR!")
        print("Password Incorrect...")
        boot = input("Enter Password. > ")
    if boot == password:
        print("Password Accepted...")
        print("   Logging In...")

        while True:
            print(list1)
            app = input("Open Folder...").lower()
            if app == ("games"):
                print("Getting Files Ready...")
                while True:
                    print(games)
                    play = input("Choose a Game You Wish to Play or Type Home to Return to Application Screen...").lower()
                    if play == "minecraft":
                        print("You Are Suddenly in a Block World Fighting for Your Life Day and Night...")
                        print("Theres No End to This Game...")
                        print("But, at Least You Have an Awesome Dirt House...")
                        while True:
                            if wood.name not in inventory.items:
                                print("""You Cut Down a Treee and Got Some Wood...
Do You Want to Take it With You???""")
                                irn = input("").lower()
                                if irn == "yes":
                                    print("""You Leave The Block World... 
Snagging The Wood as You Leave...""")
                                    inventory.append(wood)
                                    break
                                elif irn == "no":
                                    print("You Leave The Wood Behind as You Exit...")
                                    break
                                else:
                                    print("Use YES and NO to Choose...")
                            else:
                                print("You've Got Everything You Needed...")
                    elif play == "skyrim":
                        print("You Slayed a Dragon and Saved the Town!!!")
                        time.sleep(.2)
                        print("But You Accidentally Killed a Chicken so Now You're Public Enemy #1...")
                        while True:
                            print("Do You Harvest The Chicken's Feathers???")
                            fthr = input("").lower()
                            if fthr == "yes":
                                if feathers.name not in inventory.items:
                                    print("You Grab Some Feathers From The Bird...")
                                    inventory.append(feathers)
                                    break
                                else:
                                    print("You already collected some Feathers...")
                                    break
                            elif fthr == "no":
                                print("You Decide to Leave The Chicken and Run Away as Fast as Possible...")
                                break
                            else:
                                print("Use YES and NO to Choose...")
                    elif play == "warframe":
                        print("You Somersault Through the Air Conquering Those Who Stand in Your Way Across the Galaxy...")
                        print("""You Notice a Pile of Scraps Near...
Do You Take Some???""")
                        while True:
                            picup = input("").lower()
                            if picup == "yes":
                                if metal_scraps.name not in inventory.items:
                                    print("""You Take Some Scraps With You...
Maybe They'll Come in Handy Later...""")
                                    inventory.append(metal_scraps)
                                    break
                                else:
                                    print("You already have some Sraps hoarder...")
                                    break
                            elif picup == "no":
                                print("You Leave The Scraps to Rust...")
                                break
                            else:
                                print("Do You Want The Scraps??? (YES or NO)")
                    elif play == "dnd":
                        print("New Quest-line Under Construction...")
                    elif play == "war thunder":
                        print("Tanks, Planes, and Battleships!!!")
                        print("     My Kinda Party...")
                    elif play == "home":
                        break
                    else:
                        print("Sorry That File Does Not Exist in This List...")
            elif app == "documents":
                print("Loading Boring Stuff...")
                while True:
                    print(documents)
                    doc = input("Choose a Document...").lower()
                    if doc == "lab reports":
                        print("Redacted, Redacted, Redacted, and...")
                        print("Redacted...")
                    elif doc == "memes":
                        print("""( ͡❛ ͜ʖ ͡❛)
                Get Back to Work!!!""")
                    elif doc == "h.w. project":
                        print("Reactor Code is 8675309...")
                        if reactor_code.name not in inventory.items:
                            inventory.append(reactor_code)
                        else:
                            print("""Do You really want to make more copies???
You already have one...""")
                    elif doc == "pie":
                        print("What is 3.1415926535...")
                        if pie.name not in inventory.items:
                            inventory.append(pie_code)
                        else:
                            print("""No more copies for you!!!
You got a copy already, leave some for other players...""")
                    elif doc == "other junk":
                        print("Nothing but tattered papers in here...")
                    elif doc == "home":
                        break
                    else:
                        print("Document Not Found...")
            elif app == "internet":
                print("Looks Like You're Not Connected...")
            elif app == "trash bin":
                while True:
                    print("Just More Junk Needing to be Cleaned...")
                    trash = input("").lower()
                    if trash == "search":
                        while True:
                            if shny_trsh.name in inventory.items:
                                print("There's nothing left to get here...")
                                break
                            shob = input("What is that shiny object???")
                            if shob == "look":
                                if shny_trsh.name not in inventory.items:
                                    print("Oh, Just More Trash...")
                                    inventory.append(shny_trsh)
                                else:
                                    print("You really don't need more trash...")
                    elif trash == "home":
                        break
                    else:
                        print("Why do You Want to Hang Around Trash???")
            elif app == "reactor":
                while True:
                    reactor = input("Enter Authorized Code...")
                    if reactor == "8675309":
                        print("Authorization Complete...")
                        while True:
                            command = input("Do You Wish to Start Reactor???").lower()
                            if command == "yes":
                                print("Reactor Enabled...")
                                print("Power Initializing...")
                                print("Machine Powering up...")
                                print("Machine Status... Online...")
                                input("{Run}")
                                print("Hello, World!")
                                lab2()
                            elif command == "no":
                                break
                    elif reactor == "3.1415926535":
                        print("Reactor Oven has Popped Out a Pie...")
                        while True:
                            pie = input("Do You Eat the Pie???").lower()
                            if pie == "yes":
                                pil2()
                            elif pie == "no":
                                break
                    elif reactor == "home":
                        break
                    else:
                        print("Authorization Code Invalid...")
            elif app == "shutdown":
                print("Power Systems Shutting Down...")
                break
            else:
                print("Navigate by Typing Which Selection You Want to Open or Use SHUTDOWN to Power Off...")


while True:
    print("Welcome to Hello World Program...")
    print("Would you like to play?")
    start = input("").lower()
    if start == "no":
        exit("Well then be gone with you!!!")
    elif start == "yes":
        print("Welcome new player...")
        print("You need to start the reactor to begin...")
        print("Type where you wish to go and what you wish to do...")
        print("If you need HELP just ask...")
        house()
    else:
        print("Please use YES or NO...")






#end of HELLO WORLD program
#print("Hello, World!")