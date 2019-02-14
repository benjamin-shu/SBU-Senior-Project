label CSE_uml:
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
