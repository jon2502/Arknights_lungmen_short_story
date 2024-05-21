
label start:
    "welcome to Arknights lungmen short story"
    "all the art and characters in the game are owned by Hypergryph"
    $ povname = renpy.input("What is your name? Deafult: Lei")
    $ povname = povname.strip()
    if not povname:
        $ povname = "Lei"
    scene
    Pov "{i}well first day at work lets hope it dosent go teribly wrong{i}"
    Unkowned "come in"
    "You enter the room"
    scene Office
    show Chen5 at standart
    Chen "So you are the new recruit [povname] right?"
    Pov "yes ma'am"
    show Chen2 at standart
    hide Chen5
    Chen "Then remeber that i expect nothing but the best from you."
    Chen "Am i understod?"
    Pov "yes ma'am"
    Chen "Good then let me introduce you the others that you will be working with."
    "you follow her out the office"
    Pov "{i}{i}"
    Chen "we are here"
    hide Chen2
    show Hoshiguma4 at left
    show Swire5 at right


    #text for later
    menu:
        "stay and work":
            jump work
        "go to the bar with Hoshiguma and the others":
            jump bar
    return

label work:
    Pov "Sorry maybe another day"
    return
label bar:
    Pov "Sure I'm up for going and grabbing a few drinks"
    return
