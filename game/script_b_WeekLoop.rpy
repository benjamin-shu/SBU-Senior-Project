# ==============================================================================
# Weekly Loop Start
# ==============================================================================
label schedule_show:
    scene West F 301C with fade
    show Dimmed with dissolve

    $ reminder = ARS_reminders[week_num]
    B "{i}[reminder]{/i}"
    $ reminder = CSE_reminders[week_num]
    B "{i}[reminder]{/i}"
    $ reminder = HON_reminders[week_num]
    B "{i}[reminder]{/i}"

label schedule_screen:
    window hide
    show schedule_img with dissolve

    call screen schedule
    $ renpy.pause()

label schedule_check:
    $ act_cnt[L_src.index(L_img)] += 1
    $ act_cnt[M_src.index(M_img)] += 1
    $ act_cnt[R_src.index(R_img)] += 1
    "[act_cnt]"

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

    if (not valid_schedule):
        $ act_cnt = [ 0, 0, 0, 0]
        jump schedule_screen

    $ ARS_progress += act_cnt[0]
    $ CSE_progress += act_cnt[1]
    $ HON_progress += act_cnt[2]

    "Week [week_num]"
    "Checking progress so far."
    "ARS Progress: [ARS_progress]"
    "CSE Progress: [CSE_progress]"
    "HON Progress: [HON_progress]"

label week_phase_0:
    # $ renpy.jump("Week_%d" % week_num)

label week_phase_1:

label week_phase_2:
    $ L_img = "Schedule/L Placeholder.png"
    $ L_ind = 0
    $ M_img = "Schedule/M Placeholder.png"
    $ M_ind = 0
    $ R_img = "Schedule/R Placeholder.png"
    $ R_ind = 0

    $ act_cnt = [ 0, 0, 0, 0]
    $ ARS_max = ARS_caps[week_num]
    $ CSE_max = CSE_caps[week_num]

    $ week_num += 1
    "[week_num]"

    if (week_num in ARS_deadlines):
        $ renpy.setValue("ARS_%s" % ARS_deadlines[week_num], ARS_progress)
        $ ARS_progress = 0

    if (week_num in CSE_deadlines):
        $ renpy.set("CSE_%s" % CSE_deadlines[week_num], CSE_progress)
        $ CSE_progress = 0

    if (week_num in HON_deadlines):
        $ renpy.set("HON_%s" % HON_deadlines[week_num], HON_progress)
        $ HON_progress = 0

    "[ARS_composition]"

    if week_num < 14:
        jump schedule_show
