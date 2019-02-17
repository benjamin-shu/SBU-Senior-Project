# ==============================================================================
# Ren'Py Object Definitions
# ==============================================================================
define b_name = "Ben"
define B = DynamicCharacter("b_name", image="Ben", who_color="#71B7E2", who_bold=True,
    what_Size=30, what_Bold=False, what_font="fonts/Courier Prime Bold.ttf")

define f_name = "???"
define f_path = ""
define F = DynamicCharacter("f_name", image="Faith", who_color="#FFFF66", who_bold=True, who_font="fonts/Pacifico.ttf",
    what_Size=30, what_bold=False, what_font="fonts/Pacifico.ttf")

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

# Default darkness setting for sprites.
define dark = -0.25

# Define new default Dissolve for transitions between sprites.
define dissolve = Dissolve(0.5)

# Define generic index counter.
default i = 0

# ==============================================================================
# Init Block - Transforms
# ==============================================================================
init:
    # Define transformation for scaling images.
    transform img_Scale(x, y):
        size (x, y)

    # Define transformation for centering images on projector screen.
    transform projectCenter():
        xalign 0.5
        yalign 0.2
# ==============================================================================
# Init Block - Screen Positions
# ==============================================================================
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

# ==============================================================================
# Python Statements (If Needed)
# ==============================================================================
# init python:

# ==============================================================================
# ARS Presentation Slides & Project Materials
# ==============================================================================

# Slides for first ARS assignment.
image Composition Slide 1 = "Slides/Composition/Slide 01.png"
image Composition Slide 2a = "Slides/Composition/Slide 02 a.png"
image Composition Slide 2b = "Slides/Composition/Slide 02 b.png"
image Composition Slide 2c:
    "Slides/Composition/Slide 02 c.png" with Dissolve(0.5)
    0.5
    "Slides/Composition/Slide 02 d.png" with Dissolve(0.5)
    0.5
    "Slides/Composition/Slide 02 e.png" with Dissolve(0.5)

image Composition Slide 3a = "Slides/Composition/Slide 03 a.png"
image Composition Slide 3b:
    "Slides/Composition/Slide 03 b.png" with Dissolve(0.5)
    0.5
    "Slides/Composition/Slide 03 c.png" with Dissolve(0.5)
    0.5
    "Slides/Composition/Slide 03 d.png" with Dissolve(0.5)

image Composition Slide 4:
    "Slides/Composition/Slide 04 a.png" with Dissolve(0.5)
    0.5
    "Slides/Composition/Slide 04 b.png" with Dissolve(0.5)

image Composition Slide 5:
    "Slides/Composition/Slide 05 a.png" with Dissolve(0.5)
    0.5
    "Slides/Composition/Slide 05 b.png" with Dissolve(0.5)

image Composition Slide 6 = "Slides/Composition/Slide 06.png"
image Composition Slide 7 = "Slides/Composition/Slide 07.png"
image Composition Slide 8 = "Slides/Composition/Slide 08.png"
image Composition Slide 9 = "Slides/Composition/Slide 09.png"

# First ARS assignment.
image Composition Canvas = "Projects/Composition_Canvas.png"

image Composition Point01 = "Projects/Composition_Point01.png"
image Composition Point02 = "Projects/Composition_Point02.png"
image Composition Point03 = "Projects/Composition_Point03.png"
image Composition Point04 = "Projects/Composition_Point04.png"
image Composition Point05 = "Projects/Composition_Point05.png"

image Composition Depth01 = "Projects/Composition_Depth01.png"
image Composition Depth02 = "Projects/Composition_Depth02.png"
image Composition Depth03 = "Projects/Composition_Depth03.png"
image Composition Depth04 = "Projects/Composition_Depth04.png"
image Composition Depth05 = "Projects/Composition_Depth05.png"

image Composition Shape01 = "Projects/Composition_Shape01.png"
image Composition Shape02:
    "Projects/Composition_Shape02.png" with Dissolve(0.5)
    0.5
    "Projects/Composition_Shape03.png" with Dissolve(0.5)
    0.5
    "Projects/Composition_Shape04.png" with Dissolve(0.5)
    0.5
