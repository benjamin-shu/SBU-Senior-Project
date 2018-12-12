# Define images for background art.
# West Apartments
image West F 301 Hallway = "Backgrounds/West F 301 Hallway 1.png"
image West F 301C Door = "Backgrounds/West F 301C Door.png"
# Frey Hall
image Frey Hall Front = "Backgrounds/Frey Hall Front.png"
# Javits Lecture Hall
image Javits Front Door = "Backgrounds/Javits Front Door.png"
# Staller Center for the Arts
image Staller = "Backgrounds/Staller.png"
image Staller Music = "Backgrounds/Staller Music.png"
image eMedia Seats = "Backgrounds/eMedia Seats.png"
image eMedia Screen = "Backgrounds/eMedia Screen.png"

# Character sprites for Ben's introduction scene.
image Ben Intro Cas Brth = "Ben/Intro/Casual Breathe.png"
image Ben Intro Cas Neut Spk = "Ben/Intro/Casual Neutral Speaking.png"
image Ben Intro Cas Sto = "Ben/Intro/Casual Stoic.png"
image Ben Intro Cas Sto Spk = "Ben/Intro/Casual Stoic Speaking.png"
image Ben Intro Cas Fru Spk = "Ben/Intro/Casual Frustrated Speaking.png"
image Ben Intro Hands Ddpn = "Ben/Intro/Hands Deadpan.png"
image Ben Intro Hands Sml = "Ben/Intro/Hands Smile.png"
image Ben Intro Hel Spk = "Ben/Intro/Hello Speaking.png"
image Ben Intro Hel Awk = "Ben/Intro/Hello Awkward.png"
image Ben Intro Hel Fru = "Ben/Intro/Hello Frustrated.png"
image Ben Intro Pho = "Ben/Intro/Phone.png"
image Ben Intro Pho Spk = "Ben/Intro/Phone Speaking.png"
image Ben Intro Pho Fru = "Ben/Intro/Phone Frustrated.png"
image Ben Intro Pho Fru Spk = "Ben/Intro/Phone Frustrated Speaking.png"
image Ben Intro Pho Chk = "Ben/Intro/Phone Check.png"
image Ben Intro Pho Chk Fru Spk = "Ben/Intro/Phone Check Frustrated Speaking.png"

# Character sprites for Ben.
define Ben_Walk_Neut = "Ben/Walking/Neutral.png"
define Ben_Walk_Neut_Spk = "Ben/Walking/Neutral Speaking.png"
define Ben_Walk_Bore = "Ben/Walking/Bored.png"
define Ben_Walk_Bore_Spk = "Ben/Walking/Bored Speaking.png"
# define Ben_Walk Annoy = "Ben/Walking/Annoyed.png"
# define Ben_Walk_Annoy_Spk = "Ben/Walking/Annoyed Speaking.png"
# define Ben_Walk_Sus = "Ben/Walking/Sus.png"
# define Ben_Walk_Sus_Spk = "Ben/Walking/Sus Speaking.png"
define Ben_Casual_Neut = "Ben/Casual/Neutral.png"
define Ben_Casual_Neut_Spk = "Ben/Casual/Neutral Speaking.png"
define Ben_Casual_Sto = "Ben/Casual/Stoic.png"
define Ben_Casual_Sto_Spk = "Ben/Casual/Stoic Speaking.png"

# Character sprites for Faith.
define Faith_Walk_Neut = "Faith/Walking/Neutral.png"
define Faith_Walk_Neut_Spk = "Faith/Walking/Neutral Speaking.png"
# define Faith_Walk_Pens = "Faith/Walking/Pensive.png"
# define Faith_Walk_Pens_Spk = "Faith/Walking/Pensive Speaking.png"
# define Faith_Walk_PupD = "Faith/Walking/Puppy Dog.png"
# define Faith_Walk_PupD_Spk = "Faith/Walking/Puppy Dog Speaking.png"
# define Faith_Walk_Sere = "Faith/Walking/Serene.png"
# define Faith_Walk_Sere_Spk = "Faith/Walking/Serene Speaking.png"
define Faith_Hello_Spk = "Faith/Hello/Speaking.png"

# Character sprites for Maria. (HAS NOT APPEARED)
define Maria_Walk_Neut = "Maria/Walking/Neutral.png"
# define Maria_Walk_Neut_Spk = "Maria/Walking/Neutral Speaking.png"
# define Maria_Walk_Chee = "Maria/Walking/Cheerful.png"
# define Maria_Walk_Chee_Spk = "Maria/Walking/Cheerful Speaking.png"
# define Maria_Walk_Annoy = "Maria/Walking/Annoyed.png"
# define Maria_Walk_Annoy_Spk = "Maria/Walking/Annoyed Speaking.png"
# define Maria_Walk_Conf = "Maria/Walking/Confused.png"
# define Maria_Walk_Conf_Spk = "Maria/Walking/Confused Speaking.png"

