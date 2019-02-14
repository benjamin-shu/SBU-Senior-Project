# ==============================================================================
# Weekly Loop Start
# ==============================================================================
label schedule_show:
    # Set scene at Ben's apartment.
    scene West F 301C with fade
    show Dimmed with dissolve

    # If current week is a project deadline, save current progress on that project.
    if (week_num in ARS_deadlines):
        $ ARS_scores[ARS_deadlines[week_num]] = ARS_progress
        $ ARS_progress = 0
    if (week_num in CSE_deadlines):
        $ CSE_scores[CSE_deadlines[week_num]] = CSE_progress
        $ CSE_progress = 0
    if (week_num in HON_deadlines):
        $ HON_scores[HON_deadlines[week_num]] = HON_progress
        $ HON_progress = 0

    # Go over weekly reminders of project due dates.
    $ reminder = ARS_reminders[week_num]
    B "{i}[reminder]{/i}"
    $ reminder = CSE_reminders[week_num]
    B "{i}[reminder]{/i}"
    $ reminder = HON_reminders[week_num]
    B "{i}[reminder]{/i}"

    # Show schedule planner.
    window hide
    show schedule_img with dissolve

label schedule_screen:
    # Call schedule() screen to take player input.
    call screen schedule
    $ renpy.pause()

label schedule_check:
    # If player hasn't selected something for all slots, jump back to schedule screen.
    if (L_img == "Schedule/L Placeholder.png" or M_img == "Schedule/M Placeholder.png" or R_img == "Schedule/R Placeholder.png"):
        B "I haven't filled out the schedule yet - I should add something to each slot."
        jump schedule_screen

    # Add to act_cnt[] based on player's choices.
    $ act_cnt[L_src.index(L_img)] += 1
    $ act_cnt[M_src.index(M_img)] += 1
    $ act_cnt[R_src.index(R_img)] += 1
    "[act_cnt]"

    # If player has put too many points into any activity,
    # or already completed an activity, set valid_schedule to False.
    if (ARS_progress >= ARS_max):
        "ARS Progress: [ARS_progress], Max: [ARS_max]"
        $ reminder = ARS_completed[week_num]
        B "[reminder]"
        $ valid_schedule = False
    elif (ARS_progress + act_cnt[0]) > ARS_max:
        "ARS Progress: [ARS_progress], Max: [ARS_max]"
        $ reminder = ARS_overflow[week_num]
        B "[reminder]"
        $ valid_schedule = False
    if (CSE_progress >= CSE_max):
        "CSE Progress: [CSE_progress], Max: [CSE_max]"
        $ reminder = CSE_completed[week_num]
        B "[reminder]"
        $ valid_schedule = False
    elif (CSE_progress + act_cnt[1]) > CSE_max:
        "CSE Progress: [CSE_progress], Max: [CSE_max]"
        $ reminder = CSE_overflow[week_num]
        B "[reminder]"
        $ valid_schedule = False
    if (HON_progress + act_cnt[2]) > HON_max:
        "HON Progress: [HON_progress], Max: [HON_max]"
        B "Done with studying."

    # If planned schedule is not valid, jump back to schedule screen.
    if (not valid_schedule):
        $ act_cnt = [ 0, 0, 0, 0]
        jump schedule_screen

    "Week [week_num]"
    "Checking progress so far."
    "ARS Progress: [ARS_progress]"
    "CSE Progress: [CSE_progress]"
    "HON Progress: [HON_progress]"

label week_phase_0:
    # Set scene for ARS classes at eMedia.
    hide Dimmed with dissolve
    scene eMedia Seats with fade
    show Dimmed with dissolve
    $ renpy.pause()

    if (code_A in L_img):
        $ week_dict = ARS_deadlines
        $ week_act = code_A
        $ ARS_progress += 1
    elif (code_C in L_img):
        $ week_dict = CSE_deadlines
        $ week_act = code_C
        $ CSE_progress += 1
    elif (code_S in L_img):
        $ week_dict = HON_deadlines
        $ week_act = code_S
        $ HON_progress += 1

    $ week_cnt = week_num + 1
    $ week_proj = ""

    while week_cnt < 16:
        if (week_cnt in week_dict):
            $ week_proj = week_dict[week_cnt]
            jump week_phase_0_act
        else:
            $ week_cnt += 1

label week_phase_0_act:
    if (week_proj != ""):
        $ renpy.jump("%s_%s" % (week_act, week_proj))

    # $ renpy.jump("Week_%d" % week_num)

label week_phase_1:
    # Set scene for CSE classes at Javits.
    hide Dimmed with dissolve
    scene Javits Seats with fade
    show Dimmed with dissolve
    $ renpy.pause()

    if (code_A in L_img):
        $ week_dict = ARS_deadlines
        $ week_act = code_A
        $ ARS_progress += 1
    elif (code_C in L_img):
        $ week_dict = CSE_deadlines
        $ week_act = code_C
        $ CSE_progress += 1
    elif (code_S in L_img):
        $ week_dict = HON_deadlines
        $ week_act = code_S
        $ HON_progress += 1

    $ week_cnt = week_num + 1
    $ week_proj = ""

    while week_cnt < 16:
        if (week_cnt in week_dict):
            $ week_proj = week_dict[week_cnt]
            jump week_phase_1_act
        else:
            $ week_cnt += 1

label week_phase_1_act:
    if (week_proj != ""):
        $ renpy.jump("%s_%s" % (week_act, week_proj))

label week_phase_2:
    # Set scene for free time at West F 301C.
    hide Dimmed with dissolve
    scene West F 301C with fade
    show Dimmed with dissolve
    $ renpy.pause()

    if (code_A in L_img):
        $ week_dict = ARS_deadlines
        $ week_act = code_A
        $ ARS_progress += 1
    elif (code_C in L_img):
        $ week_dict = CSE_deadlines
        $ week_act = code_C
        $ CSE_progress += 1
    elif (code_S in L_img):
        $ week_dict = HON_deadlines
        $ week_act = code_S
        $ HON_progress += 1

    $ week_cnt = week_num + 1
    $ week_proj = ""

    while week_cnt < 16:
        if (week_cnt in week_dict):
            $ week_proj = week_dict[week_cnt]
            jump week_phase_2_act
        else:
            $ week_cnt += 1

label week_phase_2_act:
    if (week_proj != ""):
        $ renpy.jump("%s_%s" % (week_act, week_proj))

label week_end:
    # Reset schedule planner for next week.
    $ L_img = "Schedule/L Placeholder.png"
    $ L_ind = 0
    $ M_img = "Schedule/M Placeholder.png"
    $ M_ind = 0
    $ R_img = "Schedule/R Placeholder.png"
    $ R_ind = 0

    # Reset phase counter for next week.
    $ phase = 0

    # Reset act_cnt[] to take input for next week.
    $ act_cnt = [ 0, 0, 0, 0]
    $ ARS_max = ARS_caps[week_num]
    $ CSE_max = CSE_caps[week_num]

    # Increment week counter.
    $ week_num += 1
    "[week_num]"

    # Jump back to schedule planner if semester is not over.
    if week_num < 14:
        jump schedule_show
