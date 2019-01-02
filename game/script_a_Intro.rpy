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

# Default darkness setting for sprites.
define dark = -0.25

# Character sprites for Ben's introduction scene.
image Ben Intro Cas Brth = "Ben/Intro/Casual Breathe.png"
image Ben Intro Cas Neut Spk = "Ben/Intro/Casual Neutral Speaking.png"
image Ben Intro Cas Sto = "Ben/Intro/Casual Stoic.png"
image Ben Intro Cas Sto Dark = im.MatrixColor("Ben/Intro/Casual Stoic.png", im.matrix.brightness(dark))
image Ben Intro Cas Sto Spk = "Ben/Intro/Casual Stoic Speaking.png"
image Ben Intro Cas Sto Spk Dark = im.MatrixColor("Ben/Intro/Casual Stoic Speaking.png", im.matrix.brightness(dark))
image Ben Intro Cas Fru Spk = "Ben/Intro/Casual Frustrated Speaking.png"
image Ben Intro Hel Spk = "Ben/Intro/Hello Speaking.png"
image Ben Intro Hel Awk = "Ben/Intro/Hello Awkward.png"
image Ben Intro Hel Fru = "Ben/Intro/Hello Frustrated.png"
image Ben Intro Pho Dark = im.MatrixColor("Ben/Intro/Phone.png", im.matrix.brightness(dark))
image Ben Intro Pho Spk Dark = im.MatrixColor("Ben/Intro/Phone Speaking.png", im.matrix.brightness(dark))
image Ben Intro Pho Fru Spk Dark = im.MatrixColor("Ben/Intro/Phone Frustrated Speaking.png", im.matrix.brightness(dark))
image Ben Intro Pho Chk Dark = im.MatrixColor("Ben/Intro/Phone Check.png", im.matrix.brightness(dark))
image Ben Intro Pho Chk Fru Spk Dark = im.MatrixColor("Ben/Intro/Phone Check Frustrated Speaking.png", im.matrix.brightness(dark))

image side Ben Intro Cas Neut Spk Si = im.FactorScale("Ben/Intro/Casual Neutral Speaking.png", 0.5)
image side Ben Intro Cas Sto Spk Si = im.FactorScale("Ben/Intro/Casual Stoic Speaking.png", 0.5)
image side Ben Intro Hel Spk Si = im.FactorScale("Ben/Intro/Hello Speaking.png", 0.5)
image side Ben Intro Hands Sml Si = im.FactorScale("Ben/Intro/Hands Smile.png", 0.5)
image side Ben Intro Hands Ddpn Si = im.FactorScale("Ben/Intro/Hands Deadpan.png", 0.5)

# Character sprites for Ben.
image Ben Walk Neut = "Ben/Walking/Neutral.png"
image Ben Walk Neut Dark = im.MatrixColor("Ben/Walking/Neutral.png", im.matrix.brightness(dark))
image Ben Walk Neut Spk = "Ben/Walking/Neutral Speaking.png"
image Ben Walk Bore = "Ben/Walking/Bored.png"
image Ben Walk Bore Dark = im.MatrixColor("Ben/Walking/Bored.png", im.matrix.brightness(dark))
image Ben Walk Bore Spk = "Ben/Walking/Bored Speaking.png"
# image Ben Walk Annoy = "Ben/Walking/Annoyed.png"
# image Ben Walk Annoy Spk = "Ben/Walking/Annoyed Speaking.png"
# image Ben Walk Sus = "Ben/Walking/Sus.png"
# image Ben Walk Sus Spk = "Ben/Walking/Sus Speaking.png"
image Ben Casual Neut = "Ben/Casual/Neutral.png"
image Ben Casual Neut Dark = im.MatrixColor("Ben/Casual/Neutral.png", im.matrix.brightness(dark))
image Ben Casual Neut Spk = "Ben/Casual/Neutral Speaking.png"
image Ben Casual Sto = "Ben/Casual/Stoic.png"
image Ben Casual Sto Dark = im.MatrixColor("Ben/Casual/Stoic.png", im.matrix.brightness(dark))
image Ben Casual Sto Spk = "Ben/Casual/Stoic Speaking.png"

# Character sprites for Faith.
image Faith Walk Neut = "Faith/Walking/Neutral.png"
image Faith Walk Neut Dark = im.MatrixColor("Faith/Walking/Neutral.png", im.matrix.brightness(dark))
image Faith Walk Neut Spk = "Faith/Walking/Neutral Speaking.png"
# image Faith Walk Pens = "Faith/Walking/Pensive.png"
# image Faith Walk Pens Spk = "Faith/Walking/Pensive Speaking.png"
# image Faith Walk PupD = "Faith/Walking/Puppy Dog.png"
# image Faith Walk PupD Spk = "Faith/Walking/Puppy Dog Speaking.png"
# image Faith Walk Sere = "Faith/Walking/Serene.png"
# image Faith Walk Sere Spk = "Faith/Walking/Serene Speaking.png"
image Faith Hello Spk = "Faith/Hello/Speaking.png"
image Faith Mac Foc Neut = "Faith/Macbook Focus/Neutral.png"
image Faith Mac Foc Neut Dark = im.MatrixColor("Faith/Macbook Focus/Neutral.png", im.matrix.brightness(dark))
image Faith Mac LkUp Neut = "Faith/Macbook LookUp/Neutral.png"
image Faith Mac LkUp Spk = "Faith/Macbook LookUp/Speaking.png"

