label HON_sequences:
    # Retrieve index for HON data using codes[].
    default HON_index = codes.index("HON")
    # Retrive player's current progress in this skill tree.
    default HON_progress = progress[HON_index]

    # Set scene in West F 301C.
    scene West F 301C with fade
    show Dimmed with dissolve

    $ renpy.jump("HON_sequences_%d" % (HON_progress))

label HON_sequences_1:
    show projector_emedia with dissolve
    i += 1
    jump show_skills

label HON_sequences_2:
    i += 1
    jump show_skills

label HON_sequences_3:
    i += 1
    jump show_skills

label HON_sequences_4:
    i += 1
    jump show_skills

label HON_sequences_5:
    i += 1
    jump show_skills

label HON_sequences_6:
    i += 1
    jump show_skills

label HON_sequences_7:
    i += 1
    jump show_skills

label HON_sequences_8:
    i += 1
    jump show_skills

label HON_sequences_9:
    i += 1
    jump show_skills

label HON_sequences_10:
    i += 1
    jump show_skills
