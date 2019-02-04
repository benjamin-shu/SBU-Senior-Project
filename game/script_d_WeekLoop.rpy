# ==============================================================================
# Integer counters used to track the player's progress in various areas.
# ==============================================================================

# Current week in the semester.
default week_num = 1

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

# Progress counters for current available activities, and their point caps.
default ARS_progress = 0
default ARS_max = 1

default CSE_progress = 0
default CSE_max = 1

default HON_progress = 0
default HON_max = 4

# ==============================================================================
# Control variables for the schedule() screen.
# ==============================================================================

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


label screen_schedule:
    window hide
    show schedule_img

    call screen schedule
    $ renpy.pause()

label check_schedule:
    $ act_cnt[L_src.index(L_img)] += 1
    $ act_cnt[M_src.index(M_img)] += 1
    $ act_cnt[R_src.index(R_img)] += 1
    "[act_cnt]"

    if (ARS_progress + act_cnt[0]) > ARS_max:
        "ARS Progress: [ARS_progress], Max: [ARS_max]"
        B "I'm already finished with that project."
        $ valid_schedule = False

    if (CSE_progress + act_cnt[1]) > CSE_max:
        "CSE Progress: [CSE_progress], Max: [CSE_max]"
        B "I'm done with that project."
        $ valid_schedule = False

    if (HON_progress + act_cnt[2]) > HON_max:
        "HON Progress: [HON_progress], Max: [HON_max]"
        B "Done with studying."
        $ valid_schedule = False

    if (not valid_schedule):
        "[act_cnt]"
        $ act_cnt = [ 0, 0, 0, 0 ]
        "[act_cnt]"
        jump screen_schedule

    $ ARS_progress += act_cnt[0]
    $ CSE_progress += act_cnt[1]
    $ HON_progress += act_cnt[2]

    "Week [week_num]"
    "Checking progress so far."
    "ARS Progress: [ARS_progress], Max: [ARS_max]"
    "CSE Progress: [CSE_progress], Max: [CSE_max]"
    "HON Progress: [HON_progress], Max: [HON_max]"

    $ act_cnt = [ 0, 0, 0, 0]

    $ week_num += 1

    jump screen_schedule

label menu_morning:
    if week_num == 3:
        "Principles of Design: [ARS_principles]"

    elif week_num == 5:
        "Shapes: [ARS_shapes]"

    elif week_num == 7:
        "Typography: [ARS_typography]"

    elif week_num == 11:
        "Poster: [ARS_poster]"

    if week_num > 0 and week_num < 15:
        menu:
            "Work on the Principles of Design project." if week_num >= 1 and week_num <= 2:
                if ARS_principles < 2:
                    $ ARS_principles = ARS_principles + 1

            "Work on the Shapes project." if week_num >= 3 and week_num <= 4:
                if ARS_shapes < 2:
                    $ ARS_shapes = ARS_shapes + 1

            "Work on the Typography project." if week_num >= 5 and week_num <= 6:
                if ARS_typography < 2:
                    $ ARS_typography = ARS_typography + 1

            "Work on the Poster project." if week_num >= 7 and week_num <= 10:
                if ARS_poster < 4:
                    $ ARS_poster = ARS_poster + 1

            "Work on the \"Self-Portrait\" video project." if week_num >= 11 and week_num <= 14:
                $ ARS_video = ARS_video + 1

            "Work on UML diagram for CSE 308." if week_num >= 1 and week_num <= 2:
                $ CSE_uml = CSE_uml + 1

            "Work on SRS document for CSE 308." if week_num >= 3 and week_num <= 4:
                $ CSE_srs = CSE_srs + 1

            "Work on Phase 1 project goals for CSE 308." if week_num >= 5 and week_num <= 7:
                $ CSE_phase1 = CSE_phase1 + 1

            "Work on Phase 2 project goals for CSE 308." if week_num >= 8 and week_num <= 10:
                $ CSE_phase2 = CSE_phase2 + 1

            "Work on Phase 3 project goals for CSE 308." if week_num >= 11 and week_num <= 14:
                $ CSE_phase3 = CSE_phase3 + 1

            "Review CSE course material." if week_num >= 1 and week_num <= 2:
                $ CSE_study1 = CSE_study1 + 1

            "Prepare for the first round of CSE midterms." if week_num >= 3 and week_num <= 4:
                $ CSE_study1 = CSE_study1 + 1

            "Review material from the first round of CSE midterms." if week_num >= 6 and week_num <= 14:
                $ CSE_study1 = CSE_study1 + 1

            "Prepare for the second round of CSE midterms." if week_num >= 6 and week_num <= 9:
                $ CSE_study2 = CSE_study2 + 1

            "Review material from the second round of CSE midterms." if week_num >= 11 and week_num <= 14:
                $ CSE_study2 = CSE_study2 + 1

            "Prepare for the CSE final exams." if week_num >= 11 and week_num <= 14:
                $ CSE_study3 = CSE_study3 + 1

