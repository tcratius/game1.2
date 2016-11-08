import msvcrt as m
import random
from sys import exit

def finds_sword():
    change_weapon = "sword"
    print "You find a secret wardrobe with a sword in it, Awesome!."
    print "Picking up the %r" % change_weapon,
    print "you give it a swing it and smile, 'this will come in handy'."
    return change_weapon


def finds_armour():
   print "You find some really futuristic armour and put it on adding 5 points"
   print "to health points. press 1 of 2"
   add_to_hp = 5
   return add_to_hp

# randomly generates attack on monsters
def attack(back):
    strike = random.randint(0, back)
    return strike

# takes in string fist or sword and assigns them a integer value
def weapon_selection(selected):
    if selected == "fist":
        human_dmg = 3
        return human_dmg
    elif selected == "sword":# returns sword when found
        human_dmg = 6
        return human_dmg
    else:
        print "not sure"
        exit(0)
# pauses until
def wait():
    m.getch()

def intro():
    print "\nYou work for a mad scientist who is working on the first telli-portation"
    print "machine. So far they have sent through a coffee cup, a spider and transported"
    print "most of them back.  Due to this success they asked for a volunteer to check"
    print "things out. Without realising you put your hand up to go. What was I thinking."
    print "        ~~~~~~~~~~ PRESS ANY KEY TO CONTINUE ~~~~~~~~~~        \n"
    wait()

def room_a():
    hp = 10
    sel = "fist"
    weapon = weapon_selection(sel)
    finds_defence = False
    print "The machine telliports you to a dark room. You get out your flash"
    print "light and realise your gun is missing! You pull out your compass"
    print "and find that it stil works. There is a cool breeze coming from"
    print "the wall to the east of you. Lying to the south is hallway."
    print "Choose an option\n"
    print "\t* Go south [1]:"
    print "\t* Search room [2]:"

    i = 0
    for i in range(10):

            room_a_choice = int(raw_input("-> "))
            if room_a_choice == 1:
                intersection_south(hp, weapon)
            elif room_a_choice == 2:
                if finds_defence == False:
                    hp = hp + finds_armour()
                    finds_defence = True
                    continue
                elif finds_defence == True:# add extra hit points to health
                    sel = finds_sword()
                    weapon = weapon_selection(sel)
                    print "There is nothing more to find.\n"
                    intersection_south(hp, weapon)
                    exit(0)
            elif room_a_choice != 1 or room_a_choice != 2: # or room_a_choice != 3:
               print "Please learn to read. Press 1 or 2"
            else:
                intersection_south(hp, weapon)

    return hp, weapon



def intersection_south(human_hp, human_damage):
    print """Walking down a hallway, you come to an intersection going
    (s) south
     and
    (e) east. Please select your direction"""
    fight_s_happened = False
    i = 0
    for i in range (10):
        inter_south = raw_input("-> ")
        if inter_south == "s" or inter_south == "S":
            print "You come to a locked door. you will need to find a key, try going 'e' east"
        elif inter_south == "e" or inter_south == "E":
            if fight_s_happened == False:
                fight_spider(human_hp, human_damage)
                fight_s_happened = True
                room_d()
            elif fight_s_happened == True:
                room_d()
            else:
                print "There is nothing more in the room to find."
                #intersection east

            exit(0)


        else:
            print "Please enter 's', 'e' or 'w'"

def final_fight(human_hp, human_damage):
    print human_hp, human_damage
    print "Tis a long game for me"

def room_d(human_hp, human_damage):
    print "Looking down on the carcass of the enormous spider you wonder how it"
    print "got so big. The room is filled with spider webs, Do you wish to look further"
    print "or leave room?"
    i = 0
    for i in range(10):
        room_d_choice = raw_input("-> ")
        if room_d_choice == "s" or room_d_choice == "S":
            print "Time to do some prunning, you slash away at the cobwebs"
            print "and find a golden key"
            #key = 1
            fight_giant_coffee(human_hp,human_damage)
            exit(0)
        elif room_d_choice == "l" or room_d_choice == "L":
            print "You head back out into hallway, trip over and land on your"
            print "sword, Game over!"
            exit(0)
        else:
            print "You die from bordem. Try pressing"
            print "'s' or 'l' next time, GAME OVER"
            # eastern corridor

def fight_giant_coffee(hit_points, strike):
    print "\nHeading back out the hall, you go back to the locked door"
    print "The door creaks open revelving the oddest thing you've ever seen!"
    print "Before you stands a Giant cup of Gloria Jeans coffee. "# room D
    gc_hit_points = 20
    gc_strike = random.randint(0, 6)
    attack(strike)

    print "Do you wish to fight 'f' or runaway 'r':"
    # loops while hit points of spider and human >= 0
    while (gc_hit_points >= 0 and hit_points >= 0):
        choice = raw_input("-> ")
        if choice == "f" or choice == "F":
            hit_points = (hit_points - gc_strike)
            print "The coffee spills on you for %r " % gc_strike
            print "\tYour hit points %r" % hit_points
            attack(strike)
            print "you hit the Giant coffee cup for %r" % strike
            gc_hit_points = (gc_hit_points - strike)
            print "\tGiant Coffee cup's hit points %r" % gc_hit_points

        elif choice == "r" or choice == "R":
            print "The coffee chases you down and eats you."
            print "You died, GAME OVER"
            # hallway_b()
            exit(0)
        elif choice != "f" or choice != "F" or choice != "r" or choice != "R":
            print "Please press 'f' or 'r':"
        else:
            exit(0)
    if hit_points <= 0:
        print "You Died! Back luck"
        exit(0)
    elif gc_hit_points <= 0:
        print "You slayed the Giant Coffee Cup"
        print "Your health is now %r " % hit_points
        print "          You win!          "
        print "~~~~~~~~~GAME OVER~~~~~~~~~~"
        exit(0)
    else:
        exit(0)

def fight_spider(hit_points, strike):
    print """The room smells musty and is hard to see in.  You hear a rustling in
    the room and quickly get out your sword but are shocked to see a giant spider
    the size of bear.""" # room D
    fws_hit_points = 5
    fws_strike = random.randint(0, 5)
    attack(strike)

    print "Do you wish to fight 'f' or runaway 'r':"
    # loops while hit points of spider and human >= 0
    while (fws_hit_points >= 0 and hit_points >= 0):
        choice = raw_input("-> ")
        if choice == "f" or choice == "F":
            hit_points = (hit_points - fws_strike)
            print "spider hits you for %r " % fws_strike
            print "\tYour hit points %r" % hit_points
            attack(strike)
            print "you hit the spider %r" % strike
            fws_hit_points = (fws_hit_points - strike)
            print "\tSpider hit points %r" % fws_hit_points

        elif choice == "r" or choice == "R":
            print "The spider chases you down and kills you. GAME OVER!"
            exit(0)
        elif choice != "f" or choice != "F" or choice != "r" or choice != "R":
            print "Please press 'f' or 'r':"
        else:
            exit(0)
    if hit_points <= 0:
        print "You Died! Back luck"
        exit(0)
    elif fws_hit_points <= 0:
        print "You slayed the spider"
        print "Your health is now %r " % hit_points
        key = 0
        room_d(hit_points, strike)
        exit(0)
    else:
        exit(0)



intro()
room_a()




# fight_spider(hit_points_a, weapon)
