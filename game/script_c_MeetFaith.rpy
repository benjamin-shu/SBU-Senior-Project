label Day1:
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

    # Actual story sequence starts here.
    scene West F 301C Door with fade

    play music "sounds/Ben/Jazz Brunch.mp3" loop

    B "{i}When I was in my senior year of high school, I couldn’t wait to leave for college.{/i}"
    B "{i}Four years later, and here I am wondering where the hell I’m going next.{/i}"

    show Ben Walk Neut Dark at center, img_Scale(500, 800) with dissolve
    show Ben Walk Neut Spl at center, img_Scale(500, 800) with dissolve
    B "{i}Okay, last check - do I have everything?{/i}"
    show Ben Walk Neut Dark at center, img_Scale(500, 800) with dissolve
    show Dimmed
    show Backpack 1 at projectCenter with dissolve
    B "{i}Laptop, charger, headphones…{/i}"
    show Backpack 2 at projectCenter with dissolve
    B "{i}…binder, pencil case, notepad…{/i}"
    show Backpack 3 at projectCenter with dissolve
    B "{i}…water bottle, running shoes, spare shirt…{/i}"
    show Backpack 4 at projectCenter with dissolve
    B "{i}…first-aid kit, flashlight, mini-stapler…{/i}"
    hide Backpack 4 with dissolve
    hide Dimmed with dissolve
    show Ben Walk Neut Spk at center, img_Scale(500, 800) with dissolve
    B "Okay. I think that’s everything."
    B "I’m going to head out to class now. I’ll see you guys later."
    hide Ben with dissolve

    stop music fadeout 1.0
    scene Black with fade

    B "{i}First stop of the day: Staller Center for the Arts.{/i}"
    B "{i}Okay, Ben. The sun is shining, and it's a bright new day.{/i}"
    B "{i}Try not to fuck this up.{/i}"

label Day1_ARS:
    scene Staller with fade

    B "{i}It’s been a while since I was last here.{/i}"
    scene Staller Music with fade
    B "{i}If I remember correctly, all of the digital art classes are held on the Music side of the building…{/i}"
    B "{i}…because, clearly, {b}that{/b} makes {b}perfect{/b} sense.{/i}"

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
    # Conditional checks for looking around the eMedia SINC site.
    define faith_hair = False
    define faith_mac = False
    define meet_faith_ben_clicks = 0

    # Conditional checks for talking to Faith.
    define faith_talked = False
    define faith_awk = False            # Have you made conversation awkward?
    define faith_art = False            # Have you asked if Faith is an Arts major?
    define faith_work = False           # Have you asked Faith what she's working on?
    define faith_under = False          # Have you asked Faith about Undertale?
    define faith_youtube = False        # Have you found out about Faith's YouTube channel?

