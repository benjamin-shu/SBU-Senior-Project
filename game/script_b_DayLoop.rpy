label day_start:
    if (day_num == 0):
        scene West F 301C with fade
        B "Well, I was definitely not ready for that call!"
        B "I need to start preparing {b}{i}now{/i}{/b} - between classes and homework, I'm not going to have much time."
        B "And starting now, the clock is ticking."
        show Dimmed with dissolve
    elif (day_num == 10 and countdown == 0):
        jump interview
    else:
        scene West F 301C
        B "Just [countdown] days left until the interview."
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
            $ renpy.jump("%s_sequences" % (codes[i]))
        else:
            $ i += 1

    scene West F 301C with fade

    # Update skill counters for choice screen.
    $ day_countARS = progress[0]
    $ day_countCSE = progress[1]
    $ day_countHON = progress[2]

    # Reset choice button controls.
    $ day_buttonARS = False
    $ day_buttonCSE = False
    $ day_buttonHON = False

    $ i = 0
    while i < len(choices):
        $ choices[i] = False
        $ i += 1

    # Update day_num and countdown counters.
    $ day_num += 1
    $ countdown -= 1

    jump day_start
