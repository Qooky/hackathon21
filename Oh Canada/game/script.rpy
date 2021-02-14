# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("")
define MC = Character("[player_name]")
define Rex = Character("Rex", color="#f21823")
define Thunder = Character("Thunder", color="#1d35ed")
define Blue = Character("Blue", color="#a625d9")
define GUBA = Character("GUBA", color="#2c911f")
define Wallace = Character("Wallace", color="#e8bd23")
define Justin = Character("Justin Trudeau")
define A = Character("Flight Attendant")
define L = Character("Librarian")
define Mystery = Character("???")
define Dean = Character("The Dean")
define C = Character("Cashier")
define V1 = Character("First Voice")
define V2 = Character("Second Voice")
define USDJ = Character("Ultra Sugoi Dream Justin", color="#f766f0")

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
    N "[[Today is a beautiful day]"
    N "[[The sun is shining]"
    N "[[The cherry blossoms are blooming]"
    N "[[And [player_name] is attending her highschool graduation]"

    MC "(I can't believe high school is actually over)"
    MC "(It was a lot of fun, but I'm looking forward to what comes next)"
    MC "(This time tomorrow, I'll finally be in Canada!)"
    MC "(I wonder if there will be any cute boys there)"
    MC "*sigh*"

    jump scene2

label scene2:
    scene bg black with dissolve
    N "[[Later that night]"

    scene bg room with dissolve
    MC "I sure hope I made the right choice..."
    MC "I'll be leaving my friends and family behind"
    MC "And if I don't get accepted by any universities, I'll be forced to come back home..."
    MC "What if people aren't impressed with my maple syrup chugging and polar bear riding skills?"
    MC "Then all that time I spent practicing would go to waste :^("

    N "[[You glance at the clock]"
    N "[[It's getting quite late...]"

    MC "Guess there's no point in worrying now"
    MC "Better get some rest, my flight leaves early tomorrow"

    N "[[You take a quick swig of maple syrup before getting into bed]"

    MC "goodbye Japan"

    scene bg black with dissolve
    MC "{cps=3}.....{/cps}"

    jump scene3

label scene3:
    N "[[The next day]"
    scene bg plane with dissolve
    A "Welcome ma'am. Please take a seat."
    A "the prime minister has the prepared a special video to welcome you to the country!"

    MC "Really!? Thank you so much!"
    MC "(The prime minister? That's so cool!)"

    scene bg black with Dissolve(1.0)

    pause 0.5

    scene bg video with dissolve

    pause 0.5

    $ renpy.movie_cutscene("animations/OC Justin Trudeau.webm")

    pause 0.5

    scene bg plane with Dissolve(1.0)

    MC "(Wow! I can't believe the {b}real Justin Trudeau{/b} made a video for us!)"
    MC "(Wait... did he say 'see you there'?)"

    scene bg black with dissolve

    jump scene4

label scene4:
    scene bg school with dissolve

    MC "I'm actually here. My first day at the university of Canada"
    MC "I wonder what kinds of people I'll meet- hmm?"
    MC "Who's that over that?"

    show justin hello with dissolve

    Justin "Bonjour et bienvenue au Canada. Hello and welcome to Canada!"

    MC "..."

    Justin "Enjoy your stay in Canada [player_name]! Profitez de votre séjour au Canada [player_name]! Au revoir!"

    hide justin hello with dissolve

    MC "(What was that?)"
    MC "(How did he know my name??)"
    MC "(Does he know I can't understand french???)"
    MC "(Oh well, let's try to get the lay of the land)"

    jump scene5

label scene5:
    scene bg hall with dissolve
    MC "Where should I go now?"
    menu:
        "{color=#000000}Library{/color}":
            MC "I should pick up my books from the library"
            jump scene6
        "{color=#000000}Tim Hortons{/color}":
            MC "I guess a coffee would be nice"
            jump scene7
        "{color=#000000}Canadian Studies Classroom{/color}":
            MC "Oh no! I forgot I have a class right now! I gotta get there fast"
            jump scene8
        "{color=#000000}Computer Lab{/color}":
            MC "I wonder what the labs are like"
            jump scene9
        "{color=#000000}Dorm{/color}":
            MC "Maybe I should get some rest"
            jump scene10