label Meet_Faith_Interact:
    window hide
    menu:
        "{i}{b}Should I talk to this random stranger?{/b}{/i}"

        "Nah - let her go about her business." if faith_talked == False:
            window show
            B "{i}...nah. She’s probably got other things to think about right now.{/i}"
            B "{i}No sense in me bothering her.{i}"

            jump Meet_Faith_End

        "Wait for class to start." if (faith_talked == True && faith_awk == False):
            window show
            B "{i}Okay, that's enough. I've avoided awkward interactions so far.{/i}"
            B "{i}Let's try and keep it that way.{i}"

            jump Meet_Faith_End

        "Shut up and pray that the professor shows up soon." if (faith_talked == True && faith_awk == True):
            window show
            B "{i}Well, that was a stupid question!{/i}"
            B "{i}Way to go, genius. I better keep a lid on it now for now.{i}"

            jump Meet_Faith_End

        "Look around the room for conversation starters and talking points.":
            label Meet_Faith_Map1:
                # Call look_around screen to force the player to pick an ImageButton.
                call screen look_around

                # A little joke for if the player clicks on Ben.
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

                # Intended for Faith's face/arms. Unsure as to whether I will use this.
                label Meet_Faith_Map1_faith:
                    B "{i}Blonde hair, black t-shirt with ripped jeans, and a MacBook.{/i}"
                    B "{i}No idea who she is, or where she came from.{/i}"

                    jump Meet_Faith_Map1

                # For clicking on Faith's hairstyle. Asking about this is pretty stupid.
                label Meet_Faith_Map1_faith_hair:
                    B "{i}Her hair is {b}impressively{/b} spikey. I wonder how she does that?{/i}"
                    B "{i}Is there some kind of product that gives you anime hair?{/i}"
                    B "{i}I'm kind of curious now. Would it be rude to ask?{/i}"
                    B "{i}Yeah, it'd probably be rude to ask.{/i}"

                    jump Meet_Faith_Map1

                # Intended for Faith's t-shirt and jeans. May not use this - jeans will not be visible.
                label Meet_Faith_Map1_faith_clothes:
                    B "{i}I've never really understood why ripped jeans are a thing.{/i}"
                    B "{i}I get that it's a fashion and all, but you're still buying damaged clothes.{/i}"
                    B "{i}How do you keep them from falling apart?{/i}"
                    if f_name == "???":
                        B "{i}Maybe this girl can explain it to me?{/i}"
                    else:
                        B "{i}Maybe Faith has something to say about that?{/i}"

                    jump Meet_Faith_Map1

                # For clicking on Faith's Macbook Pro. Leads to an image of Adobe Illustrator.
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

                # For clicking on the Mac computers in the eMedia SINC site.
                label Meet_Faith_Map1_macs:
                    B "{i}The eMedia SINC site provides Mac computers for the students.{/i}"
                    B "{i}They run pretty fast, and they all have the Adobe Creative Cloud installed.{/i}"
                    B "{i}They're also tall, so they can hide you if you're on your phone or napping.{/i}"
                    B "{i}It happens more often than you'd think.{/i}"
                    B "{i}From what I've been told, I mean.{/i}"

                    jump Meet_Faith_Map1

                # For clicking on an audio mixer in the eMedia SINC site.
                label Meet_Faith_Map1_mixer:
                    B "{i}There's all sorts of equipment here besides the computers.{/i}"
                    B "{i}I've seen sound mixers, keyboards, art tablets, and microphones on the desks.{/i}"
                    B "{i}It makes this a great place to work, if you know what you're doing.{/i}"

                    jump Meet_Faith_Map1

                # For clicking on the very back rows of the classroom.
                label Meet_Faith_Map1_backmacs:
                    B "{i}Over yonder are the forgotten lands of the back two rows.{/i}"
                    B "{i}When you're that far away from the screen, it's hard to hear the professor.{/i}"
                    B "{i}It is pretty easy to reach the door, though.{/i}"

                    jump Meet_Faith_Map1

                # For clicking on a poster on the wall.
                label Meet_Faith_Map1_poster:
                    B "{i}It's a flyer for the MFA program here at Stony Brook.{/i}"
                    B "{i}I'd really like to join, but that would mean another two years of torture and tuition.{/i}"
                    B "{i}I should probably worry about my undergraduate degree first.{/i}"

                    jump Meet_Faith_Map1

                # For clicking on a projector in the back of the classroom.
                label Meet_Faith_Map1_projector:
                    B "{i}This room doesn't have a chalkboard or a dry erase board.{/i}"
                    B "{i}Instead, that projector displays a computer screen up on the front wall.{/i}"
                    B "{i}It makes sense, since a lot of the professors here use PowerPoint presentations.{/i}"

                    jump Meet_Faith_Map1

                # Must include a button to return to interaction menu!
                # jump Meet_Faith_Interact

        "Interrupt her work with idle small talk.":
        label Meet_Faith_Talk:
            menu:
                # If the player backs out on talking to Faith.
                "On second thought, I'll just keep my mouth shut." if faith_talked == False:
                    jump Meet_Faith_Interact

                # If the player decides to stop talking after saying something.
                "I'm going to shut up now." if faith_talked == True:
                    jump Meet_Faith_Interact

                # If the player decides to start by asking Faith's name.
                "So, what's your name?" if (faith_awk == False && faith_talked == False && f_name == "???"):
                    $ faith_talked = True;
                    B "So, uh, what’s your name?"
                    F "…"
                    B "…hello?"
                    F "Hm? Oh! Sorry, did you say something?"
                    B "What’s your name?"
                    $ f_name = "Faith"
                    F "My name is Faith. And your name is…?"
                    B "My name is Ben. It’s nice to meet you!"
                    F "Likewise!"
                    B "..."
                    B "{i}Alright, genius - {b}now{/b} what?{/i}"

                    jump Meet_Faith_Talk

                # If the player asks for Faith's name after saying something else.
                "I probably should have asked this first, but what's your name?" if (faith_awk == False && faith_talked == True && f_name == "???"):
                    $ faith_talked = True
                    $ f_name = "Faith"
                    B "So, uh, probably should have asked this first, but..."
                    B "What's your name?"
                    F "My name is Faith. What's yours?"
                    B "My name is Ben. It's nice to meet you!"
                    F "Likewise!"

                    jump Meet_Faith_Talk

                # If the player starts by asking about Faith's major.
                "Are you an arts major?" if (faith_awk == False && faith_talked == False):
                    $ faith_talked = True
                    $ faith_art = True
                    B "So, uh, are you an arts major?"
                    F "What was that?"
                    B "Oh! I didn’t mean to bug you or anything!"
                    B "I just thought I’d ask, since we’re sitting in an arts lab and all..."
                    B "{i}Real smooth, jackass!{/i}"
                    F "Oh! Yeah, no, I get that!"
                    F "I’m an ARS major, or Studio Art."
                    F "What about you? What major are you in?"
                    B "I'm a Computer Science major."
                    F "Really? Why are you in an arts class, then?"
                    B "{i}That's an {b}excellent{/b} question!{/i}"
                    B "I'm doing a Digital Arts minor, so I get to take this class too."
                    F "Oh, wow! What made you decide to take that minor?"
                    B "Well, at first, I was hoping I could major in something like Digital Arts."
                    B "After I got here, I found out that they only offered the minor. So I decided to major in CS instead."
                    F "Isn't the Comp Sci major here really difficult?"
                    B "I never said it was a {b}good{/b} decision."

                # If the player asks about Faith's major after saying something else.
                "So, I'm guessing you're an arts major?" if (faith_awk == False && faith_talked == True):
                    $ faith_talked = True
                    $ faith_art = True
                    B "So, I'm guessing you're an arts major?"
                    F "Yeah, I am! Well, technically I'm a {i}Studio{/i} Art major."
                    B "What's the difference?"
                    F "..."
                    F "I dunno!"
                    F "What major are you, by the way?"
                    B "I'm a Computer Science major."
                    F "Really? Why are you in an arts class, then?"
                    B "{i}That's an {b}excellent{/b} question!{/i}"
                    B "I'm doing a Digital Arts minor, so I get to take this class too."
                    F "Oh, wow! What made you decide to take that minor?"
                    B "Well, at first, I was hoping I could major in something like Digital Arts."
                    B "After I got here, I found out that they only offered the minor. So I decided to major in CS instead."
                    F "Isn't the Comp Sci major here really difficult?"
                    B "I never said it was a {b}good{/b} decision."

                "Weird question - what do you use on your hair?" if (faith_awk == False && faith_hair == True):
                    $ faith_talked = True
                    $ faith_awk = True
                    B "So, um, weird question - what do you use on your hair?"
                    F "...I’m sorry. What was that?"
                    B "Well, your hair is just so spikey! How did you make it do that?"
                    F "...I didn’t do anything to it. This is just my hair."
                    B "...oh."
                    B "{i}And now you made it awkward. Nice going, jackass!{/i}"
                    F "Is there something wrong with my hair?" # Use puppy dog face!
                    B "What? No! Not at all!"
                    B "I didn’t mean it like that! I was just surprised, is all!"
                    B "I haven’t seen hair that sticks out at those...{i}angles{/i} before."
                    F "...?"
                    B "{i}I really need to shut up now.{/i}"

                "What are you working on right now?" if (faith_awk == False && faith_under == False):
                    $ faith_talked = True
                    $ faith_work = True
                    if faith_talked == False:
                        B "Excuse me? What are you working on right now?"
                        F "Oh, this? It's a thumbnail for a YouTube video I want to make."
                    else:
                        B "What are you working on right now?"
                        F "I'm making a thumbnail for a YouTube video I want to make."

                    B "Neat! What kind of video is it?"
                    F "Nothing special, really - just me, talking about video games."
                    F "It's a fun little side project I like to do when I have time."

                "So you've made YouTube videos before?" if (faith_awk == False && faith_work == True):
                    B "So you've made YouTube videos before?"
                    F "Yeah, I have. I made a channel a long time ago."
                    F "Most of the videos are just speedpaints or me talking about video games."
                    B "That sounds like fun!"
                    F "It is! I don’t really have a lot of subscribers, but it’s nice to just make videos every once in a while."


                    # F "I don't really expect much, honestly. There's no way I could ever do it for a living."
                    # B "Really? Why's that?"
                    # F "I wouldn't get discovered. Not enough to partner with YouTube, anyway."

label Meet_Faith_End:


# Conclusion sequence.
label End:
    return