# Character sprites for Rajesh. (HAS NOT APPEARED)
define Rajesh_Walk_Neut = "Rajesh/Walking/Neutral.png"
# define Rajesh_Walk_Neut_Spk = "Rajesh/Walking/Neutral Speaking.png"

# Definitions for each DynamicCharacter object used.
define b_name = "Ben"
image b_sprite = DynamicImage("[b_path]")
define b_path = ""
define B = DynamicCharacter("b_name", who_color="#71B7E2", who_bold=True,
    what_Size=30, what_Bold=False, what_font="fonts/Courier Prime Bold.ttf")

define f_name = "???"
image f_sprite = DynamicImage("[f_path]")
define f_path = ""
define F = DynamicCharacter("f_name", who_color="#FFFF66", who_bold=True, who_font="fonts/Amatic-Bold.ttf",
    what_Size=30, what_bold=True)

define m_name = "???"
image m_sprite = DynamicImage("[m_path]")
define m_path = ""
define M = DynamicCharacter("m_name", who_color="#C42727", who_bold=False, who_font="fonts/Chunkfive.otf",
    what_Size=30, what_bold=True)

define r_name = "???"
image r_sprite = DynamicImage("[r_path]")
define r_path = ""
define R = DynamicCharacter("r_name", who_color="#159639", who_bold=True,
    what_Size=30, what_Bold=True, what_font="fonts/KaushanScript-Regular.otf")

# Define speaking positions for character sprites.
define center_l = Position(xpos = 0.25)
define center_r = Position(xpos = 0.75)
define seat_l = Position(xpos = 0.27, xanchor = 225, ypos = 0.55, yanchor = 360)
define seat_r = Position(xpos = 0.73, xanchor = 225, ypos = 0.55, yanchor = 360)

# Define new default Dissolve for transitions between sprites.
define dissolve = Dissolve(0.5)

# Define transformation for scaling images.
init:
    transform img_Scale(x, y):
        size (x, y)

# Screen Effects - Images
# A simple black screen.
image Black = "Screen Effects/Black.png"

# Screen Effects - ATL
# A short animation for TV static.
image static:
    alpha 0.0
    "Screen Effects/Static 1.png" with dissolve
    linear 0.25 alpha 1.0
    0.25
    "Screen Effects/Static 2.png" with dissolve
    0.25
    "Screen Effects/Static 1.png" with dissolve
    0.25
    "Screen Effects/Static 2.png" with dissolve
    linear 0.25 alpha 0.0

# Close a clapper board labeled "Take 1".
image take1:
    xalign 0.0
    "Screen Effects/Take 1 Open.png"
    linear 0.5 xalign 1.0
    0.25
    "Screen Effects/Take 1 Closed.png" with dissolve
    0.5
    linear 0.75 alpha 0.0

# Close a clapper board labeled "Take 2".
image take2:
    xalign 0.0
    "Screen Effects/Take 2 Open.png"
    linear 0.5 xalign 1.0
    0.25
    "Screen Effects/Take 2 Closed.png" with dissolve
    0.5
    linear 0.75 alpha 0.0

# Close a clapper board labeled "Take 3".
# image take3:
#     xalign 0.0
#     "Screen Effects/Take 3 Open.png"
#     linear 0.5 xalign 1.0
#     0.25
#     "Screen Effects/Take 3 Closed.png" with dissolve
#     0.5
#     linear 0.75 alpha 0.0

# Close a clapper board labeled "Take 4".
# image take4:
#     xalign 0.0
#     "Screen Effects/Take 4 Open.png"
#     linear 0.5 xalign 1.0
#     0.25
#     "Screen Effects/Take 4 Closed.png" with dissolve
#     0.5
#     linear 0.75 alpha 0.0

# Dim the lights for the eMedia SINC Site screen.