label scene6:
    scene bg library with dissolve
    N "[[You walk into the library and take a look around]"
    N "[[Taking a look around, you see several students studying, the librarians counter, and...]"
    MC "(Is he looking at me?)"

    show wallace neutral with dissolve
    Mystery "..."

    MC "..."
    hide wallace neutral with dissolve
    MC "(Nah I'm probably imagining things. I'll go ask at the counter about my books)"

    N "[[You walk over to the counter with a kindly looking old lady behind it]"

    MC "Hello, do you have the reservations for [player_name] ready?"

    L "[player_name]? Ah yes, here you are"

    MC "Thank you very much!"

    N "[[You take your large stack of books for the semester and make your way out the door]"

    scene bg black
    N "*THUD*"

    MC "Ouch... what just happened?"

    scene bg library with Dissolve(1.0)
    show wallace neutral with Dissolve(1.0)

    N "[[The stranger is staring at you intently]"

    MC "..."
    Mystery "..."

    menu:
        "{color=#000000}Can I help you with something?{/color}":
            jump scene6_1
        "{color=#000000}(Say nothing){/color}":
            jump scene6_2
        "{color=#000000}What's wrong with you >:^({/color}":
            jump scene6_3

label scene6_1:
    MC "Can I help you with something?"

    Mystery "Oh- I, uh..."
    Mystery "I was just thinking that I hadn't seen you before and um-"
    Mystery "Well... I... Do you..."
    Mystery "{cps=69}Do you know anything about linear algebra?{/cps}"

    MC "Well..."
    menu:
        "{color=#000000}I do, and I hate it{/color}":
            jump scene6_1_1
        "{color=#000000}Not really{/color}":
            jump scene6_1_2
        "{color=#000000}I know everything{/color}":
            jump scene6_1_3

label scene6_1_1:
    MC "The only thing I know about Linear Algebra is that I hate it with every fibre of my being"
    MC "You merely bringing it up has made me regret this entire trip"
    MC "I really thought things would be different here"

    Mystery "I-"

    MC "{b}Don't.{/b}"
    MC "I'm leaving"

    hide wallace neutral with dissolve

    scene bg black with dissolve

    N "[[And so, [player_name] returned home at the mere mention of linear algebra]"
    N "[[BAD END]"
    N "Continue?"
    menu:
        "{color=#000000}Yes (From Library){/color}":
            jump scene6
        "{color=#000000}Yes (From Hallway){/color}":
            jump scene5
        "{color=#000000}No{/color}":
            jump end

label scene6_1_2:
    MC "Not really, no"

    Mystery "Oh... uh... alright..."

    MC "Sorry"

    Mystery "N-No problem."

    MC "..."

    Mystery "..."

    hide wallace neutral with Dissolve(1.0)

    N "[[The stranger left]"

    MC "(Kinda glad that's over with)"

    scene bg black with dissolve
    jump scene5

label scene6_1_3:
    MC "You may as well call me David Hestenes (The pioneer of modern Linear Algebra) Because I know everything about it"
    MC "I was multiplying matrices in kindergarten"
    MC "I was diagonalizing in daycare"
    MC "I was... well you get the point"
    MC "My name is [player_name], nice to meet you :^)"

    Mystery "Y-yeah nice to meet you too"

    N "[[He seems to have calmed down a bit]"

    Mystery "My name is Wallace"
    Wallace "Would you like to study with me [player_name]?"

    MC "Sure, that sounds great :^)"

    scene bg black with Dissolve(1.0)

    N "[[Wallace and [player_name] would go on to have a very stable and studious relationship]"
    N "[[GOOD END]"
    N "This is where the demo ends for this route. Would you like to see the other routes?"
    menu:
        "{color=#000000}Yes (Go to Hallway){/color}":
            jump scene5
        "{color=#000000}Yes (From Library){/color}":
            jump scene6
        "{color=#000000}No thanks{/color}":
            jump end

