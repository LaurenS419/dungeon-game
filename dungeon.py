# Lauren Spee
# 261008497

ROOM_NAME = "Snowy Cabin"
AUTHOR = "Lauren Spee"
PUBLIC = True

## Functions the game will call to to save space ##
        
def cabin_surroundings():
    """ () -> NoneType
    Prints a description of the cabin
    >>> cabin_surroundings()

    You blink harder to clear you eyes, looking around. 
    There's a door that seems to have a thick lock on it.
    Along the wall opposite to the door, there seems to be 
    some sort of trapdoor in the floor.

    """
    
    print("\nYou blink harder to clear you eyes, looking around. ")
    print("There's a door that seems to have a thick lock on it.")
    print("Along the wall opposite to the door, there seems to be ")
    print("some sort of trapdoor in the floor.\n")
    
    
def trapdoor():
    """ () -> NoneType
    Prints a description of the trapdoor
    >>> trapdoor()
    
    You get up, shaking the sleep out of your limbs 
    as you go. The trap door is made of a solid wood 
    with a metal handle.
    You pull, and to your surprise it opens without 
    a hitch. A ladder descends into darkness. 
    It looks creepy, but it's your only hope.
    
    """
    
    print("\nYou get up, shaking the sleep out of your limbs ")
    print("as you go. The trap door is made of a solid wood ")
    print("with a metal handle.")
    print("You pull, and to your surprise it opens without ")
    print("a hitch. A ladder descends into darkness. ")
    print("It looks creepy, but it's your only hope.\n")
    
    
def door():
    """() -> NoneType
    Prints a description of the door.
    >>> door()
    
    The door appears to be locked with a very thick 
    metal padlock. If only you could find the key..
    
    """
    print("\nThe door appears to be locked with a very thick ")
    print("metal padlock. If only you could find the key..\n")

def descend_ladder():
    """() -> NoneType
    Prints a description of descending the ladder and the
    room the user ends up in.
    >>> descend_ladder()
    
    You descend downwards, the dark pressing in on you 
    in ways you can't explain. You don't want to spend 
    long down here. You get to the bottom and it seems 
    bright and you almost feel.. warm? Then you blink 
    and it's gone. It's a cramped room with an old 
    book on a desk. Squeaks sounding from the corner 
    distract you.
    
    """
    
    print("\nYou descend downwards, the dark pressing in on you ")
    print("in ways you can't explain. You don't want to spend ")
    print("long down here. You get to the bottom and it seems ")
    print("bright and you almost feel.. warm? Then you blink ")
    print("and it's gone. It's a cramped room with an old ")
    print("book on a desk. Squeaks sounding from the corner ")
    print("distract you.\n")
    
