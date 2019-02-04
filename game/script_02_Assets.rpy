# ==========================================================================
# Intro Sequence Presentation Slides
# ==========================================================================

image Intro Slide 1 = "Screen Effects/Intro Slide 1.png"
image Intro Slide 2 = "Screen Effects/Intro Slide 2.png"
image Intro Slide 3 = "Screen Effects/Intro Slide 3.png"
image Intro Slide 4 = "Screen Effects/Intro Slide 4.png"
image Intro Slide 5 = "Screen Effects/Intro Slide 5.png"

# ==========================================================================
# Background Art
# ==========================================================================

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

# Define new default Dissolve for transitions between sprites.
define dissolve = Dissolve(0.5)

init:
    # Define transformation for scaling images.
    transform img_Scale(x, y):
        size (x, y)

    # Define transformation for centering images on projector screen.
    transform projectCenter():
        xalign 0.5
        yalign 0.2

# ==========================================================================
# Screen Effects - Images
# ==========================================================================

# A simple black screen.
image Black = "Screen Effects/Black.png"
image Dimmed = "Screen Effects/Dimmed.png"
image Macbook = "Screen Effects/Macbook Screen.png"

# Used in first week to show contents of Ben's bag.
image Backpack 1 = "Screen Effects/Backpack_1.png"
image Backpack 2 = HBox("Screen Effects/Backpack_1.png", "Screen Effects/Backpack_2.png")
image Backpack 3 = VBox(HBox("Screen Effects/Backpack_1.png", "Screen Effects/Backpack_2.png"), "Screen Effects/Backpack_3.png")
image Backpack 4 = VBox(HBox("Screen Effects/Backpack_1.png", "Screen Effects/Backpack_2.png"), HBox("Screen Effects/Backpack_3.png", "Screen Effects/Backpack_4.png"))

# ==========================================================================
# Screen Effects - ATL
# ==========================================================================

## (UNUSED)
## A short animation for TV static.
# image static:
#     alpha 0.0
#     "Screen Effects/Static 1.png" with dissolve
#     linear 0.25 alpha 1.0
#     0.25
#     "Screen Effects/Static 2.png" with dissolve
#     0.25
#     "Screen Effects/Static 1.png" with dissolve
#     0.25
#     "Screen Effects/Static 2.png" with dissolve
#     linear 0.25 alpha 0.0

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

## (UNUSED)
## Close a clapper board labeled "Take 3".
# image take3:
#     xalign 0.0
#     "Screen Effects/Take 3 Open.png"
#     linear 0.5 xalign 1.0
#     0.25
#     "Screen Effects/Take 3 Closed.png" with dissolve
#     0.5
#     linear 0.75 alpha 0.0

## (UNUSED)
## Close a clapper board labeled "Take 4".
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
    "Screen Effects/Projector 0.png" with Dissolve(0.5)
    0.25
    "Screen Effects/Projector 1.png" with Dissolve(0.5)
    0.25
    "Screen Effects/Projector 2.png" with Dissolve(0.5)
    0.25
    "Screen Effects/Projector 3.png" with Dissolve(0.5)

# Quick fade in/out with a black screen
image fadeInOut:
    "Screen Effects/Black.png"
    alpha 0.0
    linear 0.5 alpha 1.0
    0.25
    linear 0.5 alpha 0.0

# ==========================================================================
# Screen Positions - Character Sprites
# ==========================================================================
init:
    transform center_l():
        xpos 0.25
        xanchor 225
        yanchor 360

    transform center_l_stand():
        xpos 0.25
        xanchor 225
        ypos 0.15
        yanchor 360

    transform center_r():
        xpos 0.75
        xanchor 225
        yanchor 360

    transform center_r_stand():
        xpos 0.75
        xanchor 225
        ypos 0.15
        yanchor 360

    transform center_stand():
        xpos 0.5
        xanchor 225
        ypos 0.15
        yanchor 360

    transform seat_l():
        xpos 0.27
        xanchor 225
        ypos 0.55
        yanchor 360

    transform seat_r():
        xpos 0.73
        xanchor 225
        ypos 0.55
        yanchor 360

# ==========================================================================
# DynamicCharacter Definitions
# ==========================================================================
define b_name = "Ben"
define B = DynamicCharacter("b_name", image="Ben", who_color="#71B7E2", who_bold=True,
    what_Size=30, what_Bold=False, what_font="fonts/Courier Prime Bold.ttf")

# # (UNUSED)
# define f_name = "???"
# define f_path = ""
# define F = DynamicCharacter("f_name", image="Faith", who_color="#FFFF66", who_bold=True, who_font="fonts/Pacifico.ttf",
#     what_Size=30, what_bold=False, what_font="fonts/Pacifico.ttf")

# # (UNUSED)
# define m_name = "???"
# define m_path = ""
# define M = DynamicCharacter("m_name", image="Maria", who_color="#C42727", who_bold=False, who_font="fonts/Chunkfive.otf",
#     what_Size=30, what_bold=True)

# # (UNUSED)
# define r_name = "???"
# define r_path = ""
# define R = DynamicCharacter("r_name", image="Rajesh", who_color="#159639", who_bold=True,
#     what_Size=30, what_Bold=True, what_font="fonts/KaushanScript-Regular.otf")