label scene6_2:
    MC "..."

    Mystery "..."

    hide wallace neutral with Dissolve(1.0)

    N "[[The stranger left]"

    MC "(What a weirdo)"

    scene bg black with dissolve
    jump scene5

label scene6_3:
    MC "HEY! What's wrong with you! Can't you watch where you're going?"

    Mystery "I... uh..."
    Mystery "sorry."

    hide wallace neutral with dissolve

    N "[[The stranger ran out in a hurry]"
    N "[[You hear a new, much deeper voice coming from behind you]"

    Mystery "Young lady"

    N "[[You turn, and to your horror you see...]"

    Dean "Hasn't anyone ever told you to be quiet in a library?"
    Dean "I'm afraid we have a zero tolerance policy in this establishment"
    Dean "I'll have to expel you"

    MC "But I-"

    Dean "I won't hear it."
    Dean "Farewell"

    scene bg black with dissolve
    N "[[And so, [player_name] was deported for yelling in the library]"
    N "[[BAD END]"
    N "Continue?"
    menu:
        "{color=#000000}Yes (From Library){/color}":
            jump scene6
        "{color=#000000}Yes (From Hallway){/color}":
            jump scene5
        "{color=#000000}No{/color}":
            jump end

label scene7:
    scene bg tims with dissolve

    N "[[you have no issue finding the nearest Tim Hortons]"
    N "[[Surprisingly, the line is quite small]"
    N "[[In fact, the line would be empty if not for...]"

    show blue neutral with dissolve

    Mystery "Can I get a double-double?"
    Mystery "Actually, make that 2 double-doubles, I'm running a little slow today"

    MC "(I've never seen someone with clothes like that before...)"

    N "[[The man turns around to meet your gaze]"

    Mystery "Can I help you with something?"

    MC "Oh, um, sorry for staring..."

    Mystery "Come on, out with it. What did you wanna ask?"

    menu:
        "{color=#000000}What's a double-double?{/color}":
            jump scene7_1
        "{color=#000000}(Stay quiet){/color}":
            jump scene7_2

label scene7_1:
    Mystery "A double-double is coffee with 2 creams and 2 sugar- are you new here?"

    MC "Yeah actually, I just got here yesterday"

    Mystery "Name?"

    MC "Sorry?"

    Mystery "No you're not, I just asked your name"

    MC "Oh, my name is [player_name]"

    Mystery "I'm Blue, nice to meet you"
    Blue "Now I have places to be [player_name], but I've taken a liking to you"
    Blue "Here's my number, maybe I can show you around the city sometime."
    N "[[Blue pulls a business card out of his front pocket and holds it out to you]"

    menu:
        "{color=#000000}Yeah! I think I'd like that{/color}":
            jump scene7_1_1
        "{color=#000000}No thanks! I'm good{/color}":
            jump scene7_1_2

label scene7_1_1:
    Blue "Great. See you soon."

    hide blue neutral with dissolve

    N "[[Blue walks away with purpose]"

    MC "(I'll have to call him when I have some free time)"

    scene bg black with Dissolve(1.0)
    N "[[Several days later, Blue took you out for a night on the town]"
    N "[[Perhaps this is the start of something more?]"
    N "[[GOOD END]"
    N "This is where the demo ends for this route. Would you like to see the other routes?"
    menu:
        "{color=#000000}Yes (Go to Hallway){/color}":
            jump scene5
        "{color=#000000}Yes (From Tim Hortons){/color}":
            jump scene7
        "{color=#000000}No thanks{/color}":
            jump end


label scene7_1_2:
    Blue "*tch* Fine, fine. Your loss I suppose."

    N "[[He puts the card back in it's pocket and picks up his drinks, leaving in a hurry]"

    hide blue neutral with dissolve

    MC "(What a creep)"

    N "[[You order your coffee and head out]"

    jump scene5