# Character sprites for Maria. (HAS NOT APPEARED)
image Maria Walk Neut = "Maria/Walking/Neutral.png"
# image Maria Walk Neut Spk = "Maria/Walking/Neutral Speaking.png"
# image Maria Walk Chee = "Maria/Walking/Cheerful.png"
# image Maria Walk Chee Spk = "Maria/Walking/Cheerful Speaking.png"
# image Maria Walk Annoy = "Maria/Walking/Annoyed.png"
# image Maria Walk Annoy Spk = "Maria/Walking/Annoyed Speaking.png"
# image Maria Walk Conf = "Maria/Walking/Confused.png"
# image Maria Walk Conf Spk = "Maria/Walking/Confused Speaking.png"

# Character sprites for Rajesh. (HAS NOT APPEARED)
image Rajesh Walk Neut = "Rajesh/Walking/Neutral.png"
# image Rajesh Walk Neut Spk = "Rajesh/Walking/Neutral Speaking.png"


# Define new default Dissolve for transitions between sprites.
define dissolve = Dissolve(0.5)

# Define transformation for scaling images.
init:
    transform img_Scale(x, y):
        size (x, y)

# Screen Effects - images
# A simple black screen.
image Black = "Screen Effects/Black.png"
image Dimmed = "Screen Effects/Dimmed.png"
image Macbook = "Screen Effects/Macbook Screen.png"

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

# Turn on a projector screen in current scene.
image projector:
    0.5
    "Screen Effects/Projector 0.png" with Dissolve(2.5)
    0.5
    "Screen Effects/Projector 1.png" with Dissolve(0.5)
    0.5
    "Screen Effects/Projector 2.png" with Dissolve(0.5)
    0.5
    "Screen Effects/Projector 3.png" with Dissolve(0.5)
    0.5

# Define speaking positions for character sprites.
define center_l = Position(xpos = 0.25)
define center_r = Position(xpos = 0.75)
define seat_l = Position(xpos = 0.27, xanchor = 225, ypos = 0.55, yanchor = 360)
define seat_r = Position(xpos = 0.73, xanchor = 225, ypos = 0.55, yanchor = 360)

# Definitions for each DynamicCharacter object used.
define b_name = "Ben"
define B = DynamicCharacter("b_name", image="Ben", who_color="#71B7E2", who_bold=True,
    what_Size=30, what_Bold=False, what_font="fonts/Courier Prime Bold.ttf")

define f_name = "???"
define f_path = ""
define F = DynamicCharacter("f_name", image="Faith", who_color="#FFFF66", who_bold=True, who_font="fonts/Amatic-Bold.ttf",
    what_Size=30, what_bold=True)

define m_name = "???"
define m_path = ""
define M = DynamicCharacter("m_name", image="Maria", who_color="#C42727", who_bold=False, who_font="fonts/Chunkfive.otf",
    what_Size=30, what_bold=True)

define r_name = "???"
define r_path = ""
define R = DynamicCharacter("r_name", image="Rajesh", who_color="#159639", who_bold=True,
    what_Size=30, what_Bold=True, what_font="fonts/KaushanScript-Regular.otf")

# Game starts here.
label start:
    scene West F 301 Hallway with fade

    show Ben Intro Cas Sto Dark at center with dissolve
    B "..."

    show Ben Intro Cas Sto Spk with dissolve
    B "...okay, is this thing recording?"

    show Ben Intro Cas Fru Spk with dissolve
    B "...ah crap, it is!"
    show Ben Intro Cas Sto Spk Dark with dissolve
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
    show Ben Intro Pho Chk Fru Spk Dark with dissolve
    B "Why {i}now{/i}?"
    show Ben Intro Pho Spk Dark with dissolve
    B "Hello?"
    B "No, everything's fine here. I finished unpacking a while ago."
    show Ben Intro Pho Dark with dissolve
    B "..."
    show Ben Intro Pho Spk Dark with dissolve
    B "Okay. Where is this internship?"
    B "...no, I don't really have any experience with that."
    B "I know. I'll look in a bit."
    B "Yeah, I know. I'll go see an advisor soon."
    show Ben Intro Pho Fru Spk Dark with dissolve
    B "...{i}yes{/i}, I know. I won't let it happen again."
    show Ben Intro Pho Spk Dark with dissolve
    B "Okay. I will. Bye, mom."
    show Ben Intro Pho Chk Dark with dissolve
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

    window hide
    show projector:
    hide Ben with dissolve
    $ renpy.pause(3.0)
    window show

    B Intro Hel Spk Si "Hello! My name is Benjamin Shu."
    B Intro Hands Sml Si "I am a senior computer science major, here at Stony Brook..."
    B Intro Hands Ddpn "...and like a lot of people my age, I have no idea what I'm doing with my life."
    B Intro Cas Neut Spk Si "Recently, I've started thinking that this {i}might{/i} be a problem."
    B Intro Cas Sto Spk Si "I can't say that I've accomplished much over the last four years..."
    B "...but I wanted to make something of my time here before I left."
    B Intro Hands Ddpn Si "So I’m going to try and turn the disorganized mess of thoughts and feelings inside my head into something coherent."
    B "Something people might actually {i}care{/i} about."
    B Intro Hands Sml Si "And hopefully, something worth their time."

    window hide
    hide projector with Dissolve(1.0)
    show Ben Intro Cas Neut Spk with dissolve
    window show

    B "With that in mind, welcome to the show. I hope you enjoy your stay."
    hide Ben with dissolve
    scene Black with fade

    jump Day1