# Game starts here.
label start:
    scene West F 301 Hallway with fade

    show Ben Intro Cas Sto with dissolve
    B "..."
    show Ben Intro Cas Sto Spk with dissolve
    B "...okay, is this thing recording?"
    show Ben Intro Cas Fru Spk with dissolve
    B "...ah crap, it is!"
    show Ben Intro Cas Sto Spk with dissolve
    B "Okay, going to have to cut this-"

    window hide
    show Ben Intro Hel Spk:
    show take1:
    with dissolve
    $ renpy.pause(1.0)
    window show

    B "Hey, guys. My name is Benjamin Shu."
    B "I'm in my senior year here, and-"
    "RRRIIING! RRRIIING! RRRIIING!"
    show Ben Intro Hel Awk with dissolve
    B "..."
    show Ben Intro Hel Fru with dissolve
    B "...son of a {i}bitch{/i}!"
    show Ben Intro Pho Chk Fru Spk with dissolve
    B "Why {i}now{/i}?"
    show Ben Intro Pho Spk with dissolve
    B "Hello?"
    B "No, everything's fine here. I finished unpacking a while ago."
    show Ben Intro Pho with dissolve
    B "..."
    show Ben Intro Pho Spk with dissolve
    B "Okay. Where is this internship?"
    B "...no, I don't really have any experience with that."
    B "I know. I'll look in a bit."
    B "Yeah, I know. I'll go see an advisor soon."
    show Ben Intro Pho Fru Spk with dissolve
    B "...{i}yes{/i}, I know. I won't let it happen again."
    show Ben Intro Pho Spk with dissolve
    B "Okay. I will. Bye, mom."
    show Ben Intro Pho Chk with dissolve
    B "..."

    window hide
    show Ben Intro Cas Sto Spk:
    show take2:
    with dissolve
    $ renpy.pause(1.0)
    window show

    B "Okay, here goes. From the top..."
    show Ben Intro Cas Brth with dissolve
    B "..."
    show Ben Intro Hel Spk with dissolve
    B "Hello! My name is Benjamin Shu."
    show Ben Intro Hands Sml with dissolve
    B "I am a senior computer science major, here at Stony Brook..."
    show Ben Intro Hands Ddpn with dissolve
    B "...and like a lot of people my age, I have no idea what I'm doing with my life."
    show Ben Intro Cas Neut Spk with dissolve
    B "Recently, I've started thinking that this {i}might{/i} be a problem."
    show Ben Intro Sto Spk with dissolve
    B "I can't say that I've accomplished much over the last four years..."
    B "...but I wanted to make something of my time here before I left."
    show Ben Intro Hands Ddpn with dissolve
    B "So I’m going to try and turn the disorganized mess of thoughts and feelings inside my head into something coherent."
    B "Something people might actually {i}care{/i} about."
    show Ben Intro Hands Sml with dissolve
    B "And hopefully, something worth their time."
    show Ben Intro Cas Neut Spk with dissolve
    B "With that in mind, welcome to the show. I hope you enjoy your stay."

    scene Black with fade

label Day1:
    scene West F 301C Door with fade

    B "{i}When I was in my senior year of high school, I couldn’t wait to leave for college.{/i}"
    B "{i}Four years later, and here I am wondering where the hell I’m going next.{/i}"

    $ b_path = Ben_Walk_Bore;
    show b_sprite at center, img_Scale(500, 800) with dissolve

    B "{i}Laptop, charger, headphones…{/i}"
    B "{i}…binder, pencil case, notepad…{/i}"
    B "{i}…water bottle, running shoes, spare shirt…{/i}"
    B "{i}…first-aid kit, scissors, mini-stapler…{/i}"

    $ b_path = Ben_Walk_Bore_Spk
    show b_sprite with dissolve

    B "…and the flashlight. Can’t forget the flashlight."
    B "Okay. I think that’s everything."
    B "I’m going to head out to class now. I’ll see you guys later."
    $ b_path = Ben_Walk_Bore
    show b_sprite with dissolve
    "Kris" "See you later, Shuben."

    scene Black with fade

    B "{i}First stop of the day: Staller Center for the Arts.{/i}"
    B "{i}Okay, Ben. You’ve only got two more semesters left.{/i}"
    B "{i}Try not to fuck this up.{/i}"
    hide b_sprite with dissolve

