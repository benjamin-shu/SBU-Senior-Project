label ARS_composition_1:
    show Dimmed with dissolve
    B "For this first project, I'm thinking that I'll use "

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_composition_2:

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_shapes_1:

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_shapes_2:

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_typography_1:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_typography_2:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_poster_1:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_poster_2:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_poster_3:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_poster_4:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_video_1:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_video_2:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_video_3:

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end

label ARS_video_4:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
    else:
        $ phase = 0
        jump week_end
