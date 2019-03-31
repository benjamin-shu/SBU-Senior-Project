# ==============================================================================
# Ren'Py Object Definitions
# ==============================================================================
define b_name = "Ben"
define B = DynamicCharacter("b_name", image="Ben", who_color="#71B7E2", who_bold=True,
    what_Size=30, what_Bold=False, what_font="fonts/Courier Prime Bold.ttf")

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

# ==============================================================================
# ARS Project Materials
# ==============================================================================

# Compositional Elements Presentation

# Typography Project

# Poster Design Project

# Video Editing Project

# ==============================================================================
# CSE Presentation Slides & Project Materials
# ==============================================================================

# Website Design Diagrams

# Page Designs in HTML

# Content Uploading

# Website Deployment

# ==============================================================================
# HON Review Materials
# ==============================================================================

# Resume Review

# LinkedIn Profile

# Presentation Prep

# Interview Prep

# ==============================================================================
# Background Art
# ==============================================================================

# West Apartments
image West F 301 Hallway = "Backgrounds/West F 301 Hallway 1.png"
image West F 301C = "Backgrounds/West F 301C.png"
image West F 301C Door = "Backgrounds/West F 301C Door.png"

# Javits Lecture Hall
image Javits Front Door = "Backgrounds/Javits Front Door.png"
image Javits Seats = "Backgrounds/Javits Seats.png"
image Javits Screen = "Backgrounds/Javits Screen.png"

# Staller Center for the Arts
image Staller = "Backgrounds/Staller.png"
image Staller Music = "Backgrounds/Staller Music.png"
image eMedia Seats = "Backgrounds/eMedia Seats.png"
image eMedia Screen = "Backgrounds/eMedia Screen.png"

# Interview Background

# ==============================================================================
# Screen Effects - Images
# ==============================================================================

# A simple black screen.
image Black = "Screen Effects/Black.png"

# Dimming effect for the entire screen.
image Dimmed = "Screen Effects/Dimmed.png"

# Image used to show Ben using his laptop.
image Laptop = "Screen Effects/Laptop.png"

# ==============================================================================
# Screen Effects - ATL
# ==============================================================================

# Turn on a projector screen in current scene.
image projector_emedia:
    "Screen Effects/Projector 0.png" with Dissolve(0.5)
    0.5
    "Screen Effects/Projector 1.png" with Dissolve(0.5)
    0.5
    "Screen Effects/Projector 2.png" with Dissolve(0.5)
    0.5
    "Screen Effects/Projector 3.png" with Dissolve(0.5)

# Turn on the projector in Javits 100.
image projector_javits:
    "Screen Effects/Javits Screen Projector 1.png" with Dissolve(0.5)
    0.5
    "Screen Effects/Javits Screen Projector 2.png" with Dissolve(0.5)
    0.5
    "Screen Effects/Javits Screen Projector 3.png" with Dissolve(0.5)
    0.5

# Quick fade in/out with a black screen
image fadeInOut:
    "Screen Effects/Black.png"
    alpha 0.0
    linear 0.5 alpha 1.0
    0.25
    linear 0.5 alpha 0.0