label menu_afternoon:
    if week_num == 3:
        "UML Diagram: [CSE_uml]"

    elif week_num == 5:
        "SRS Document: [CSE_srs]"
        "Midterm 1: [CSE_study1]"

    elif week_num == 8:
        "CSE 308 Phase 1: [CSE_phase1]"

    elif week_num == 10:
        "Midterm 2: [CSE_study2]"

    elif week_num == 11:
        "CSE 308 Phase 2: [CSE_phase2]"

    elif week_num > 0 and week_num < 15:
        menu:
            "Work on the Principles of Design project." if week_num >= 1 and week_num <= 2:
                $ ARS_principles = ARS_principles + 1

            "Work on the Shapes project." if week_num >= 3 and week_num <= 4:
                $ ARS_shapes = ARS_shapes + 1

            "Work on the Typography project." if week_num >= 5 and week_num <= 6:
                $ ARS_typography = ARS_typography + 1

            "Work on the Poster project." if week_num >= 7 and week_num <= 10:
                $ ARS_poster = ARS_poster + 1

            "Work on the \"Self-Portrait\" video project." if week_num >= 11 and week_num <= 14:
                $ ARS_video = ARS_video + 1

            "Work on UML diagram for CSE 308." if week_num >= 1 and week_num <= 2:
                $ CSE_uml = CSE_uml + 1

            "Work on SRS document for CSE 308." if week_num >= 3 and week_num <= 4:
                $ CSE_srs = CSE_srs + 1

            "Work on Phase 1 project goals for CSE 308." if week_num >= 5 and week_num <= 7:
                $ CSE_phase1 = CSE_phase1 + 1

            "Work on Phase 2 project goals for CSE 308." if week_num >= 8 and week_num <= 10:
                $ CSE_phase2 = CSE_phase2 + 1

            "Work on Phase 3 project goals for CSE 308." if week_num >= 11 and week_num <= 14:
                $ CSE_phase3 = CSE_phase3 + 1

            "Review CSE course material." if week_num >= 1 and week_num <= 2:
                $ CSE_study1 = CSE_study1 + 1

            "Prepare for the first round of CSE midterms." if week_num >= 3 and week_num <= 4:
                $ CSE_study1 = CSE_study1 + 1

            "Review material from the first round of CSE midterms." if week_num >= 6 and week_num <= 14:
                $ CSE_study1 = CSE_study1 + 1

            "Prepare for the second round of CSE midterms." if week_num >= 6 and week_num <= 9:
                $ CSE_study2 = CSE_study2 + 1

            "Review material from the second round of CSE midterms." if week_num >= 11 and week_num <= 14:
                $ CSE_study2 = CSE_study2 + 1

            "Prepare for the CSE final exams." if week_num >= 11 and week_num <= 14:
                $ CSE_study3 = CSE_study3 + 1

label menu_night:
    if week_num > 0 and week_num < 15:
        menu:
            "Work on the Principles of Design project." if week_num >= 1 and week_num <= 2:
                $ ARS_principles = ARS_principles + 1

            "Work on the Shapes project." if week_num >= 3 and week_num <= 4:
                $ ARS_shapes = ARS_shapes + 1

            "Work on the Typography project." if week_num >= 5 and week_num <= 6:
                $ ARS_typography = ARS_typography + 1

            "Work on the Poster project." if week_num >= 7 and week_num <= 10:
                $ ARS_poster = ARS_poster + 1

            "Work on the \"Self-Portrait\" video project." if week_num >= 11 and week_num <= 14:
                $ ARS_video = ARS_video + 1

            "Work on UML diagram for CSE 308." if week_num >= 1 and week_num <= 2:
                $ CSE_uml = CSE_uml + 1

            "Work on SRS document for CSE 308." if week_num >= 3 and week_num <= 4:
                $ CSE_srs = CSE_srs + 1

            "Work on Phase 1 project goals for CSE 308." if week_num >= 5 and week_num <= 7:
                $ CSE_phase1 = CSE_phase1 + 1

            "Work on Phase 2 project goals for CSE 308." if week_num >= 8 and week_num <= 10:
                $ CSE_phase2 = CSE_phase2 + 1

            "Work on Phase 3 project goals for CSE 308." if week_num >= 11 and week_num <= 14:
                $ CSE_phase3 = CSE_phase3 + 1

            "Review CSE course material." if week_num >= 1 and week_num <= 3:
                $ CSE_study1 = CSE_study1 + 1

            "Prepare for the first round of CSE midterms." if week_num >= 3 and week_num <= 4:
                $ CSE_study1 = CSE_study1 + 1

            "Review material from the first round of CSE midterms." if week_num >= 6 and week_num <= 14:
                $ CSE_study1 = CSE_study1 + 1

            "Prepare for the second round of CSE midterms." if week_num >= 6 and week_num <= 9:
                $ CSE_study2 = CSE_study2 + 1

            "Review material from the second round of CSE midterms." if week_num >= 11 and week_num <= 14:
                $ CSE_study2 = CSE_study2 + 1

            "Prepare for the CSE final exams." if week_num >= 11 and week_num <= 14:
                $ CSE_study3 = CSE_study3 + 1

label week_end:
    $ week_num = week_num + 1

    if week_num < 15:
        jump start

label End:
    return
