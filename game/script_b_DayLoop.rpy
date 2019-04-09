label day_start:
    if (day_num < 0 and day_num > 11):
        "Error with counter."
        return
    elif (countdown > 10 or countdown < 1):
        "Error with countdown."
        return
    else:
        scene West F 301C
        B "[countdown] days left until the interview."
        show Dimmed with dissolve

label choose_skills:
        # Prompt player to choose two of three skill trees.
        call screen day_actions
        $ renpy.pause()

label check_skills:
    # Load player's choices into choices[]
    $ choices[0] = day_buttonARS
    $ choices[1] = day_buttonCSE
    $ choices[2] = day_buttonHON

    # Check that player has not somehow picked 0 or 3 skills.
    if (choices[0] and choices[1] and choices[2]):
        "Invalid combination! (1)"
        return
    elif (not choices[0]) and (not choices[1]) and (not choices[2]):
        "Invalid combination! (2)"
        return

    # Check that player has not already completed one of the selected trees.
    $ i = 0
    while i < len(choices):
        if (choices[i] and progress[i] == day_max):
            "Tree is already done."
            jump choose_skills
        else:
            $ i += 1

    # Using player's choices, increment skill counters and jump.
    $ i = 0

label show_skills:
    while i < len(choices):
        if (choices[i]):
            $ progress[i] += 1
            "[progress]"
            $ renpy.jump("%s_sequences" % (codes[i]))
        else:
            $ i += 1

    jump day_start
