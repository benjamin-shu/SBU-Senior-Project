label HON_study1:
    "study1"
    
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