label scene7_2:
    Mystery "A little slow are we?"
    Mystery "My name's Blue, try not to get in my way"

    N "[[Blue glares at the cashier behind the counter taking his leave, a coffee in each hand]"

    hide blue neutral with dissolve

    MC "(Geez, that guy has a short fuse)"

    C "I can help you over here miss"

    MC "Oh, thank you. Could I have a medium coffee and a plain donut please"

    C "Certainly, that'll be $3.89"

    N "[[You finish your transaction and walk away with your coffee and treat]"

    scene bg hall with dissolve

    MC "(Wow this donut is great!)"

    N "[[You go to take another bite{w} but this time{w} something isn't right]"

    MC "!!"

    N "[[As your vision begins to fade you see people rushing to your aid]"
    N "[[As well as a familiar face passing you by]"

    C "..."

    scene bg black with Dissolve(1.0)
    pause (1.0)
    N "[[You wake up in a hospital bed, alive and well]"
    N "[[Apparently you had consumed a non-lethal poison that put you out of comission for five months]"
    N "[[It may not have hurt you, but it did put you out long enough for your chance at the University of Canada to slip by]"
    N "[[Who could've done this? And why?]"
    N "[[Whatever the answers to these questions are, you'll never know them, as you're on a flight back a week later]"
    N "[[BAD END]"
    N "Continue?"
    menu:
        "{color=#000000}Yes (From Tim Hortons){/color}":
            jump scene7
        "{color=#000000}Yes (From Hallway){/color}":
            jump scene5
        "{color=#000000}No{/color}":
            jump end

label scene8:
    scene bg classroom with dissolve
    N "[[You creep into class just in time]"

    MC "(I should make sure I'm in the right place, I'll ask that boy over there)"

    show thunder neutral with dissolve
    MC "Um, excuse me. This is room #032 right?"

    Mystery "Yeah, Canadian Studies 201. Class is just about to start."

    MC "*phew, that's a relief. Is this seat taken?"

    Mystery "Nope, go ahead."

    N "[[You take a seat next to the boy]"

    MC "Thank you. My name is [player_name] by the way"

    Mystery "I'm Thunder Columbia. You can call me Thunder."

    MC "Nice to meet you!"

    Thunder "Nice to meet you too!"

    hide thunder neutral with dissolve
    scene bg black with dissolve

    N "[[The professor came and started the lecture]"
    N "[[He talks about a semester long project where you're allowed to work with a partner...]"

    N "[[After the lecture]"

    scene bg classroom with dissolve
    show thunder neutral with dissolve


    Thunder "Say, [player_name], would you by any chance like to partner up for the project?"

    Thunder "It's always nice to have help. And even if we brick it, we'll still meet a new person right?"

    menu:
        "{color=#000000}Yeah! I'm down.{/color}":
            jump scene8_1
        "{color=#000000}Sorry, I prefer working on these projects alone{/color}":
            jump scene8_2

label scene8_1:
    Thunder "Great! Here's my number so we can keep in touch"
    Thunder "My schedule is PACKED, so I gotta get going"
    Thunder "Don't be a stranger hey?"
    Thunder "See you around :^)"

    hide thunder neutral with dissolve

    MC "(He seems really nice, I hope our project goes well)"

    scene bg black with dissolve

    N "[[Thunder ad [player_name] would spend much of the coming months together, working and talking]"
    N "[[Towards the end of the semester, they started dating.]"
    N "[[After graduation, the two got married and had a long and fruitful life together]"
    N "[[GOOD END]"
    N "This is where the demo ends for this route. Would you like to see the other routes?"
    menu:
        "{color=#000000}Yes (Go to Hallway){/color}":
            jump scene5
        "{color=#000000}Yes (From The Start of Class){/color}":
            jump scene8
        "{color=#000000}No thanks{/color}":
            jump end

label scene8_2:
    Thunder "Oh, no worries. I totally get you"
    Thunder "Sometimes these things are better taken on alone yeah?"
    Thunder "Well at any rate, if you ever change your mind, or if you just wanna talk, I'll be around"
    Thunder "Have a good one [player_name]"

    hide thunder neutral with dissolve

    MC "(I hope he wasn't offended...)"
    MC "(No, he seemed okay)"
    MC "(I'll clean up my notes then head out)"

    jump scene5


