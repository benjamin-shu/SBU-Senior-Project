# ==============================================================================
# Weekly Loop Start
# ==============================================================================
label schedule_show:
    # Set scene at Ben's apartment.
    scene West F 301C with fade
    show Dimmed with dissolve

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

    # Add to progress counters for each activity.
    $ ARS_progress += act_cnt[0]
    $ CSE_progress += act_cnt[1]
    $ HON_progress += act_cnt[2]

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

    # $ renpy.jump("Week_%d" % week_num)

label week_phase_1:
    # Set scene for CSE classes at Javits.
    hide Dimmed with dissolve
    scene Javits Seats with fade
    show Dimmed with dissolve

label week_phase_2:
    # Set scene for free time at West F 301C.
    hide Dimmed with dissolve
    scene West F 301C with fade
    show Dimmed with dissolve

    # Reset schedule planner for next week.
    $ L_img = "Schedule/L Placeholder.png"
    $ L_ind = 0
    $ M_img = "Schedule/M Placeholder.png"
    $ M_ind = 0
    $ R_img = "Schedule/R Placeholder.png"
    $ R_ind = 0

    # Reset act_cnt[] to take input for next week.
    $ act_cnt = [ 0, 0, 0, 0]
    $ ARS_max = ARS_caps[week_num]
    $ CSE_max = CSE_caps[week_num]

    # Increment week counter.
    $ week_num += 1
    "[week_num]"

    # If next week is a project deadline, save current progress on that project.
    if (week_num in ARS_deadlines):
        $ ARS_scores[ARS_deadlines[week_num]] = ARS_progress
        $ ARS_progress = 0
    if (week_num in CSE_deadlines):
        $ CSE_scores[CSE_deadlines[week_num]] = CSE_progress
        $ CSE_progress = 0
    if (week_num in HON_deadlines):
        $ HON_scores[HON_deadlines[week_num]] = HON_progress
        $ HON_progress = 0

    # Jump back to schedule planner if semester is not over.
    if week_num < 14:
        jump schedule_show
