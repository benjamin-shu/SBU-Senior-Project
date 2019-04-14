label ARS_sequences:
    # Retrieve index for ARS data using codes[].
    default ARS_index = codes.index("ARS")

    # Set scene in Staller's eMedia SINC site.
    scene eMedia Screen with fade

    $ renpy.jump("ARS_sequences_%d" % (progress[ARS_index]))

label ARS_sequences_1:
    show projector_emedia with dissolve

    show composition_1 with dissolve
    B "It’s tough to explain art and graphic design when most of my audience picked majors that earn money."
    B "So I started making a PowerPoint explaining the basics of composition - namely {b}Points{/b}, {b}Lines{/b}, {b}Shapes{/b}, and {b}Depth{/b}."
    hide composition_1 with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label ARS_sequences_2:
    show projector_emedia with dissolve

    show composition_2 with dissolve
    B "As it turns out, there’s a few more concepts that I can expand on for the presentation."
    show text "{color=#000000}{size=30}Composition: 2 / 2{/size}{/color}" at skill_check
    B "After adding {b}Space{/b}, {b}Color{/b}, and {b}Texture{/b}, I think I’ve covered all of the bases and finished my PowerPoint."
    hide composition_2 with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label ARS_sequences_3:
    show projector_emedia with dissolve

    show typo_1 with dissolve
    B "To add to my portfolio, I'm making another demonstration for working with text."
    B "I'll start with the different types of typographic contrast - {b}Size{/b}, {b}Structure{/b}, and {b}Form{/b}."
    hide typo_1 with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label ARS_sequences_4:
    show projector_emedia with dissolve

    show typo_2 with dissolve
    B "To wrap up my explanation of typography, I decided to combine the different examples."
    show text "{color=#000000}{size=30}Typography: 2 / 2{/size}{/color}" at skill_check
    B "To do so, I put {b}Texture{/b}, {b}Color{/b} and {b}Weight{/b} all into one composition."
    hide typo_2 with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label ARS_sequences_5:
    show projector_emedia with dissolve

    show poster_1 with dissolve
    B "As a way to demonstrate (i.e. show off) my skills, I decided to make a poster for one of my favorite comedians."
    B "I started by laying out the important pieces, with an attention-grabbing shot in the center of the page."
    hide poster_1 with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label ARS_sequences_6:
    show projector_emedia with dissolve

    show poster_2 with dissolve
    B "For the center of the poster, I drew a simplified picture of the performer."
    B "To better frame him in the poster, I also added spotlights like the ones in his show."
    hide poster_2 with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label ARS_sequences_7:
    show projector_emedia with dissolve

    show poster_3 with dissolve
    B "For the finishing touches, I added rows of empty seats with pieces of text layered between them."
    show text "{color=#000000}{size=30}Poster Design: 3 / 3{/size}{/color}" at skill_check
    B "While my choice of performer was a little unprofessional, I hope that this poster makes a good addition to my portfolio."
    hide poster_3 with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label ARS_sequences_8:
    show projector_emedia with dissolve

    show video_1 with dissolve
    B "While wasting my life watching YouTube, I realized that a two-minute video could actually make me interesting."
    B "To capitalize on this, I've made a script and storyboard to plan out a video."
    hide video_1 with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label ARS_sequences_9:
    show projector_emedia with dissolve

    show video_2 with dissolve
    B "Continuing with my plan, I started drawing pictures for each scene in the video."
    hide video_2 with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label ARS_sequences_10:
    show projector_emedia with dissolve

    show video_3 with dissolve
    show video_3a with dissolve
    B "As the final step, I've added animated transitions between each picture in Adobe After Effects."
    show text "{color=#000000}{size=30}Video Editing: 3 / 3{/size}{/color}" at skill_check
    B "All I have to do now is hope that the video proves to be more charming than I am."
    B "(Which, admittedly, isn’t a very high bar.)"
    hide video_3
    hide video_3a
    with dissolve

    hide projector_emedia with dissolve
    $ i += 1
    jump show_skills