def squeaks():
    """() -> str
    Prints the user finding a rat and naming it, returns the
    name of the rat
    >>> squeaks()
    
    You peer into the darkness and there seems to be.. a rat?
    Something about it seems overwhelmingly friendly. 
    Against your better judegment, you put your hand 
    out. It steps slowly onto your hand, big eyes 
    staring into yours. Cute.
    It seems you've made a friend, you smile at it 
    and it seems to smile back.

    What do you name your new friend? Max

    Your name is Max you tell it. 
    It squeaks happily and scurries up to rest on your 
    shoulder. It makes you feel safe. Like its warmth 
    protects you from the darkness. 
    Regardless, you should get out of here.

    'Max'
    >>> squeaks()
    
    You peer into the darkness and there seems to be.. a rat?
    Something about it seems overwhelmingly friendly. 
    Against your better judegment, you put your hand 
    out. It steps slowly onto your hand, big eyes 
    staring into yours. Cute.
    It seems you've made a friend, you smile at it 
    and it seems to smile back.

    What do you name your new friend? fluffy

    Your name is fluffy you tell it. 
    It squeaks happily and scurries up to rest on your 
    shoulder. It makes you feel safe. Like its warmth 
    protects you from the darkness. 
    Regardless, you should get out of here.

    'fluffy'
    >>> squeaks()
    
    You peer into the darkness and there seems to be.. a rat?
    Something about it seems overwhelmingly friendly. 
    Against your better judegment, you put your hand 
    out. It steps slowly onto your hand, big eyes 
    staring into yours. Cute.
    It seems you've made a friend, you smile at it 
    and it seems to smile back.

    What do you name your new friend? ELEPHANT7

    Your name is ELEPHANT7 you tell it. 
    It squeaks happily and scurries up to rest on your 
    shoulder. It makes you feel safe. Like its warmth 
    protects you from the darkness. 
    Regardless, you should get out of here.

    'ELEPHANT7'
    
    """
    
    print("\nYou peer into the darkness and there seems to be.. a rat?")
    print("Something about it seems overwhelmingly friendly. ")
    print("Against your better judegment, you put your hand ")
    print("out. It steps slowly onto your hand, big eyes ")
    print("staring into yours. Cute.")
    print("It seems you've made a friend, you smile at it ")
    print("and it seems to smile back.\n")
    
    rat_name = input("What do you name your new friend? ")
    
    print("\nYour name is " + rat_name + " you tell it. ")
    print("It squeaks happily and scurries up to rest on your ")
    print("shoulder. It makes you feel safe. Like its warmth ")
    print("protects you from the darkness. ")
    print("Regardless, you should get out of here.\n")
    
    return rat_name
    
    
def book():
    """() -> bool
    Prints a description of the book. Returns true,
    indicating that the key word has been found
    >>> book()
    
    You open the book, flipping through old pages 
    randomly. There's be thick, dark ink 
    scrawled in a language you don't understand.
    You stop on a page and one word seems to stand 
    out. Howl. You don't know what it means in the 
    context of the book, but it has something to do 
    with the door, you can feel it.
    The pressing need to leave comes back and panic 
    grips your heart. Get out.

    True

    """
    
    print("\nYou open the book, flipping through old pages ")
    print("randomly. There's be thick, dark ink ")
    print("scrawled in a language you don't understand.")
    print("You stop on a page and one word seems to stand ")
    print("out. Howl. You don't know what it means in the ")
    print("context of the book, but it has something to do ")
    print("with the door, you can feel it.")
    print("The pressing need to leave comes back and panic ")
    print("grips your heart. Get out.\n")
    
    return True


def ascend_ladder():
    """() -> NoneType
    Prints a description of what happens after the user
    ascends the ladder
    >>> ascend_ladder()

    You climb up as fast as you can, a breath of relief 
    entering your lungs when the light from the fire 
    reaches your body.
    You run over to door with lock, gripping it in your 
    hand. It doesn't have a keyhole. Just the same 
    scrawled runes carves into the metal.

    """
    
    print("\nYou climb up as fast as you can, a breath of relief ")
    print("entering your lungs when the light from the fire ")
    print("reaches your body.")
    print("You run over to door with lock, gripping it in your ")
    print("hand. It doesn't have a keyhole. Just the same ")
    print("scrawled runes carves into the metal.\n")  

def leave(rat_name, found_word):
    """ (str, bool) -> NoneType
    Uses the str rat_name and uses it in the victory message
    if the rat was found and named, also uses the boolean
    found_word to see if the user can escape yet
    >>> leave('Tracer', True)

    Whatever you did to the lock seems to work.
    You and your friend Tracer stumble 
    into the white light, wind whipping harshly 
    around you. You pray you'll find another human 
    before the deathly cold claims you.
    >>> leave('Viktor', False)
    'invalid attempt'
    >>> leave("None", True)

    Whatever you did to the lock seems to work.
    You stumble into the white light, wind whipping harshly 
    around you. You pray you'll find another human 
    before the deathly cold claims you.
    """
    
    if found_word == False:
        return "invalid attempt"
    
    if rat_name == "None":
        print("\nWhatever you did to the lock seems to work.")
        print("You stumble ", end = "")
        print("into the white light, wind whipping harshly ")
        print("around you. You pray you'll find another human ")
        print("before the deathly cold claims you.")
    
    else:
        print("\nWhatever you did to the lock seems to work.")
        print("You and your friend " + rat_name + " stumble ")
        print("into the white light, wind whipping harshly ")
        print("around you. You pray you'll find another human ")
        print("before the deathly cold claims you.")
        