image Composition Shape03 = "Projects/Composition_Shape03.png"
image Composition Shape04 = "Projects/Composition_Shape04.png"
image Composition Shape05 = "Projects/Composition_Shape05.png"
image Composition Shape06 = "Projects/Composition_Shape06.png"

# ==============================================================================
# CSE Presentation Slides & Project Materials
# ==============================================================================

# Slides for first CSE assignment.
image UML Slide 1 = "Slides/UML/Slide 01.png"
image UML Slide 2 = "Slides/UML/Slide 02.png"
image UML Slide 3a = "Slides/UML/Slide 03a.png"
image UML Slide 3b = "Slides/UML/Slide 03b.png"
image UML Slide 3c = "Slides/UML/Slide 03c.png"
image UML Slide 4a = "Slides/UML/Slide 04a.png"
image UML Slide 4b = "Slides/UML/Slide 04b.png"
image UML Slide 4c = "Slides/UML/Slide 04c.png"
image UML Slide 5a = "Slides/UML/Slide 05a.png"
image UML Slide 5b = "Slides/UML/Slide 05b.png"
image UML Slide 5c = "Slides/UML/Slide 05c.png"

# ==============================================================================
# Background Art
# ==============================================================================

# West Apartments
image West F 301 Hallway = "Backgrounds/West F 301 Hallway 1.png"
image West F 301C = "Backgrounds/West F 301C.png"
image West F 301C Door = "Backgrounds/West F 301C Door.png"

# Frey Hall
image Frey Hall Front = "Backgrounds/Frey Hall Front.png"

# Javits Lecture Hall
image Javits Front Door = "Backgrounds/Javits Front Door.png"
image Javits Seats = "Backgrounds/Javits Seats.png"
image Javits Screen = "Backgrounds/Javits Screen.png"

# Staller Center for the Arts
image Staller = "Backgrounds/Staller.png"
image Staller Music = "Backgrounds/Staller Music.png"
image eMedia Seats = "Backgrounds/eMedia Seats.png"
image eMedia Screen = "Backgrounds/eMedia Screen.png"

# ==============================================================================
# Screen Effects - Images
# ==============================================================================

# A simple black screen.
image Black = "Screen Effects/Black.png"
image Dimmed = "Screen Effects/Dimmed.png"
image Laptop = "Screen Effects/Laptop.png"
## (UNUSED)
#image Macbook = "Screen Effects/Macbook Screen.png"

# Used in first week to show contents of Ben's bag.
image Backpack 1 = "Screen Effects/Backpack_1.png"
image Backpack 2 = HBox("Screen Effects/Backpack_1.png", "Screen Effects/Backpack_2.png")
image Backpack 3 = VBox(HBox("Screen Effects/Backpack_1.png", "Screen Effects/Backpack_2.png"), "Screen Effects/Backpack_3.png")
image Backpack 4 = VBox(HBox("Screen Effects/Backpack_1.png", "Screen Effects/Backpack_2.png"), HBox("Screen Effects/Backpack_3.png", "Screen Effects/Backpack_4.png"))

# ==============================================================================
# Screen Effects - ATL
# ==============================================================================

# A short animation for TV static.
image static:
    alpha 0.35
    "Screen Effects/Static 1.png" with dissolve
    0.25
    "Screen Effects/Static 2.png" with dissolve
    0.25
    repeat

# Close a clapper board labeled "Take 1".
image take1:
    "Screen Effects/Take 1 Open.png"
    0.25
    "Screen Effects/Take 1 Closed.png" with dissolve
    0.5
    linear 0.75 alpha 0.0

# Close a clapper board labeled "Take 2".
image take2:
    "Screen Effects/Take 2 Open.png"
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
    0.5
    "Screen Effects/Projector 1.png" with Dissolve(0.5)
    0.5
    "Screen Effects/Projector 2.png" with Dissolve(0.5)
    0.5
    "Screen Effects/Projector 3.png" with Dissolve(0.5)

# Quick fade in/out with a black screen
image fadeInOut:
    "Screen Effects/Black.png"
    alpha 0.0
    linear 0.5 alpha 1.0
    0.25
    linear 0.5 alpha 0.0
