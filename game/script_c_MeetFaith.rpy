label Day1:
    scene West F 301C Door with fade

    play music "sounds/Ben/Jazz Brunch.mp3" loop

    B "{i}When I was in my senior year of high school, I couldn’t wait to leave for college.{/i}"
    B "{i}Four years later, and here I am wondering where the hell I’m going next.{/i}"

    show Ben Walk Neut Dark at center, img_Scale(500, 800) with dissolve
    show Dimmed
    show Backpack 1 at projectCenter with dissolve
    B "{i}Laptop, charger, headphones…{/i}"
    show Backpack 2 at projectCenter with dissolve
    B "{i}…binder, pencil case, notepad…{/i}"
    show Backpack 3 at projectCenter with dissolve
    B "{i}…water bottle, running shoes, spare shirt…{/i}"
    show Backpack 4 at projectCenter with dissolve
    B "{i}…first-aid kit, scissors, mini-stapler…{/i}"
    hide Backpack 4 with dissolve
    hide Dimmed with dissolve
    show Ben Walk Neut Spk at center, img_Scale(500, 800) with dissolve
    B "…and the flashlight. Can’t forget the flashlight."
    B "Okay. I think that’s everything."
    B "I’m going to head out to class now. I’ll see you guys later."
    show Ben Walk Bore Dark at center, img_Scale(500, 800) with dissolve
    "Kris" "See you later, Shuben."

    stop music fadeout 1.0
    scene Black with fade

    B "{i}First stop of the day: Staller Center for the Arts.{/i}"
    B "{i}Okay, Ben. You’ve only got two more semesters left.{/i}"
    B "{i}Try not to fuck this up.{/i}"
    hide Ben Walk Bore with dissolve

label Day1_ARS:
    scene Staller with fade

    B "{i}It’s been a while since I was last here.{/i}"
    scene Staller Music with fade
    B "{i}If I remember correctly, all of the digital art classes
       are held on the Music side of the building…{/i}"
    B "{i}…because {b}that{/b}, of course, makes {b}perfect{/b} sense.{/i}"

    scene eMedia Seats with fade

    show Ben Walk Bore Dark at center, img_Scale(500, 800) with dissolve
    B "{i}Hm. Nobody’s here yet. Guess I’ll just sit down here and wait…{/i}"
    show Ben Casual Sto Dark at seat_l, img_Scale(500, 800) with dissolve
    B "{i}…all by myself…{/i}"
    B "{i}…staring at a computer.{/i}"
    show Ben Casual Sto Spk at seat_l, img_Scale(500, 800) with dissolve
    B "Why did I leave my room, again?"
    show Ben Casual Sto Dark at seat_l, img_Scale(500, 800):
    show Faith Hello Spk at center, img_Scale(500, 800) behind Ben:
    with dissolve
    F "Hello!"
    show Faith Walk Neut Spk at center, img_Scale(500, 800) with dissolve
    F "Is this seat taken?"
    show Faith Walk Neut Dark at center, img_Scale(500, 800):
    show Ben Casual Neut Spk at seat_l, img_Scale(500, 800):
    with dissolve
    B "Oh! No, it’s not taken. Go right ahead."
    show Ben Casual Neut Dark at seat_l, img_Scale(500, 800):
    show Faith Walk Neut Spk at center, img_Scale(500, 800):
    with dissolve
    F "Thank you!"
    show Faith Walk Neut at seat_r, img_Scale(500, 800) with dissolve
    show Faith Mac Foc Neut Dark at seat_r, img_Scale(500, 800) with dissolve

    B "{i}...{/i}"
    B "{i}...well, this is an uncomfortable silence.{/i}"
    show Ben Casual Sto Dark at seat_l, img_Scale(500, 800) with dissolve
    B "{i}Maybe I should say something?{/i}"

