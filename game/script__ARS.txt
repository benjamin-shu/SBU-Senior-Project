label ARS_composition:
    if (ARS_progress == 1):
        show Dimmed with dissolve
        show Composition Canvas with dissolve
        show Composition Point01 with dissolve
        show Composition Point02 with dissolve
        show Composition Depth01 with dissolve
        show Composition Depth02 with dissolve
        show Composition Shape01 with dissolve
        show Composition Shape02 with dissolve

        B "I like the way these look right now, but I should probably add some more detail later."

        hide Composition
        hide Dimmed
        with dissolve
    elif (ARS_progress == 2):
        show Dimmed with dissolve
        show Composition Point02 with dissolve
        #show Composition Point03 with dissolve
        show Composition Point04 with dissolve
        show Composition Point05 with dissolve

        show Composition Depth02 with dissolve
        show Composition Depth03 with dissolve
        show Composition Depth04 with dissolve
        show Composition Depth05 with dissolve
        $ renpy.pause()
        #show Composition Shape03 with dissolve
        show Composition Shape04 with dissolve
        show Composition Shape05 with dissolve
        show Composition Shape06 with dissolve
        $ renpy.pause()

        hide Composition
        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label ARS_shapes:
    if (ARS_progress == 1):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve
    elif (ARS_progress == 2):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label ARS_typography:
    if (ARS_progress == 1):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve
    elif (ARS_progress == 2):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label ARS_poster:
    if (ARS_progress == 1):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve
    elif (ARS_progress == 2):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve
    elif (ARS_progress == 3):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve
    elif (ARS_progress == 4):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label ARS_video:
    if (ARS_progress == 1):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve
    elif (ARS_progress == 2):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve
    elif (ARS_progress == 3):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve
    elif (ARS_progress == 4):
        show Dimmed with dissolve

        $ renpy.pause()

        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end
