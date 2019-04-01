label ARS_sequences:
    # Retrieve index for ARS data using codes[].
    default ARS_index = codes.index("ARS")
    # Retrieve player's current progress in this skill tree.
    default ARS_progress = progress[ARS_index]

    # Set scene in Staller's eMedia SINC site.
    scene eMedia Screen with fade
    show Dimmed with dissolve

    $ renpy.jump("ARS_sequences_%d" % (ARS_progress))

label ARS_sequences_1:
    show projector_emedia with dissolve
    i += 1
    jump show_skills

label ARS_sequences_2:
    i += 1
    jump show_skills

label ARS_sequences_3:
    i += 1
    jump show_skills

label ARS_sequences_4:
    i += 1
    jump show_skills

label ARS_sequences_5:
    i += 1
    jump show_skills

label ARS_sequences_6:
    i += 1
    jump show_skills

label ARS_sequences_7:
    i += 1
    jump show_skills

label ARS_sequences_8:
    i += 1
    jump show_skills

label ARS_sequences_9:
    i += 1
    jump show_skills

label ARS_sequences_10:
    i += 1
    jump show_skills
