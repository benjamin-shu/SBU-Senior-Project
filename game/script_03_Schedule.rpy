# ==========================================================================
# Integer counters used to track the player's progress in various areas.
# ==========================================================================

# Current week in the semester.
default week_num = 0

# Progress counters for the different ARS projects.
default ARS_principles = 0
default ARS_shapes = 0
default ARS_typography = 0
default ARS_poster = 0
default ARS_video = 0

# Progress counters for the different CSE projects.
default CSE_uml = 0
default CSE_srs = 0
default CSE_phase1 = 0
default CSE_phase2 = 0
default CSE_phase3 = 0

# Progress counters for the three CS midterms.
default CSE_study1 = 0
default CSE_study2 = 0
default CSE_study3 = 0

# Progress counters for non-class-related activities.
default resume = 0
default portfolio = 0

# Boolean flag for whether or not the player's schedule is valid.
default valid_schedule = True

# Progress counters for current available activities.
default ARS_progress = 0
default CSE_progress = 0
default HON_progress = 0

# Maximum point caps for each week of the game.
default ARS_max = [ 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4 ]
default CSE_max = [ 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4 ]
default HON_max = 4

# ==========================================================================
# Control Variables For schedule() Screen.
# ==========================================================================

# Int counter to track current phase of the week.
default phase = 0

# Image array for the clock's left slot.
default L_src = [ "Schedule/L ARS.png", "Schedule/L CSE.png", "Schedule/L Study.png" ]
# File path for currently displayed image left slots.
default L_img = "Schedule/L Placeholder.png"
# Index of current image in L_src[].
default L_ind = 0

# Image array for the clock's center slot.
default M_src = [ "Schedule/M ARS.png", "Schedule/M CSE.png", "Schedule/M Study.png" ]
# File path for currently-displayed image in center slot.
default M_img = "Schedule/M Placeholder.png"
# Index of current image in M_src[].
default M_ind = 0

# Image array for the clock's right slot.
default R_src = [ "Schedule/R ARS.png", "Schedule/R CSE.png", "Schedule/R Study.png" ]
# File path for currently-displayed image in right slot.
default R_img = "Schedule/R Placeholder.png"
# Index of current image in R_src[].
default R_ind = 0

# Array of integers to be checked when the player confirms their schedule.
# Should be checked against current progress counters to avoid going over the limit for a project/activity.
define act_cnt = [ 0, 0, 0, 0 ]

# A composite image for the clock itself.
# Note that it uses the L_img, M_img, and R_img file paths.
image schedule_img = Composite(
    (1280, 720),
    (0, 0), "Schedule/Clock Back.png",
    (0, 0), "Schedule/Sleep Slot.png",
    (0, 0), "[L_img]",
    (0, 0), "[M_img]",
    (0, 0), "[R_img]",
    (0, 0), "Schedule/Clock Face.png")

# Screen definition for the interactive buttons that the player uses.
# Each section on the clock has a button which toggles through the different activities.
# There is also a "Continue" button included to confirm a schedule.
# For smooth transitions, make sure to use "show schedule_img" first!
screen schedule():
    modal True

    imagebutton:
        focus_mask True
        idle "Schedule/L Idle.png"
        hover "Schedule/L Hover.png"
        action [SetVariable("L_ind", ((L_ind + 1) % len(L_src))), SetVariable("L_img", L_src[L_ind])]

    imagebutton:
        focus_mask True
        idle "Schedule/M Idle.png"
        hover "Schedule/M Hover.png"
        action [SetVariable("M_ind", ((M_ind + 1) % len(M_src))), SetVariable("M_img", M_src[M_ind])]

    imagebutton:
        focus_mask True
        idle "Schedule/R Idle.png"
        hover "Schedule/R Hover.png"
        action [SetVariable("R_ind", ((R_ind + 1) % len(R_src))), SetVariable("R_img", R_src[R_ind])]

    imagebutton:
        focus_mask True
        pos (551, 626)
        idle "Schedule/Continue Idle.png"
        hover "Schedule/Continue Hover.png"
        action [SetVariable("valid_schedule", True), Jump("check_schedule")]
