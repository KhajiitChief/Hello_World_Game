import pygame
import random
import time
import sys
from Buildings import office, your_house
from Rooms import bedroom, living_room, feild, cubicle, parkinglot, carriage, kitchen, door

aplgy = "Sorry you can't do that..."


def br():
    while True:
        print(your_house)
        print("You are in your bedroom...")
        print("What do you want to do?")
        nav = input("").lower()
        if nav == "living room":
            lr()
        elif nav == "i":
            print("     Inventory Contents")
        else:
            print(aplgy)

def lr():
    while True:
        print(living_room.detail)
        print("What do you want to do?")
        nav = input().lower()
        if nav == "bedroom":
            br()
        elif nav == "kitchen":
            kr()
        elif nav == "work":
            print(office)
            pkgl()
        else:
            print(aplgy)

def kr():
    while True:
        print(kitchen.detail)
        print("What do you want to do?")
        nav = input("").lower()
        if nav == "living room":
            lr()
        else:
            print(aplgy)
def pkgl():
    print(parkinglot.detail)
    while True:
        print("You can go into work or go home...")
        nav = input("").lower()
        if nav == "work":
            od()
        elif nav == "home":
            lr()
        else:
            print(aplgy)
def pkgl2():
    print(parkinglot.detail)
    for b in """Herm, once outside, asked, “What did you come here for?” 
the goliath thought for a moment then reached inside a satchel bag on his hip to retrieve an ancient document,
he held it out for Herm to take. Herm quickly looked down and had no idea what the parchment was showing. 
    “I am Gerekaal, a warrior from thy Secret Shadow Guild in Yrtrelia,” said Gerekaal. 
He had traveled all the way to Herm’s office to retrieve him for a quest that was discovered centuries ago. 
Herm looked at Gerekaal, his face sour, and said, “I think you were looking for someone else,” 
and turned to go back inside. Gerekaal grabbed Herm by the arm and dragged him to the horse carriage 
he had arrived in. Herm, confused and unable to break the iron grip of Gerekaal, 
sat and stared like a fish on a hook. The insanely strong Gerekaal hurled him into the carriage with ease.
""":
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(.025)
    cg()
def cg():
    print(carriage.detail)
    for i in """Now in the carriage Gerekaal opened a chest in the back, 
he pulled a full suit of armor for Herm to put on. 
Herm struggled to maneuver the leather and looked at Gerekaal. 
    “Wear thy armor, it shall protect thou well,” Gerekaal said calmly. 
Herm wanted to argue, but after being dragged into the carriage he knew he had no choice. 
After the struggle of putting all the armor on, Herm had trouble moving. 
Curious why he had just been manhandled into this large wooden box by a medieval brute. 
Nervously, he asked, “So where is the great Gerekaal from?” 
Gerekaal, now sitting and staring at the paper he had earlier, said, 
    “I am from a small village in Kavlearsted. When I was young I was an orphan and stole to survive. 
     I was recruited by thine Secret Shadow Guild at age 12, served thy Guild with e’ery need I was able to do.” 
Herm felt bad about Gerekaal’s childhood, but was still more worried about where he was being taken.
""":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.025)
    fd()


def fd():
    print(feild.detail)
    for i in """Suddenly, there was a large explosion outside of the carriage and Herm dropped to the wooden floor. 
The cart rocked a bit until another large explosion rang out, Herm was still laying on the floor panicking, repeating, 
    “I’m gonna die, I’m gonna die, I’m gonna die. Yep, this is where I die.” The carriage stopped and Gerekaal stood and tapped Herm with his foot, 
    “Aah!,” screamed Herm, “Where the heck are we! Why am I stuck here with you? Oh, I must be going insane; yep, I’ve lost my mind, I’ve⎼”,
    “Herm! Get a hold of thyneself! We are here. We must go. Now!”, commanded Gerekaal. 
Herm, shocked, having trouble getting his thoughts straight, was only able to ask, 
    “Where exactly is here?” Gerekaal again remained quiet and opened the carriage door. 
Outside were lush green fields, fully bloomed bushes and beautiful trees covered with fruits and flowers 
that caused Herm to lose all sense of fear and anxiety, he was only captivated by the view and stunned in awe of the amazing beauty of this foreign land. 
    “This is the great Yrtrelia, the richest kingdom of all Tritorsu,” Gerekaal whispered to Herm.
""":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.025)
    input("Herm and Gerekaal head toward the castle...")
    cl()
def cl():
    pass
def od():
    print(door.detail)
    oc()
def oc():
    print(cubicle.detail)
    for x in """You open your computer and find your task list...
As always you work averagely, and normally...
""":
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(.025)
    for c in """Suddenly...
a commotion took Herm's attention...
""":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.025)
    print("Herm goes to investigate...")
    input("")
    for v in """A large warrior dressed in armor arrived around noon that day. 
The giant brute looked as though he had walked out of a medieval painting, and was looking for an employee.
This employee was Herm of course. When this fine gent asked the receptionist with an aggressive, commanding voice,
    “Where art thou mighty Herm the Inadequate concealed”, the now shaking receptionist replied that she did not know of a Herm
ever working there. Herm, having luckily been using the copier, leaned over and spoke quietly, 
    "I-I’m Herm.” The monstrous man turned to Herm scaling him up and down. 
Then almost silently whispered, “ Thou title fits ye accurately.” Herm had no idea why this 
strange warrior had come for him so he walked over and said, 
    “Maybe we should talk in private.” “As ye wish sir Herm,” said the mysterious man as he turned to leave. 
As they walked out the giant’s steps shook the building, almost as if his boots were made of solid steel...
""":
        sys.stdout.write(v)
        sys.stdout.flush()
        time.sleep(.025)
    pkgl2()
while True:
    print("Welcome player, to Herm The Inadequate...")
    print("Would you like to play?")
    start = input("").lower()
    if start == "no":
        exit("Well then be gone with you!!!")
    elif start == "yes":
        print("Welcome new player...")
        print("Type where you wish to go and what you wish to do...")
        print("If you need HELP just ask...")
        for n in """One fine morning, Herm, a normal desk jockey, went into work as always.
Although Herm has had a very normal life, nobody knew the greatness that would become of him.
Herm sat at a lonely desk surrounded by walls in the back of the office where he worked.
Little conversations between coworkers is all the social interaction Herm acquired.
All he had ever been, was normal, blending in with all that surrounded him... until today.
Today was no ordinary day. Herm, whether he is prepared or unprepared, had to help...
""":
            sys.stdout.write(n)
            sys.stdout.flush()
            time.sleep(.025)
        br()
    else:
        print("Please use YES or NO...")
