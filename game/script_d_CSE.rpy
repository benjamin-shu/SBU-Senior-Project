label CSE_sequences:
    # Retrieve index for CSE data using codes[].
    default CSE_index = codes.index("CSE")
    # Retrive player's current progress in this skill tree.
    default CSE_progress = progress[CSE_index]

    # Set scene in Javits 100.
    scene Javits Screen with fade
    show Dimmed with dissolve

    $ renpy.jump("CSE_sequences_%d" % (CSE_progress))

label CSE_sequences_1:
    show projector_emedia with dissolve
    i += 1
    jump show_skills

label CSE_sequences_2:
    i += 1
    jump show_skills

label CSE_sequences_3:
    i += 1
    jump show_skills

label CSE_sequences_4:
    i += 1
    jump show_skills

label CSE_sequences_5:
    i += 1
    jump show_skills

label CSE_sequences_6:
    i += 1
    jump show_skills

label CSE_sequences_7:
    i += 1
    jump show_skills

label CSE_sequences_8:
    i += 1
    jump show_skills

label CSE_sequences_9:
    i += 1
    jump show_skills

label CSE_sequences_10:
    i += 1
    jump show_skills
