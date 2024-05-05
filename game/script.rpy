
label start:
    "welcome"
    $ povname = renpy.input("What is your name? Deafult: Lei")
    $ povname = povname.strip()
    if not povname:
        $ povname = "Lei"
    scene Office
    show Chen1 at standart
    Chen "So you are the new recruit [povname] right?"
    pov "yes ma'am"

    # This ends the game.

    return