label scene9:
scene bg black with dissolve
N "[[As you approach the door to the computer labs, you hear two voices yelling at each other]"

V1 "No way man, It's way too crowded and noisy. How are you supposed to get to know each other when you're surrounded by noisy kids?"

V2 "tch, you just don't get it. It's the largest mall in North America. You can do {i}everything{/i} there. So much better than some dinky cowboy show"

V1 "What did you just say?!"

V2 "You heard me. No girl would want to hang out at your honky tonk sorry excuse for a festival"

V1 "Oh that is IT"

scene bg lab with dissolve
show rex neutral at right
show guba right at left
N "[[You walk in just as the boy in red seemed to be lunging towards the boy in green]"
N "[[When they hear you come in, they both turn to see you]"
N "[[The boy in red backs down sheepishly]"

V1 "You got lucky GUBA..."

GUBA "Whatever you say rex"

N "[[An awkward silence fills the air while you take a look around]"
N "[[The two boys do everything they can to avoid your, and each others, gaze]"
N "[[After a while, the boy in red addresses you"

Rex "Say... you're a girl, right?"

GUBA "What a smooth opener"

Rex "Shut up GUBA"

MC "I am, yeah"

Rex "Perfect, would you mind settling an argument for us?"

GUBA "Oh come on..."

MC "Sure I suppose"

Rex "Okay so..."
Rex "Where would you rather go on a first date with a guy?"
Rex "The Stampede, or {color=#32663c}{i}wEsT eDmOnToN mAlL{/i}{/color}"
menu:
    "{color=#000000}Stampede sounds fun{/color}":
        jump scene9_1
    "{color=#000000}Definitely West Ed Mall{/color}":
        jump scene9_2

label scene9_1:
    Rex "YES"

    GUBA "Yeah whatever. Your victory is hollow until you prove it with a real date {i}dweeb{/i}"

    Rex "Fine! You know what, hey you uh... sorry... what was your name again?"

    MC "It's [player_name]"

    Rex "Right, well, [player_name]. Would you like to go to stampede with me this summer?"

    menu:
        "{color=#000000}Sure, why not{/color}":
            jump scene9_1_1
        "{color=#000000}Sorry, I'm not {i}that{/i} into cowboys{/color}":
            jump scene9_1_2
label scene9_1_1:
    Rex "Wait really? I mean uh, great!"
    Rex "But I guess it's kinda the middle of February so uh..."

    MC "That's okay, we could go somewhere else instead"

    Rex "W-whoa no way. That would be awesome."

    GUBA "... I can't believe that worked"

    Rex "uh... we have to get to class... but here's my number so we can talk later. Is that alright?"

    MC "Sure thing :^)"

    Rex "Okay great! Well... uh... see you around!"

    hide rex neutral with dissolve
    N "[[Rex leaves with a skip in his step while GUBa stares into space]"

    Rex "Come on GUBA we're gonna be late. You can't afford to take anymore Ls today"

    GUBA "..."

    hide guba right with dissolve

    MC "(Well, didn't expect that to happen. But hey, maybe it'll be fun. He seems nice)"

    scene bg black with Dissolve(1.0)

    N "[[You spend some time in the lab working on an assignment and pack up when you're done]"
    N "[[Over the coming weeks you spend plenty of time with Rex getting to know each other more]"
    N "[[What will happen next?]"
    N "[[GOOD END]"
    N "This is where the demo ends for this route. Would you like to see the other routes?"
    menu:
        "{color=#000000}Yes (Go to Hallway){/color}":
            jump scene5
        "{color=#000000}Yes (From The Lab){/color}":
            jump scene9
        "{color=#000000}No thanks{/color}":
            jump end
label scene9_1_2:
    Rex "Oh, okay. Fair enough"

    GUBA "Yeah okay. That's what I thought."

    Rex "Shut up GUBA, I'll show you sooner or later"

    N "The boys continue to argue as they head out"

    hide rex neutral with dissolve
    hide guba right with dissolve

    GUBA "Yeah whatever dork. You couldn't get a date if your oil prices depended on it"

    Rex "Didn't see you making it that far"

    GUBA "*tch* Whatever"

    N "[[You spend some time in the lab working on an assignment and pack up when you're done]"

    jump scene5

