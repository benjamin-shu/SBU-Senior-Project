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
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label CSE_phase1:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label CSE_phase2:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label CSE_phase3:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end
