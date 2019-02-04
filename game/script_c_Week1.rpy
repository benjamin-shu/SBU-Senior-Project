label Week_1:
    # Define screen for looking at ARS classroom
    screen look_around():
        modal True
        # projector
        imagebutton:
            pos (910, 84)
            focus_mask True
            idle "Screen Effects/Meet_Faith_map1/projector_button_idle.png"
            hover "Screen Effects/Meet_Faith_map1/projector_button_hover.png"
            action Jump("Meet_Faith_Map1_projector")

        # backmacs
        imagebutton:
            pos (588, 233)
            focus_mask True
            idle "Screen Effects/Meet_Faith_map1/backmacs_button_idle.png"
            hover "Screen Effects/Meet_Faith_map1/backmacs_button_hover.png"
            action Jump("Meet_Faith_Map1_backmacs")

        # mac22
        imagebutton:
            pos (1110, 209)
            focus_mask True
            idle "Screen Effects/Meet_Faith_map1/mac22_button_idle.png"
            hover "Screen Effects/Meet_Faith_map1/mac22_button_hover.png"
            action Jump("Meet_Faith_Map1_macs")

        # mac21
        imagebutton:
            pos (446, 209)
            focus_mask True
            idle "Screen Effects/Meet_Faith_Map1/mac21_button_idle.png"
            hover "Screen Effects/Meet_Faith_Map1/mac21_button_hover.png"
            action Jump("Meet_Faith_Map1_macs")

        # mixer
        imagebutton:
            pos (478, 393)
            focus_mask True
            idle "Screen Effects/Meet_Faith_Map1/mixer_button_idle.png"
            hover "Screen Effects/Meet_Faith_Map1/mixer_button_hover.png"
            action Jump("Meet_Faith_Map1_mixer")

        # mac12
        imagebutton:
            pos (722, 126)
            focus_mask True
            idle "Screen Effects/Meet_Faith_Map1/mac12_button_idle.png"
            hover "Screen Effects/Meet_Faith_Map1/mac12_button_hover.png"
            action Jump("Meet_Faith_Map1_macs")

        # mac11
        imagebutton:
            pos (56, 129)
            focus_mask True
            idle "Screen Effects/Meet_Faith_Map1/mac11_button_idle.png"
            hover "Screen Effects/Meet_Faith_Map1/mac11_button_hover.png"
            action Jump("Meet_Faith_Map1_macs")

        # poster
        imagebutton:
            pos (40, -2)
            focus_mask True
            idle "Screen Effects/Meet_Faith_Map1/poster_button_idle.png"
            hover "Screen Effects/Meet_Faith_Map1/poster_button_hover.png"
            action Jump("Meet_Faith_Map1_poster")

        # Ben
        imagebutton:
            at seat_l, img_Scale(500, 800)
            focus_mask True
            idle ImageReference("Ben Casual Sto Dark")
            hover ImageReference("Ben Casual Sto")
            action Jump("Meet_Faith_Map1_ben")

        # Faith
        imagebutton:
            at seat_r, img_Scale(500, 800)
            focus_mask True
            idle ImageReference("Faith Mac Foc Neut Dark")
            hover ImageReference("Faith Mac Foc Neut")
            action Jump("Meet_Faith_Map1_faith")

        # Faith's Hair
        imagebutton:
            pos (815, 146)
            focus_mask True
            idle "Screen Effects/Meet_Faith_Map1/hair_button_idle.png"
            hover "Screen Effects/Meet_Faith_Map1/hair_button_hover.png"
            action Jump("Meet_Faith_Map1_hair")

        # Faith's Macbook
        imagebutton:
            pos (808, 463)
            focus_mask True
            idle "Screen Effects/Meet_Faith_Map1/macbook_button_idle.png"
            hover "Screen Effects/Meet_Faith_Map1/macbook_button_hover.png"
            action Jump("Meet_Faith_Map1_macbook")

        # Button to return from screen
        imagebutton:
            pos (560, 600)
            focus_mask True
            idle "Screen Effects/back_button_idle.png"
            hover "Screen Effects/back_button_hover.png"
            action Jump("Meet_Faith_Interact")

    scene West F 301C Door with fade

    play music "sounds/Ben/Jazz Brunch.mp3" loop

    B "({i}When I was in my senior year of high school, I couldn’t wait to leave for college.{/i})"
    B "({i}Four years later, and here I am wondering where the hell I’m going next.{/i})"

    show Ben Walk Neut Dark at center, img_Scale(500, 800) with dissolve
    show Ben Walk Neut Spk at center, img_Scale(500, 800) with dissolve
    B "({i}Okay, last check - do I have everything?{/i})"
    show Ben Walk Neut Dark at center, img_Scale(500, 800) with dissolve
    show Dimmed
    show Backpack 1 at projectCenter with dissolve
    B "({i}Laptop, charger, headphones…{/i})"
    show Backpack 2 at projectCenter with dissolve
    B "({i}…binder, pencil case, notepad…{/i})"
    show Backpack 3 at projectCenter with dissolve
    B "({i}…water bottle, running shoes, spare shirt…{/i})"
    show Backpack 4 at projectCenter with dissolve
    B "({i}…first-aid kit, flashlight, mini-stapler…{/i})"
    hide Backpack 4 with dissolve
    hide Dimmed with dissolve
    show Ben Walk Neut Spk at center, img_Scale(500, 800) with dissolve
    B "Okay. I think that’s everything."
    B "I’m going to head out to class now. I’ll see you guys later."
    hide Ben with dissolve

    stop music fadeout 1.0
    scene Black with fade

    B "({i}First stop of the day: Staller Center for the Arts.{/i})"
    B "({i}Okay, Ben. The sun is shining, and it's a bright new day.{/i})"
    B "({i}Try not to fuck this up.{/i})"