label scene9_2:
    GUBA "Looks like your plan backfired nerd"

    Rex "*sigh* Fine, I guess you win. I'm gonna get to class"

    hide rex neutral with dissolve
    show guba neutral at center with dissolve

    GUBA "..."
    MC "..."

    GUBA "So uh... You wanna actually go out some time?"
    menu:
        "{color=#000000}Sure I guess{/color}":
            jump scene9_2_1
        "{color=#000000}I'm good bro{/color}":
            jump scene9_2_2

label scene9_2_1:
    GUBA "Oh, cool... see you around then"
    hide guba neutral with dissolve
    scene bg black with Dissolve(1.0)
    N "[[A week later you go to West Edmonton Mall with GUBA]"
    N "[[It was okay]"
    N "[[You never went out together again]"
    N "[[MEDIOCRE ENDING]"
    N "This is where the demo ends for this route. Would you like to see the other routes?"
    menu:
        "{color=#000000}Yes (Go to Hallway){/color}":
            jump scene5
        "{color=#000000}Yes (From The Lab){/color}":
            jump scene9
        "{color=#000000}No thanks{/color}":
            jump end

label scene9_2_2:
    GUBA "Oh, yeah, that's cool"
    GUBA "I get you"
    GUBA "..."
    GUBA "See you around"

    hide guba neutral with dissolve

    N "[[You spend some time in the lab working on an assignment and pack up when you're done]"

    jump scene5

label scene10:
    scene bg dorm with dissolve
    N "[[You arrive in your dorm]"
    N "[[It's barren, save for the desk and bed, but it's home]"

    MC "(It's been a long day)"
    MC "(I'm in a new country, I'm meeting new people)"
    MC "(Heck, I even met the prime minister!)"

    N "[[your cushion mattress lets out a sigh as you flop onto it]"

    MC "I wonder if every day will be this exciting..."
    MC "*YAWWWWNNN*"

    scene bg black with Dissolve(2.0)

    pause 0.5

    scene bg beach with Dissolve(1.0)

    MC "What? Where am I?"
    MC "I thought we were landlocked..."
    MC "Wha... what is that???"

    show usdj running with dissolve

    N ""

    show usdj close with dissolve

    Mystery "*huff* *huff* *pant* *pant*"

    MC "!?!?"

    show usdj neutral with dissolve

    pause 0.5

    USDJ "You must be a charity, because my heart is racing for you"
    menu:
        "{color=#000000}UwU{/color}":
            show usdj uwu with dissolve
            USDJ "UwU"
            show usdj neutral with dissolve
            USDJ "You will always be my waifu [player_name]-chan"
            pass
        "{color=#000000}Sir please, I'm just here to learn about differential equations{/color}":
            USDJ "Haha, you always make me laugh [player_name]-chan"
            show usdj king with dissolve
            USDJ "As expected of my queen ;^)"
            show usdj neutral with dissolve
            pass

    show usdj worry with dissolve
    USDJ "Am I really as sugoi as you say [player_name]-chan?"
    menu:
        "{color=#000000}Yes{/color}":
            pass
        "{color=#000000}Of course{/color}":
            pass
        "{color=#000000}Always{/color}":
            pass
        "{color=#000000}hai{/color}":
            pass
    show usdj neutral with dissolve
    USDJ "OwO"
    show usdj uwu with dissolve
    USDJ "y-you too"
    show usdj bye at left with dissolve
    USDJ "Farewell my love!~"
    USDJ "Till we meet again <3"
    hide usdj bye with dissolve
    MC "..."
    scene bg black with Dissolve(1.0)
    scene bg dorm with dissolve
    MC "{cps=1}...............{/cps}"
    N "[[You decide never to talk to anyone ever again, lest you slip up and share what you have just experienced]"
    jump end

label end:
    return
