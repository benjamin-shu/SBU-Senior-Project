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

image Intro Slide 1 = "Screen Effects/Intro Slide 1.png"
image Intro Slide 2 = "Screen Effects/Intro Slide 2.png"
image Intro Slide 3 = "Screen Effects/Intro Slide 3.png"
image Intro Slide 4 = "Screen Effects/Intro Slide 4.png"
image Intro Slide 5 = "Screen Effects/Intro Slide 5.png"

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
# Default darkness setting for sprites.
define dark = -0.25

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
