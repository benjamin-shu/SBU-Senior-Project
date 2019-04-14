label interview:
    # B "Alright - today's the day. Here's hoping I'm ready."

    # scene Interview with fade

    # show Ben Formal

    $ check_num = (progress[2] if (progress[2] > 0) else 0) if (progress[2] < 2) else 2
    if (check_num == 2):
        show text "{color=#00FF00}{size=30}Resume: [check_num] / 2{/size}{/color}" at skill_check
    else:
        show text "{color=#FF0000}{size=30}Resume: [check_num] / 2{/size}{/color}" at skill_check

    $ renpy.pause()

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

    return
