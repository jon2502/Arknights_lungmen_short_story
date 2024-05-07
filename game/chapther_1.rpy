
label start:
    "welcome to Arknights lungmen short story"
    "all the art and characters in the game are owned by Hypergryph"
    $ povname = renpy.input("What is your name? Deafult: Lei")
    $ povname = povname.strip()
    if not povname:
        $ povname = "Lei"

    scene Office
    show chen5 at standart
    Chen "So you are the new recruit [povname] right?"
    pov "yes ma'am"
    show chen2 at standart
    Chen "Then"
    # This ends the game.

    return