label Day1_ARS:
    scene Staller with fade

    B "{i}It’s been a while since I was last here.{/i}"
    scene Staller Music with fade
    B "{i}If I remember correctly, all of the digital art classes
       are held on the Music side of the building…{/i}"
    B "{i}…because {b}that{/b}, of course, makes {b}perfect{/b} sense.{/i}"

    scene eMedia Seats with fade

    $ b_path = Ben_Walk_Bore
    show b_sprite at center, img_Scale(500, 800) with dissolve
    B "{i}Hm. Nobody’s here yet. Guess I’ll just sit down here and wait…{/i}"
    $ b_path = Ben_Casual_Sto
    show b_sprite at seat_l with dissolve
    B "{i}…all by myself…{/i}"
    B "{i}…staring at a computer.{/i}"
    $ b_path = Ben_Casual_Sto_Spk
    show b_sprite with dissolve
    B "Why did I leave my room, again?"
    $ b_path = Ben_Casual_Sto

    $ f_path = Faith_Hello_Spk
    show f_sprite at Position(xpos = 0.73, xanchor = 0.5), img_Scale(500, 800) with dissolve
    F "Hello!"
    $ f_path = Faith_Walk_Neut_Spk
    show f_sprite with dissolve
    F "Is this seat taken?"
    $ f_path = Faith_Walk_Neut

    $ b_path = Ben_Casual_Neut_Spk
    show b_sprite with dissolve
    B "Oh! No, it’s not taken. Go right ahead."
    $ b_path = Ben_Casual_Neut

    $ f_path = Faith_Walk_Neut_Spk
    show f_sprite with dissolve
    F "Thank you!"
    $ f_path = Faith_Walk_Neut
    show f_sprite at seat_r with dissolve

    # show Faith Sitting Neut with dissolve

    B "{i}...{/i}"
    B "{i}...well, this is an uncomfortable silence.{/i}"
    B "{i}Maybe I should say something?{/i}"

label Faith_Meet:
    define faith_obs = 0
    define faith_talked = False
    menu:
        "{i}Maybe I should say something?{/i}"

        "Say nothing.":
            B "{i}...nah. She’s probably got other things to think about right now.{/i}"
            B "{i}No sense in me bothering her.{i}"

        "Look for conversation starters.":
            if faith_obs >= 2:
                B "{i}Okay, that’s enough staring. This is starting to feel creepy.{/i}"
                $ faith_obs = faith_obs + 1
                jump Faith_Meet
            elif faith_obs == 1:
                B "{i}It looks like she’s working with Adobe Illustrator.{/i}"
                B "{i}She’s working on a profile view of a person’s face…{/i}"
                B "{i}Have I seen that before? It kind of looks like the main character from Undertale...{/i}"
                B "{i}Maybe I should ask.{/i}"
                $ faith_obs = faith_obs + 1
                jump Faith_Meet
            elif faith_obs == 0:
                B "{i}Blonde hair, black t-shirt with ripped jeans, and a MacBook.{/i}"
                B "{i}I’ve always wondered why ripped jeans were a thing.{/i}"
                B "{i}…maybe now’s not the best time to ask, though.{/i}"
                B "{i}Maybe there’s something else…?{/i}"
                $ faith_obs = faith_obs + 1
                jump Faith_Meet

        "Attempt idle small talk.":
            if faith_obs < 2:
                B "So, uh, what’s your name?"
                F "…"
                B "…hello?"
                F "Hm? Oh! Sorry, did you say something?"
                B "What’s your name?"
                $ f_name = "Faith"
                F "My name is Faith. And your name is…?"
                B "My name is Ben. It’s nice to meet you!"
                F "Likewise!"
                # Needs rewrite!
                F "I’m really sorry to cut you off - I don’t want to be rude or anything…"
                F "But I really need to get this thing done."
                B "Oh! Okay, that’s fine. I completely understand."
                B "I’ll let you get to it, then."
            elif faith_obs == 2:
                B "Excuse me?"
                F "Hm? Oh! Hi!"
                F "What’s up?"
                B "If you don’t mind me asking, are you drawing Frisk?"
                # Smiling
                F "Yeah, I am! Have you played Undertale?"
                B "Yeah! It’s one of my favorite video games!"
                F "Who was your favorite character?"
                B "Sans, hands down."

                # [An image of Sans’ pixel art appears on-screen.]

                B "The man is incapable of taking anything seriously, and it’s amazing."

                # [An image of Toriel appears on-screen.]

                F "Personally, Toriel is my favorite. After all, Goat Mom is Best Mom."
                B "Ha! Never heard that one before."
                B "So is the Frisk drawing for a class?"
                F "No, it’s actually for a YouTube video I wanted to make."

                # [An image of a YouTube video with a blank thumbnail appears.]

                F "I need a thumbnail, and I wanted to use Frisk."
                B "Wow. What kind of video is it?"
                F "It’s kind of a commentary, at this point. It’s…a work in progress."
                B "Well, I’ll have to check it out some time."
                B "I’m Ben, by the way! What’s your name?"
                $ f_name = "Faith"
                F "My name is Faith! Nice to meet you!"
                B "Likewise!"

# Conclusion sequence.
label End:
    return
