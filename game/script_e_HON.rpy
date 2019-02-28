label HON_study1:
    if (HON_progress == 1):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        show Study1 A01 with dissolve
        show Study1 A02 with dissolve
        show Study1 A03 with dissolve
        show Study1 A04 with dissolve
        show Study1 A05 with dissolve
        show Study1 A06 with dissolve
        show Study1 A07 with dissolve
        show Study1 A08 with dissolve
        show Study1 A09 with dissolve
        $ renpy.pause()

        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 2):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        show Study1 B01 with dissolve
        show Study1 B02 with dissolve
        show Study1 B03 with dissolve
        show Study1 B04 with dissolve
        show Study1 B05 with dissolve
        show Study1 B06 with dissolve
        show Study1 B07 with dissolve
        show Study1 B08 with dissolve
        show Study1 B09 with dissolve
        show Study1 B10 with dissolve
        show Study1 B11 with dissolve
        $ renpy.pause()

        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 3):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 4):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label HON_study2:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label HON_study3:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end
