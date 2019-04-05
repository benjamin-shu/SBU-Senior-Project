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
define dark = -0.5

# Define new default Dissolve for transitions between sprites.
define dissolve = Dissolve(0.5)

# ==============================================================================
# Day Loop Control Variables
# ==============================================================================

# Counter and countdown for current day, with min and max values (i.e. days 1 - 10)
default day_num = 0
default countdown = 10
define day_min = 1
define day_max = 10
default i = 0

# List of Booleans for tracking player's choices on a given day.
default choices = [ False, False, False ]

# Counters for player's progress in each of the three skill trees.
default progress = [ 0, 0, 0 ]

# Codes for jump labels when showing progress sequences.
define codes = [ "ARS", "CSE", "HON" ]

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
        xpos 0.5
        xanchor 225
        yanchor 360

    transform center_l_stand():
        xpos 0.5
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
image composition_1:
    "images/0_ARS/composition_1.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1a.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1b.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1c.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1d.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1e.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1f.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1g.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1h.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1i.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1j.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1k.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/composition_1l.png" with Dissolve(0.5)
    0.5

image composition_2:
    "images/0_ARS/composition_2a.png" with Dissolve(1.0)
    1.5
    "images/0_ARS/composition_2b.png" with Dissolve(1.0)
    1.5
    "images/0_ARS/composition_2c.png" with Dissolve(1.0)
    1.5

# Typography Project
image typo_1:
    "images/0_ARS/typo_1a.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/typo_1b.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/typo_1c.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/typo_1d.png" with Dissolve(0.5)
    0.5

image typo_2:
    "images/0_ARS/typo_1d.png" with Dissolve(1.0)
    1.0
    "images/0_ARS/typo_2a.png" with Dissolve(1.0)
    1.0
    "images/0_ARS/typo_2b.png" with Dissolve(1.0)
    1.0
    "images/0_ARS/typo_2c.png" with Dissolve(1.0)
    1.0

# Poster Design Project
image poster_1:
    "images/0_ARS/poster_1a.png" with Dissolve(0.5)
    0.5
    "images/0_ARS/poster_1b.png" with Dissolve(0.5)
    0.5

image poster_2:
    "images/0_ARS/poster_1b.png" with Dissolve(0.75)
    0.75
    "images/0_ARS/poster_2a.png" with Dissolve(0.75)
    1.0
    "images/0_ARS/poster_2b.png" with Dissolve(0.75)
    0.75

image poster_3:
    "images/0_ARS/poster_2b.png" with Dissolve(0.75)
    0.75
    "images/0_ARS/poster_3a.png" with Dissolve(0.75)
    0.75
    "images/0_ARS/poster_3b.png" with Dissolve(0.75)
    0.75

# Video Editing Project
image video_1 = "images/0_ARS/video_1.png"

image video_2 = "images/0_ARS/video_2.png"

image video_3 = "images/0_ARS/video_3.png"
image video_3a:
    "images/0_ARS/video_3a.png" with Dissolve(0.5)
    0.75
    "images/0_ARS/video_3b.png" with Dissolve(0.5)
    0.75
    "images/0_ARS/video_3c.png" with Dissolve(0.5)
    0.75
    "images/0_ARS/video_3d.png" with Dissolve(0.5)
    0.75
    "images/0_ARS/video_3e.png" with Dissolve(0.5)
    0.75
    "images/0_ARS/video_3f.png" with Dissolve(0.5)
    0.75
    repeat

# ==============================================================================
# CSE Presentation Slides & Project Materials
# ==============================================================================

# Website Design Diagrams
image uml_1 = "images/1_CSE/uml_1.png"

image uml_2 = "images/1_CSE/uml_2.png"

# Page Designs in HTML
image html_1:
    "images/1_CSE/html_1a.png" with Dissolve(1.0)
    1.5
    "images/1_CSE/html_1b.png" with Dissolve(1.0)
    1.5
    "images/1_CSE/html_1c.png" with Dissolve(1.0)
    1.5
    "images/1_CSE/html_1d.png" with Dissolve(1.0)
    1.5

image html_2:
    "images/1_CSE/html_2a.png" with Dissolve(1.0)
    1.5
    "images/1_CSE/html_2b.png" with Dissolve(1.0)
    1.5
    "images/1_CSE/html_2c.png" with Dissolve(1.0)
    1.5

# Content Uploading
image content_1 = "images/1_CSE/content_1.png"

image content_2a = "images/1_CSE/html_1d.png"
image content_2b = "images/1_CSE/content_2.png"

image content_3:
    "images/1_CSE/content_3a.png" with Dissolve(0.5)
    0.5
    "images/1_CSE/content_3b.png" with Dissolve(0.5)
    0.5

# Website Deployment
image web_1 = "images/1_CSE/web_1.png"

image web_2 = "images/1_CSE/web_2.png"

image web_3 = "images/1_CSE/web_3.png"

# ==============================================================================
# HON Review Materials
# ==============================================================================

# Resume Review
image resume_1 = "images/2_HON/resume_1.png"

image resume_2 = "images/2_HON/resume_2.png"

# LinkedIn Profile
image linkedin_1 = "images/2_HON/linkedin_1.png"
image linkedin_1a = "images/2_HON/linkedin_1a.png"
image linkedin_1b = "images/2_HON/linkedin_1b.png"
image linkedin_1c:
    "images/2_HON/linkedin_1c.png" with Dissolve(0.5)
    0.5
    "images/2_HON/linkedin_1d.png" with Dissolve(0.5)
    0.5

image linkedin_2a = "images/2_HON/linkedin_2a.png"
image linkedin_2b:
    "images/2_HON/linkedin_2b.png" with Dissolve(0.5)
    0.5
    "images/2_HON/linkedin_2c.png" with Dissolve(0.5)
    0.5

# Presentation Prep
image present_1a = "images/2_HON/present_1a.png"
image present_1b = "images/2_HON/present_1b.png"

image present_2:
    "images/2_HON/present_2a.png" with Dissolve(0.5)
    0.5
    "images/2_HON/present_2b.png" with Dissolve(0.5)
    0.5
    repeat

image present_3 = "images/2_HON/present_3.png"

# Interview Prep
image interview_1a = "images/2_HON/interview_1a.png"
image interview_1b = "images/2_HON/interview_1b.png"
image interview_1c = "images/2_HON/interview_1c.png"

image interview_2 = "images/2_HON/interview_2.png"

image interview_3a = "images/2_HON/interview_3a.png"
image interview_3b = "images/2_HON/interview_3b.png"
image interview_3c = "images/2_HON/interview_3c.png"

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
    0.5
    linear 0.5 alpha 0.0