label Meet_Faith:
    define faith_talked = False
    define meet_faith_ben_clicks = 0

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

    window hide
    menu:
        "{i}{b}Maybe I should say something?{/b}{/i}"

        "Say nothing.":
            window show
            B "{i}...nah. She’s probably got other things to think about right now.{/i}"
            B "{i}No sense in me bothering her.{i}"

        "Look for conversation starters.":
            label Meet_Faith_Map1:
                call screen look_around

                label Meet_Faith_Map1_ben:
                    if meet_faith_ben_clicks == 0:
                        B "{i}It’s me! Not much to see here.{/i}"
                        $ meet_faith_ben_clicks = 1

                    elif meet_faith_ben_clicks == 1:
                        B "{i}Still just me! Still just a skinny Asian kid with glasses.{/i}"
                        B "{i}Really not much else to say.{/i}"
                        $ meet_faith_ben_clicks = 2

                    elif meet_faith_ben_clicks == 2:
                        B "{i}Lots of other things to look at here!{/i}"
                        B "{i}I am definitely not the most interesting thing in this room.{/i}"
                        $ meet_faith_ben_clicks = 3

                    elif meet_faith_ben_clicks > 2:
                        B "{i}I should probably be spending my time thinking about something else!{/i}"
                        $ meet_faith_ben_clicks = meet_faith_ben_clicks + 1

                    jump Meet_Faith_Map1

                label Meet_Faith_Map1_faith:
                    B "{i}Blonde hair, black t-shirt with ripped jeans, and a MacBook.{/i}"
                    B "{i}No idea who she is, or where she came from.{/i}"

                    jump Meet_Faith_Map1

                label Meet_Faith_Map1_faith_hair:
                    B "{i}Her hair is {b}impressively{/b} spikey. I wonder how she does that?{/i}"
                    B "{i}Is there some kind of product that gives you anime hair?{/i}"
                    B "{i}I'm kind of curious now. Would it be rude to ask?{/i}"
                    B "{i}Yeah, it'd probably be rude to ask.{/i}"

                    jump Meet_Faith_Map1

                label Meet_Faith_Map1_faith_clothes:
                    B "{i}I've never really understood why ripped jeans are a thing.{/i}"
                    B "{i}I get that it's a fashion and all, but you're still buying damaged clothes.{/i}"
                    B "{i}How do you keep them from falling apart?{/i}"
                    if f_name == "???":
                        B "{i}Maybe this girl can explain it to me?{/i}"
                    else:
                        B "{i}Maybe Faith has something to say about that?{/i}"

                    jump Meet_Faith_Map1

                label Meet_Faith_Map1_macbook:
                    show Dimmed with dissolve
                    show Macbook with dissolve
                    # show Macbook meet_faith with dissolve (simultaneous transition!)
                    B "{i}It looks like she’s working with Adobe Illustrator.{/i}"
                    B "{i}She’s working on a profile view of a person’s face...{/i}"
                    B "{i}Have I seen that before? It kind of looks like the main character from Undertale.{/i}"
                    B "{i}Maybe I should ask.{/i}"
                    # hide Macbook meet_faith with dissolve (simultaneous transition!)
                    hide Macbook with dissolve
                    hide Dimmed with dissolve

                    jump Meet_Faith_Map1

                label Meet_Faith_Map1_macs:
                    B "{i}The eMedia SINC site provides Mac computers for the students.{/i}"
                    B "{i}They run pretty fast, and they all have the Adobe Creative Cloud installed.{/i}"
                    B "{i}They're also tall, so they can hide you if you're on your phone or napping.{/i}"
                    B "{i}It happens more often than you'd think.{/i}"
                    B "{i}From what I've been told, I mean.{/i}"

                    jump Meet_Faith_Map1

                label Meet_Faith_Map1_mixer:
                    B "{i}There's all sorts of equipment here besides the computers.{/i}"
                    B "{i}I've seen sound mixers, keyboards, art tablets, and microphones on the desks.{/i}"
                    B "{i}It makes this a great place to work, if you know what you're doing.{/i}"

                    jump Meet_Faith_Map1

                label Meet_Faith_Map1_backmacs:
                    B "{i}Over yonder are the forgotten lands of the back two rows.{/i}"
                    B "{i}When you're that far away from the screen, it's hard to hear the professor.{/i}"
                    B "{i}It is pretty easy to reach the door, though.{/i}"

                    jump Meet_Faith_Map1

                label Meet_Faith_Map1_poster:
                    B "{i}It's a flyer for the MFA program here at Stony Brook.{/i}"
                    B "{i}I'd really like to join, but that would mean another two years of torture and tuition.{/i}"
                    B "{i}I should probably worry about my undergraduate degree first.{/i}"

                    jump Meet_Faith_Map1

                label Meet_Faith_Map1_projector:
                    B "{i}This room doesn't have a chalkboard or a dry erase board.{/i}"
                    B "{i}Instead, that projector displays a computer screen up on the front wall.{/i}"
                    B "{i}It makes sense, since a lot of the professors here use PowerPoint presentations.{/i}"

                    jump Meet_Faith_Map1

        "Attempt idle small talk.":
            window show
            if faith_obs < 2:
                B "So, uh, what’s your name?"
                F "…"
                B "…hello?"
                F "Hm? Oh! Sorry, did you say something?"
                B "What’s your name?"
                $ f_name = "Faith"
                F "My name is Faith. And your name is…?"
                B "My name is Ben. It’s nice to meet you!"
                F "Likewise!"
                # Needs rewrite!
                F "I’m really sorry to cut you off - I don’t want to be rude or anything…"
                F "But I really need to get this thing done."
                B "Oh! Okay, that’s fine. I completely understand."
                B "I’ll let you get to it, then."
            elif faith_obs == 2:
                B "Excuse me?"
                F "Hm? Oh! Hi!"
                F "What’s up?"
                B "If you don’t mind me asking, are you drawing Frisk?"
                # Smiling
                F "Yeah, I am! Have you played Undertale?"
                B "Yeah! It’s one of my favorite video games!"
                F "Who was your favorite character?"
                B "Sans, hands down."

                # [An define of Sans’ pixel art appears on-screen.]

                B "The man is incapable of taking anything seriously, and it’s amazing."

                # [An define of Toriel appears on-screen.]

                F "Personally, Toriel is my favorite. After all, Goat Mom is Best Mom."
                B "Ha! Never heard that one before."
                B "So is the Frisk drawing for a class?"
                F "No, it’s actually for a YouTube video I wanted to make."

                # [An define of a YouTube video with a blank thumbnail appears.]

                F "I need a thumbnail, and I wanted to use Frisk."
                B "Wow. What kind of video is it?"
                F "It’s kind of a commentary, at this point. It’s…a work in progress."
                B "Well, I’ll have to check it out some time."
                B "I’m Ben, by the way! What’s your name?"
                $ f_name = "Faith"
                F "My name is Faith! Nice to meet you!"
                B "Likewise!"

# Conclusion sequence.
label End:
    return
