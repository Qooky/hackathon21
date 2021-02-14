# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("")
define MC = Character("[player_name]")
define Rex = Character("Rex")
define Thunder = Character("Thunder")
define Blue = Character("Blue")
define GUBA = Character("GUBA")
define Wallace = Character("Wallace")
define Justin = Character("Justin Trudeau")


# The game starts here.

label start:
    $ player_name = ""
    $ nameEntry = False
    scene bg basic with dissolve

    N "Welcome to the world of Oh, Canada!!"

    while not nameEntry:
        $ player_name = renpy.input("What is your name?")
        N "Is your name [player_name]?"
        menu:
            "{color=#000000}Yes{/color}":
                $ nameEntry = True
            "{color=#000000}No{/color}":
                pass

    jump scene1

label scene1:
    scene bg grad with dissolve
    N "Today is a beautiful day"
    N "The sun is shining"
    N "The cherry blossoms are blooming"
    N "And [player_name] is attending her highschool graduation"

    MC "(I can't believe high school is actually over)"
    MC "(It was a lot of fun, but I'm looking forward to what comes next)"
    MC "(This time tomorrow, I'll finally be in Canada!)"
    MC "(I wonder if there will be any cute boys there)"
    MC "*sigh*"

    jump scene2

label scene2:
    scene bg black with dissolve
    N "Later that night"

    scene bg room with dissolve
    MC "I sure hope I made the right choice..."
    MC "I'll be leaving my friends and family behind"
    MC "And if I don't get accepted by any universities, I'll be forced to come back home..."
    MC "What if people aren't impressed with my maple syrup chugging and polar bear riding skills?"
    MC "Then all that time I spent practicing would go to waste :^("

    N "You glance at the clock"
    N "It's getting quite late..."

    MC "Guess there's no point in worrying now"
    MC "Better get some rest, my flight leaves early tomorrow"

    N "You take a quick swig of maple syrup before getting into bed"

    MC "goodbye Japan"

    scene bg black with dissolve
    MC "{cps=3}.....{/cps}"

    return
