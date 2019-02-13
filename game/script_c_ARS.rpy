label ARS_composition_1:
    show Dimmed with dissolve
    show Composition Canvas with dissolve
    B "For this first project, I'm thinking that I'll use {b}Point{/p}, {b}Depth{/b}, and {b}Shape{/b}."
    show Composition Point01 with dissolve
    B "For {b}Point{/b}, I think I'll use this - a single boat out on the water draws attention."
    show Composition Point02 with dissolve
    B "I think I'll add a sunset in the back, just to make it more obvious."
    show Composition Depth01 with dissolve
    B "For {b}Depth{/b}, I'm thinking of a tunnel, drawn with one-point perspective."
    show Composition Depth02 with dissolve
    B "Adding a point makes it look a little more like a tunnel, but I think it's missing something."
    show Composition Shape01 with dissolve
    B "And for {b}Shape{/b}, I thought of a video game character that's basically a puff ball."
    show Composition Shape02 with dissolve
    B "It's a fun little design, and made entirely of distinctive shapes."
    B "It might look better with some color, though."

    hide Composition
    hide Dimmed
    with dissolve

    B "I like the way these look right now, but I should probably add some more detail later."

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)

label ARS_composition_2:

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_shapes_1:

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_shapes_2:

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_typography_1:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_typography_2:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_poster_1:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_poster_2:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_poster_3:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_poster_4:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_video_1:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_video_2:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_video_3:

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)

label ARS_video_4:
    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d", phase)