label Day1_ARS:
    # Ben arrives at the Staller Center for the Arts.
    scene Staller with fade

    B "({i}It’s been a while since I was last here.{/i})"
    scene Staller Music with fade
    B "({i}If I remember correctly, all of the digital art classes are held on the Music side of the building…{/i})"
    B "({i}…because, clearly, {b}that{/b} makes {b}perfect{/b} sense.{/i})"

    scene eMedia Seats with fade

    show Ben Walk Bore Dark at center, img_Scale(500, 800) with dissolve
    B "({i}Hm. Nobody’s here yet. Guess I’ll just sit down here and wait…{/i})"
    show Ben Casual Sto Dark at seat_l, img_Scale(500, 800) with dissolve
    B "({i}…all by myself…{/i})"
    B "({i}…staring at a computer.{/i})"
    show Ben Casual Sto Spk at seat_l, img_Scale(500, 800) with dissolve
    B "Why did I leave my room, again?"
    show Ben Casual Sto Dark at seat_l, img_Scale(500, 800):
    show Faith Hello Spk Stan at center_stand, img_Scale(500, 1128) behind Ben:
    with dissolve
    play music "sounds/Faith/Doobly Doo.mp3" loop
    F "Hello!"
    show Faith Walk Neut Spk Stan at center_stand, img_Scale(500, 1128) with dissolve
    F "Is this seat taken?"
    show Faith Walk Neut Dark Stan at center_stand, img_Scale(500, 1128):
    show Ben Casual Neut Spk at seat_l, img_Scale(500, 800):
    with dissolve
    B "Oh! No, it’s not taken. Go right ahead."
    show Ben Casual Neut Dark at seat_l, img_Scale(500, 800):
    show Faith Walk Neut Spk Stan at center_stand, img_Scale(500, 1128):
    with dissolve
    F "Thank you!"
    show Faith Walk Neut at seat_r, img_Scale(500, 800) with dissolve
    show Faith Mac Foc Neut Dark at seat_r, img_Scale(500, 800) with dissolve

    B "({i}...{/i})"
    B "({i}...well, this is an uncomfortable silence.{/i})"
    show Ben Casual Sto Dark at seat_l, img_Scale(500, 800) with dissolve
    B "({i}Maybe I should say something?{/i})"

    show fadeInOut

    B "({i}Okay, on to the next class.{/i})"
    B "({i}Hopefully computer science lectures won’t be too bad this year.{/i})"
    show Ben Casual Neut Spk at seat_l, img_Scale(500, 800) with dissolve
    B "Alright, I’ve got to get to my next class."
    show Ben Casual Neut Dark at seat_l, img_Scale(500, 800):
    show Faith Mac LkUp Spk at seat_r, img_Scale(500, 800):
    with dissolve
    F "Same here."

    F "Before you go, though - I don’t think I got your name."
    show Ben Casual Neut Spk at seat_l, img_Scale(500, 800):
    show Faith Mac LkUp Neut at seat_r, img_Scale(500, 800):
    with dissolve
    B "Oh, wow, I completely forgot!"
    B "My name is Ben. What’s yours?"
    show Ben Casual Neut Dark at seat_l, img_Scale(500, 800):
    show Faith Mac LkUp Spk at seat_r, img_Scale(500, 800):
    with dissolve
    F "My name is Faith."

    show Ben Casual Neut Spk at seat_l, img_Scale(500, 800):
    show Faith Mac LkUp Neut at seat_r, img_Scale(500, 800):
    with dissolve
    B "Are you on Steam?"
    show Ben Casual Neut Dark at seat_l, img_Scale(500, 800):
    show Faith Mac LkUp Spk at seat_r, img_Scale(500, 800):
    with dissolve
    F "Yeah, I am! My name’s kind of dumb - it’s 'GOATmom', with 'goat' in all caps."
    show Ben Casual Neut Spk at seat_l, img_Scale(500, 800):
    show Faith Mac LkUp Neut Dark at seat_r, img_Scale(500, 800):
    with dissolve
    B "Hey, I’m not judging - I named myself 'SaltedBeef.'"

    show Ben Casual Neut Spk at seat_l, img_Scale(500, 800):
    show Faith Mac LkUp Neut Dark at seat_r, img_Scale(500, 800):
    with dissolve
    B "Okay, then - it was nice meeting you!"
    show Ben Casual Neut Dark at seat_l, img_Scale(500, 800):
    show Faith Mac LkUp Spk at seat_r, img_Scale(500, 800):
    with dissolve
    F "It was nice meeting you too!"
    F "I’ll see you next class, then."

    hide Ben with dissolve
    hide Faith with dissolve

    scene Black with fade

    stop music fadeout 1.0

    jump screen_schedule
