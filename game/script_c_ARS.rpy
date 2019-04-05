label ARS_sequences:
    # Retrieve index for ARS data using codes[].
    default ARS_index = codes.index("ARS")
    # Retrieve player's current progress in this skill tree.
    default ARS_progress = progress[ARS_index]

    # Set scene in Staller's eMedia SINC site.
    scene eMedia Screen with fade

    #$ renpy.jump("ARS_sequences_%d" % (ARS_progress))

label ARS_sequences_1:
    show projector_emedia with dissolve

    show composition_1 with dissolve
    B "It’s tough to explain art and graphic design when most of your audience picked majors that earn money."
    B "So you started making a PowerPoint explaining the basics of composition - namely {b}Points{/b}, {b}Lines{/b}, {b}Shapes{/b}, and {b}Depth{/b}."
    hide composition_1 with dissolve

    hide projector_emedia with dissolve

    #i += 1
    #jump show_skills

label ARS_sequences_2:
    show projector_emedia with dissolve

    show composition_2 with dissolve
    B "As it turns out, there’s a few more concepts that you can expand on for the presentation."
    B "After adding {b}Space{/b}, {b}Color{/b}, and {b}Texture{/b}, you’ve covered all of the compositional elements and finished your PowerPoint."
    hide composition_2 with dissolve

    hide projector_emedia with dissolve

    #i += 1
    #jump show_skills

label ARS_sequences_3:
    show projector_emedia with dissolve

    show typo_1 with dissolve
    B "To add to your portfolio, you decide to do another demonstration for working with text."
    B "You start by making examples of typographic contrast - like {b}Size{/b}, {b}Structure{/b}, and {b}Form{/b}."
    hide typo_1 with dissolve

    hide projector_emedia with dissolve

    #i += 1
    #jump show_skills

label ARS_sequences_4:
    show projector_emedia with dissolve

    show typo_2 with dissolve
    B "To wrap up your explanation of typography, you decide to combine the different contrasts."
    B "To do so, you put {b}Texture{/b}, {b}Color{/b} and {b}Weight{/b} into one composition."
    hide typo_2 with dissolve

    hide projector_emedia with dissolve

    #i += 1
    #jump show_skills

label ARS_sequences_5:
    show projector_emedia with dissolve

    show poster_1 with dissolve
    B "As a way to demonstrate (i.e. show off) your skills, you decide to make a poster for one of your favorite shows."
    B "You start by laying out the important pieces, with an attention-grabbing shot of the performer in the center of the page."
    hide poster_1 with dissolve

    hide projector_emedia with dissolve

    #i += 1
    #jump show_skills

label ARS_sequences_6:
    show projector_emedia with dissolve

    show poster_2 with dissolve
    B "For the center of the poster, you draw a simplified picture of the performer."
    B "To better frame him in the poster, you also add spotlight effects like the ones used in his show."
    hide poster_2 with dissolve

    hide projector_emedia with dissolve
    #i += 1
    #jump show_skills

label ARS_sequences_7:
    show projector_emedia with dissolve

    show poster_3 with dissolve
    B "To add the finishing touches, you add rows and rows of empty seats, with pieces of text layered between them."
    B "While your choice of performer was a little unprofessional, you hope that this poster makes a good addition to your portfolio."
    hide poster_3 with dissolve

    hide projector_emedia with dissolve

    #i += 1
    #jump show_skills

label ARS_sequences_8:
    show projector_emedia with dissolve

    show video_1 with dissolve
    B "While wasting your life watching YouTube, you realize that a two-minute video could actually make you interesting."
    B "To capitalize on this, you decide to write a script and storyboard to plan out a video."
    hide video_1 with dissolve

    hide projector_emedia with dissolve

    #i += 1
    #jump show_skills

label ARS_sequences_9:
    show projector_emedia with dissolve

    show video_2 with dissolve
    B "Continuing with your plan, you start drawing pictures for each scene in your video."
    hide video_2 with dissolve

    hide projector_emedia with dissolve

    #i += 1
    #jump show_skills

label ARS_sequences_10:
    show projector_emedia with dissolve

    show video_3 with dissolve
    show video_3a with dissolve
    B "As the final step, you add animated transitions between each picture in Adobe After Effects."
    B "All you have to do now is hope that the video proves to be more charming than you are."
    B "(Which, admittedly, isn’t a very high bar.)"
    hide video_3
    hide video_3a
    with dissolve

    hide projector_emedia with dissolve
    #i += 1
    #jump show_skills
