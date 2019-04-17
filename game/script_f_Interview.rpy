label interview:
    default finalScore = 0
    # B "Alright - today's the day. Here's hoping I'm ready."

    # scene Interview with fade

    # show Raj Interview Neutral at interview_r with dissolve
    # show Ben Interview Neutral at interview_l with dissolve

    # show Raj Interview Neutral Spk at interview_r with dissolve
    R "It's very good to finally meet you, Benjamin!"
    $ r_name = "Rajesh"
    # show Raj Interview Cheer Spk at interview_r with dissolve
    R "My name is Rajesh - I'm the person who spoke to you over the phone."
    # show Raj Interview Neutral Spk at interview_r with dissolve
    R "I'm glad you could make it today."
    # show Raj Interview Neutral at interview_r
    # show Ben Interview Neutral Spk at interview_l
    # with dissolve
    B "Likewise - I'm glad I could be here."
    # show Ben Interview Neutral at interview_l with dissolve

    $ check_num = (progress[2] if (progress[2] > 0) else 0) if (progress[2] < 2) else 2
    if (check_num == 2):
        show text "{color=#00FF00}{size=30}Resume: [check_num] / 2{/size}{/color}" at skill_check
        # show Rajesh Interview Cheer Spk at interview_r with dissolve
        R "Before we begin, I really must say - I like the way your resume is formatted!"
        # show Rajesh Interview Awkward Spk at interview_r with dissolve
        R "So many applicants think that I {i}like{/i} reading tiny text crammed into a single page!"
        # show Rajesh Interview Neutral Spk at interview_r with dissolve
        R "Seeing yours made for a...refreshing change of pace."
        # show Rajesh Interview
        $ finalScore += 2
    else:
        # show Raj Interview Neutral Spk at interview_r with dissolve
        R "Now, before we begin, I wanted to ask a question about your resume."
        show Dimmed
        show resume_1a
        with dissolve
        # show Raj Interview Awkward Spk at interview_r with dissolve
        show text "{color=#FF0000}{size=30}Resume: [check_num] / 2{/size}{/color}" at skill_check
        R "I have to say, this a...unique resume compared what we usually receive."
        R "Am I correct in assuming that you've no professional experience?"
        # show Raj Interview Awkward at interview_l
        # show Ben Interview Awkward Spk at interview_r
        # with dissolve
        B "Uh, yes, that would be correct."
        B "I'm sorry about the state of my resume - it's been a busy semester."
        # show Raj Interview Neutral Spk at interview_l
        # show Ben Interview Awkward at interview_r
        # with dissolve
        R "Oh, no, I completely understand."

    $ check_num = (progress[2] - 2 if (progress[2] - 2 > 0) else 0) if (progress[2] < 4) else 2
    if (check_num == 2):
        show text "{color=#00FF00}{size=30}LinkedIn: [check_num] / 2{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}LinkedIn: [check_num] / 2{/size}{/color}" at skill_check

    $ renpy.pause()

    $ check_num = (progress[2] - 4 if (progress[2] - 4 > 0) else 0) if (progress[2] < 7) else 3
    if (check_num == 3):
        show text "{color=#00FF00}{size=30}Presentation: [check_num] / 3{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}Presentation: [check_num] / 3{/size}{/color}" at skill_check

    $ renpy.pause()

    $ check_num = (progress[2] - 7 if (progress[2] - 7 > 0) else 0) if (progress[2] < 10) else 3
    if (check_num == 3):
        show text "{color=#00FF00}{size=30}Interviewing: [check_num] / 3{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}Interviewing: [check_num] / 3{/size}{/color}" at skill_check

    $ renpy.pause()

    $ check_num = (progress[0] if (progress[0] > 0) else 0) if (progress[0] < 2) else 2
    if (check_num == 2):
        show text "{color=#00FF00}{size=30}Composition: [check_num] / 2{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}Composition: [check_num] / 2{/size}{/color}" at skill_check

    $ renpy.pause()

    $ check_num = (progress[0] - 2 if (progress[0] - 2 > 0) else 0) if (progress[0] < 4) else 2
    if (check_num == 2):
        show text "{color=#00FF00}{size=30}Typography: [check_num] / 2{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}Typography: [check_num] / 2{/size}{/color}" at skill_check

    $ renpy.pause()

    $ check_num = (progress[0] - 4 if (progress[0] - 4 > 0) else 0) if (progress[0] < 7) else 3
    if (check_num == 3):
        show text "{color=#00FF00}{size=30}Poster Design: [check_num] / 3{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}Poster Design: [check_num] / 3{/size}{/color}" at skill_check

    $ renpy.pause()

    $ check_num = (progress[0] - 7 if (progress[0] - 7 > 0) else 0) if (progress[0] < 10) else 3
    if (check_num == 3):
        show text "{color=#00FF00}{size=30}Video Editing: [check_num] / 3{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}Video Editing: [check_num] / 3{/size}{/color}" at skill_check

    $ renpy.pause()

    $ check_num = (progress[1] if (progress[1] > 0) else 0) if (progress[1] < 2) else 2
    if (check_num == 2):
        show text "{color=#00FF00}{size=30}UML Diagrams: [check_num] / 2{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}UML Diagrams: [check_num] / 2{/size}{/color}" at skill_check

    $ renpy.pause()

    $ check_num = (progress[1] - 2 if (progress[1] - 2 > 0) else 0) if (progress[1] < 4) else 2
    if (check_num == 2):
        show text "{color=#00FF00}{size=30}HTML Designs: [check_num] / 2{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}HTML Designs: [check_num] / 2{/size}{/color}" at skill_check

    $ renpy.pause()

    $ check_num = (progress[1] - 4 if (progress[1] - 4 > 0) else 0) if (progress[1] < 7) else 3
    if (check_num == 3):
        show text "{color=#00FF00}{size=30}Digital Content: [check_num] / 3{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}Digital Content: [check_num] / 3{/size}{/color}" at skill_check

    $ renpy.pause()

    $ check_num = (progress[1] - 7 if (progress[1] - 7 > 0) else 0) if (progress[1] < 10) else 3
    if (check_num == 3):
        show text "{color=#00FF00}{size=30}Web Development: [check_num] / 3{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}Web Development: [check_num] / 3{/size}{/color}" at skill_check

    $ renpy.pause()

label final_Score:

    return