def list_commands(counter, found_word):
    """ (int, bool) -> NoneType
    Based on the counter (tells what stage the user is at) and
    a boolean found_word telling if the user found the key
    word yet, prints the commands
    >>> list_commands(2, False)
    examine surroundings
    examine door
    examine trapdoor
    >>> list_commands(4, True)
    examine surroundings
    examine door
    examine trapdoor
    descend ladder
    examine squeak
    examine book
    >>> list_commands(6, True)
    examine surroundings
    examine door
    examine trapdoor
    descend ladder
    examine squeak
    examine book
    ascend ladder
    pull on the lock
    say howl into the lock
    sit down
    bark like a dog
    """
    
    if counter < 1:
        print("none")
        
    if counter >= 1:
        print("examine surroundings")
        
    if counter >= 2:
        print("examine door")
        print("examine trapdoor")
        
    if counter >= 3:
        print("descend ladder")
        
    if counter >= 4:
        print("examine squeak")
        print("examine book")
       
    if counter >= 5:   
        print("ascend ladder") 
     
    if counter >= 6:
        
        if found_word == True:
            print("pull on the lock")
            print("say howl into the lock")
            print("sit down")
            print("bark like a dog")
    
## Main Game Function ##
    
def escape_room():
    """ () -> NoneType
    When called, runs an escape room text-based game
    >>> escape_room()
    You come to, blinking slowly at the roaring fire in 
    front of you. Where am I?

    You blink hard, taking in your surroundings. 
    You can hear two things: the fire crackling and popping, 
    and the wind howling outside. If you think 
    too hard it sounds like it's saying something. You 
    don't think too hard about it.

    You seem to be in some sort of rustic wood cabin, 
    though the whole place has been stripped aside from 
    the fire place and surprisingly comfy white rug you lay on.
 
    What do you do? list commands
    examine surroundings
    What do you do? examine my surroundings

    You blink harder to clear you eyes, looking around. 
    There's a door that seems to have a thick lock on it.
    Along the wall opposite to the door, there seems to be 
    some sort of trapdoor in the floor.

    What do you do? examine trapdoor

    You get up, shaking the sleep out of your limbs 
    as you go. The trap door is made of a solid wood 
    with a metal handle.
    You pull, and to your surprise it opens without 
    a hitch. A ladder descends into darkness. 
    It looks creepy, but it's your only hope.

    What do you do? list commands
    examine surroundings
    examine door
    examine trapdoor
    descend ladder
    What do you do? go down ladder

    You descend downwards, the dark pressing in on you 
    in ways you can't explain. You don't want to spend 
    long down here. You get to the bottom and it seems 
    bright and you almost feel.. warm? Then you blink 
    and it's gone. It's a cramped room with an old 
    book on a desk. Squeaks sounding from the corner 
    distract you.

    What do you do? examine squeaks

    You peer into the darkness and there seems to be.. a rat?
    Something about it seems overwhelmingly friendly. 
    Against your better judegment, you put your hand 
    out. It steps slowly onto your hand, big eyes 
    staring into yours. Cute.
    It seems you've made a friend, you smile at it 
    and it seems to smile back.

    What do you name your new friend? Rat

    Your name is Rat you tell it. 
    It squeaks happily and scurries up to rest on your 
    shoulder. It makes you feel safe. Like its warmth 
    protects you from the darkness. 
    Regardless, you should get out of here.

    What do you do? list commands
    examine surroundings
    examine door
    examine trapdoor
    descend ladder
    examine squeak
    examine book
    What do you do? examine book

    You open the book, flipping through old pages 
    randomly. There's be thick, dark ink 
    scrawled in a language you don't understand.
    You stop on a page and one word seems to stand 
    out. Howl. You don't know what it means in the 
    context of the book, but it has something to do 
    with the door, you can feel it.
    The pressing need to leave comes back and panic 
    grips your heart. Get out.

    What do you do? go up ladder

    You climb up as fast as you can, a breath of relief 
    entering your lungs when the light from the fire 
    reaches your body.
    You run over to door with lock, gripping it in your 
    hand. It doesn't have a keyhole. Just the same 
    scrawled runes carves into the metal.

    What do you do? list commands
    examine surroundings
    examine door
    examine trapdoor
    descend ladder
    examine squeak
    examine book
    ascend ladder
    pull on the lock
    say howl into the lock
    sit down
    bark like a dog
    What do you do? sit down

    It doesn't work, maybe look at the command list.

    What do you do? i say howl

    Whatever you did to the lock seems to work.
    You and your friend Rat stumble 
    into the white light, wind whipping harshly 
    around you. You pray you'll find another human 
    before the deathly cold claims you. 
    >>> escape_room()
    You come to, blinking slowly at the roaring fire in 
    front of you. Where am I?

    You blink hard, taking in your surroundings. 
    You can hear two things: the fire crackling and popping, 
    and the wind howling outside. If you think 
    too hard it sounds like it's saying something. You 
    don't think too hard about it.

    You seem to be in some sort of rustic wood cabin, 
    though the whole place has been stripped aside from 
    the fire place and surprisingly comfy white rug you lay on.
 
    What do you do? look at my surroundings

    You blink harder to clear you eyes, looking around. 
    There's a door that seems to have a thick lock on it.
    Along the wall opposite to the door, there seems to be 
    some sort of trapdoor in the floor.

    What do you do? examine the door

    The door appears to be locked with a very thick 
    metal padlock. If only you could find the key..

    What do you do? list commands
    examine surroundings
    examine door
    examine trapdoor
    What do you do? examine trapdoor

    You get up, shaking the sleep out of your limbs 
    as you go. The trap door is made of a solid wood 
    with a metal handle.
    You pull, and to your surprise it opens without 
    a hitch. A ladder descends into darkness. 
    It looks creepy, but it's your only hope.

    What do you do? descend ladder

    You descend downwards, the dark pressing in on you 
    in ways you can't explain. You don't want to spend 
    long down here. You get to the bottom and it seems 
    bright and you almost feel.. warm? Then you blink 
    and it's gone. It's a cramped room with an old 
    book on a desk. Squeaks sounding from the corner 
    distract you.

    What do you do? examine book

    You open the book, flipping through old pages 
    randomly. There's be thick, dark ink 
    scrawled in a language you don't understand.
    You stop on a page and one word seems to stand 
    out. Howl. You don't know what it means in the 
    context of the book, but it has something to do 
    with the door, you can feel it.
    The pressing need to leave comes back and panic 
    grips your heart. Get out.

    What do you do? ascend ladder

    You climb up as fast as you can, a breath of relief 
    entering your lungs when the light from the fire 
    reaches your body.
    You run over to door with lock, gripping it in your 
    hand. It doesn't have a keyhole. Just the same 
    scrawled runes carves into the metal.

    What do you do? list commands
    examine surroundings
    examine door
    examine trapdoor
    descend ladder
    examine squeak
    examine book
    ascend ladder
    pull on the lock
    say howl into the lock
    sit down
    bark like a dog
    What do you do? say howl

    Whatever you did to the lock seems to work.
    You stumble into the white light, wind whipping harshly 
    around you. You pray you'll find another human 
    before the deathly cold claims you.
    >>> escape_room()
    You come to, blinking slowly at the roaring fire in 
    front of you. Where am I?

    You blink hard, taking in your surroundings. 
    You can hear two things: the fire crackling and popping, 
    and the wind howling outside. If you think 
    too hard it sounds like it's saying something. You 
    don't think too hard about it.

    You seem to be in some sort of rustic wood cabin, 
    though the whole place has been stripped aside from 
    the fire place and surprisingly comfy white rug you lay on.
     
    What do you do? look around

    You feel like you should look at your surroundings and get out of here..something about the shadows don't look friendly.

    What do you do? look at surroundings

    You blink harder to clear you eyes, looking around. 
    There's a door that seems to have a thick lock on it.
    Along the wall opposite to the door, there seems to be 
    some sort of trapdoor in the floor.

    What do you do? go to trapdoor

    You get up, shaking the sleep out of your limbs 
    as you go. The trap door is made of a solid wood 
    with a metal handle.
    You pull, and to your surprise it opens without 
    a hitch. A ladder descends into darkness. 
    It looks creepy, but it's your only hope.

    What do you do? list commands
    examine surroundings
    examine door
    examine trapdoor
    descend ladder
    What do you do? go down ladder

    You descend downwards, the dark pressing in on you 
    in ways you can't explain. You don't want to spend 
    long down here. You get to the bottom and it seems 
    bright and you almost feel.. warm? Then you blink 
    and it's gone. It's a cramped room with an old 
    book on a desk. Squeaks sounding from the corner 
    distract you.

    What do you do? go towards squeaks

    You peer into the darkness and there seems to be.. a rat?
    Something about it seems overwhelmingly friendly. 
    Against your better judegment, you put your hand 
    out. It steps slowly onto your hand, big eyes 
    staring into yours. Cute.
    It seems you've made a friend, you smile at it 
    and it seems to smile back.

    What do you name your new friend? my boy

    Your name is my boy you tell it. 
    It squeaks happily and scurries up to rest on your 
    shoulder. It makes you feel safe. Like its warmth 
    protects you from the darkness. 
    Regardless, you should get out of here.

    What do you do? look at the book

    You open the book, flipping through old pages 
    randomly. There's be thick, dark ink 
    scrawled in a language you don't understand.
    You stop on a page and one word seems to stand 
    out. Howl. You don't know what it means in the 
    context of the book, but it has something to do 
    with the door, you can feel it.
    The pressing need to leave comes back and panic 
    grips your heart. Get out.

        What do you do? list commands
    examine surroundings
    examine door
    examine trapdoor
    descend ladder
    examine squeak
    examine book
    ascend ladder
    What do you do? go up ladder

    You climb up as fast as you can, a breath of relief 
    entering your lungs when the light from the fire 
    reaches your body.
    You run over to door with lock, gripping it in your 
    hand. It doesn't have a keyhole. Just the same 
    scrawled runes carves into the metal.

    What do you do? cry

    It doesn't work, maybe look at the command list.

    What do you do? scream

    It doesn't work, maybe look at the command list.

    What do you do? sit down

    It doesn't work, maybe look at the command list.

    What do you do? ask my boy for help

    It doesn't work, maybe look at the command list.

    What do you do? list commands
    examine surroundings
    examine door
    examine trapdoor
    descend ladder
    examine squeak
    examine book
    ascend ladder
    pull on the lock
    say howl into the lock
    sit down
    bark like a dog
    What do you do? howl into it

    Whatever you did to the lock seems to work.
    You and your friend my boy stumble 
    into the white light, wind whipping harshly 
    around you. You pray you'll find another human 
    before the deathly cold claims you.
    _
    """
    
    rat_name = "None"
    found_word = False
    counter = 0
    
    # Intro #
    
    print("You come to, blinking slowly at the roaring fire in ")
    print("front of you. Where am I?\n")
    
    print("You blink hard, taking in your surroundings. ")
    print("You can hear two things: the fire crackling and popping, ")
    print("and the wind howling outside. If you think ")
    print("too hard it sounds like it's saying something. You ")
    print("don't think too hard about it.\n")
    
    print("You seem to be in some sort of rustic wood cabin, ")
    print("though the whole place has been stripped aside from ")
    print("the fire place and surprisingly comfy white rug you lay on.\n ")
    
    # Choices #
    
    counter += 1
    look_cabin_surroundings = ""
    
    while look_cabin_surroundings.find("surroundings") < 0:
        look_cabin_surroundings = input("What do you do? ")
        look_cabin_surroundings = look_cabin_surroundings.lower()
        
        if look_cabin_surroundings.find("commands") >= 0:
            list_commands(counter, found_word)
            
        elif look_cabin_surroundings.find("surroundings") < 0:
            print("\nYou feel like you should look at your surroundings and get out of here..", end = "")
            print("something about the shadows don't look friendly.\n")

    
    cabin_surroundings()
    
    counter += 1
    door_or_trap = ""
    
    while door_or_trap.find("trapdoor") < 0:
        door_or_trap = input("What do you do? ")
        door_or_trap = door_or_trap.lower()
    
        if door_or_trap.find("commands") >= 0:
            list_commands(counter, found_word)
    
        elif door_or_trap.find("trapdoor") >= 0:
            trapdoor()
        
        elif door_or_trap.find("door") >= 0:
            door()
            
        else:
            print("\nYou feel like you need to do something to get out")
            print("of here.\n")
    
    counter += 1
    yes_descend_ladder = ""
    
    while yes_descend_ladder.find("ladder") < 0:
        yes_descend_ladder = input("What do you do? ")
        yes_descend_ladder = yes_descend_ladder.lower()
        
        if yes_descend_ladder.find("commands") >= 0:
            list_commands(counter, found_word)
        
        elif yes_descend_ladder.find("ladder") < 0:
            print("\nEven though it's scary, you feel like you need")
            print("to go down there. It's your only hope.\n")
    
    descend_ladder()
    
    counter += 1
    squeaks_or_book = ""
    
    while squeaks_or_book.find("book") < 0:
        squeaks_or_book = input("What do you do? ")
        squeaks_or_book = squeaks_or_book.lower()
    
        if squeaks_or_book.find("commands") >= 0:
            list_commands(counter, found_word)
    
        elif squeaks_or_book.find("book") >= 0:
            found_word = book()
        
        elif squeaks_or_book.find("squeak") >= 0:
            rat_name = squeaks()
        
        else:
            print("\nThe dark particularily in the corners of ")
            print("the room seem to writhe and pulse. You ")
            print("really need to get out of here.\n")
    
    counter += 1
    yes_ascend_ladder = ""
    
    while yes_ascend_ladder.find("ladder") < 0:
        yes_ascend_ladder = input("What do you do? ")
        yes_ascend_ladder = yes_ascend_ladder.lower()
        
        if yes_ascend_ladder.find("commands") >= 0:
            list_commands(counter, found_word)
        
        elif yes_ascend_ladder.find("ladder") < 0:
            print("\nYou swear the dark is creeping up on you, ")
            print("there's something seriously off about this ")
            print("room. You need to get out before the darkness ")
            print("drags you under, and god knows what happens. ")
            print("You'll be safer battling the cold outside than ")
            print("the slow onset of the dark.\n")
        
    ascend_ladder()
    
    counter += 1
    lock_attempts = ""
    
    while lock_attempts.find("howl") < 0:
        lock_attempts = input("What do you do? ")
        lock_attempts = lock_attempts.lower()
        
        if lock_attempts.find("commands") >= 0:
            list_commands(counter, found_word)
            
        elif lock_attempts.find("howl") < 0:
            print("\nIt doesn't work, maybe look at the command list.\n")

    leave(rat_name, found_word)
        
    
    
    
        
    