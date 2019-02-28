label CSE_uml:
    if (CSE_progress == 1):
        show Dimmed
        show Laptop
        show Violet UML
        with dissolve

        show UML Diagram MetroMap 01 with dissolve
        show UML Diagram MetroMap 02 with dissolve
        show UML Diagram MetroStation 01 with dissolve
        show UML Diagram MetroStation 02 with dissolve
        show UML Diagram MetroLine 01 with dissolve
        show UML Diagram MetroLine 02 with dissolve
        show UML Diagram Combined 01 with dissolve
        $ renpy.pause()

        hide UML Diagram
        hide Laptop
        hide Dimmed
        hide Violet UML
        with dissolve

    elif (CSE_progress == 2):
        show Dimmed
        show Laptop
        show Violet UML
        with dissolve

        show UML Diagram Combined 02 with dissolve
        show UML Diagram Combined 03 with dissolve
        show UML Diagram Combined 04 with dissolve
        show UML Diagram Combined 05 with dissolve
        $ renpy.pause()

        hide Laptop
        hide Dimmed
        hide Violet UML
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label CSE_srs:
    if (CSE_progress == 1):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve
    elif (CSE_progress == 2):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label CSE_phase1:
    if (CSE_progress == 1):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve
    elif (CSE_progress == 2):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve
    elif (CSE_progress == 3):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label CSE_phase2:
    if (CSE_progress == 1):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve
    elif (CSE_progress == 2):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve
    elif (CSE_progress == 3):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve
    elif (CSE_progress == 4):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label CSE_phase3:
    if (CSE_progress == 1):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve
    elif (CSE_progress == 2):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve
    elif (CSE_progress == 3):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve
    elif (CSE_progress == 4):
        show Dimmed with dissolve
        show Laptop with dissolve

        $ renpy.pause()

        hide Laptop
        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end
