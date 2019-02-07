label Week_1:
    scene West F 301C with fade

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

label Week_1_ARS:
    # Ben arrives at the Staller Center for the Arts.
    scene Staller with fade
    play sound "sounds/Sunny Day.mp3" loop

    B "({i}It’s been a while since I was last here.{/i})"
    scene Staller Music with fade
    B "({i}If I remember correctly, all of the digital art classes are held on the Music side of the building…{/i})"
    B "({i}…because, clearly, {b}that{/b} makes {b}perfect{/b} sense.{/i})"

    stop sound
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

    B "Looks like class is about to start."
    hide Ben
    hide Faith
    with dissolve

    scene eMedia Screen with dissolve
    show projector
    play music "sounds/Miami Viceroy.mp3" loop
    show Composition Slide 1 with dissolve
    "Hello, everyone, and welcome back! I hope you enjoyed your break!"
    "We're going to get right into it, and start by going over the basics of graphic design."
    "There are seven elements that make up any composition."
    show Composition Slide 2a with dissolve
    "The first element is called {b}Point{/b}, or {b}Dot{/b}."
    show Composition Slide 2b with dissolve
    "Placing dots is a good way to focus the viewer's eye on one part of your composition."
    show Composition Slide 2c
    "Using multiple dots can also help guide the viewer's attention in a certain direction."
    show Composition Slide 3a with dissolve
    "That brings us nicely to the next element - {b}Line{/b}."
    show Composition Slide 3b
    "Lines are composed of many individual points, and give directions for the eye."
    show Composition Slide 4
    "When lines are joined together to enclose an area, we have a {b}Shape{/b}."
    "Well-defined shapes help the viewer make sense of your composition."
    show Composition Slide 5
    "Shapes can be manipulated to give the viewer a sense of {b}Depth{/b}."
    "Here, we're making the shape grow smaller as it gets further away."
    "This helps make the image feel less flat and more realistic."
    show Composition Slide 6 with dissolve
    "When arranging shapes, make sure to consider how you use {b}Space{/b}."
    "Placing elements closer together or further apart can change the feel of a composition."
    "Here, we want the road and the ground to shrink and come closer as they get further from the viewer."
    show Composition Slide 7 with dissolve
    "Careful use of {b}Color{/b} also makes a big difference."
    "Different colors elicit different moods, and contrasting colors can highlight your use of space."
    show Composition Slide 8 with dissolve
    "Last but not least, consider adding some {b}Texture{/b}."
    "Doing so helps make your objects look more real, and makes an image feel less flat."
    hide Composition with dissolve
    "Those are all seven of the Compositional Elements."
    "For your first assignment, I want you make an image each for three elements."
    "Make that element very visible in your image, and write short explanations for how you've used them."
    "That's it for now, everyone! I'll see you again next lecture."

    hide projector with dissolve
    stop music fadeout 1.0
    $ renpy.pause(0.5)
    scene eMedia Seats with dissolve
    show Ben Casual Neut Dark at seat_l, img_Scale(500, 800):
    show Faith Mac Foc Neut Dark at seat_r, img_Scale(500, 800):
    with dissolve

    B "({i}Okay, so that wasn't too complicated.{/i})"
    B "({i}I'll have to start this project later, though. I need to get to my next class.{/i})"
    B "({i}Hopefully computer science lectures won’t be too bad this year.{/i})"

    # Needs rewriting - how do we introduce Faith?

    # B "({i}...{/i})"
    # B "({i}...well, this is an uncomfortable silence.{/i})"
    # show Ben Casual Sto Dark at seat_l, img_Scale(500, 800) with dissolve
    # B "({i}Maybe I should say something?{/i})"

    # show Ben Casual Neut Spk at seat_l, img_Scale(500, 800) with dissolve
    # B "Alright, I’ve got to get to my next class."
    # show Ben Casual Neut Dark at seat_l, img_Scale(500, 800):
    # show Faith Mac LkUp Spk at seat_r, img_Scale(500, 800):
    # with dissolve
    # F "Same here."
    # F "Before you go, though - I don’t think I got your name."
    # show Ben Casual Neut Spk at seat_l, img_Scale(500, 800):
    # show Faith Mac LkUp Neut at seat_r, img_Scale(500, 800):
    # with dissolve
    # B "Oh, wow, I completely forgot!"
    # B "My name is Ben. What’s yours?"
    # show Ben Casual Neut Dark at seat_l, img_Scale(500, 800):
    # show Faith Mac LkUp Spk at seat_r, img_Scale(500, 800):
    # with dissolve
    # F "My name is Faith."
    #
    # show Ben Casual Neut Spk at seat_l, img_Scale(500, 800):
    # show Faith Mac LkUp Neut at seat_r, img_Scale(500, 800):
    # with dissolve
    # B "Are you on Steam?"
    # show Ben Casual Neut Dark at seat_l, img_Scale(500, 800):
    # show Faith Mac LkUp Spk at seat_r, img_Scale(500, 800):
    # with dissolve
    # F "Yeah, I am! My name’s kind of dumb - it’s 'GOATmom', with 'goat' in all caps."
    # show Ben Casual Neut Spk at seat_l, img_Scale(500, 800):
    # show Faith Mac LkUp Neut Dark at seat_r, img_Scale(500, 800):
    # with dissolve
    # B "Hey, I’m not judging - I named myself 'SaltedBeef.'"
    #
    # show Ben Casual Neut Spk at seat_l, img_Scale(500, 800):
    # show Faith Mac LkUp Neut Dark at seat_r, img_Scale(500, 800):
    # with dissolve
    # B "Okay, then - it was nice meeting you!"
    # show Ben Casual Neut Dark at seat_l, img_Scale(500, 800):
    # show Faith Mac LkUp Spk at seat_r, img_Scale(500, 800):
    # with dissolve
    # F "It was nice meeting you too!"
    # F "I’ll see you next class, then."

    hide Ben
    hide Faith
    with dissolve

    scene Black with fade

label Week_1_CSE:

#    jump screen_schedule