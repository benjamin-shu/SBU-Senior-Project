label Week_0:
    show Ben Walk Neut Dark at center, img_Scale(500, 800) with dissolve
    show Ben Walk Neut Spk at center, img_Scale(500, 800) with dissolve
    B "Okay, Ben, one last check - do you have everything?"
    show Ben Walk Neut Dark at center, img_Scale(500, 800) with dissolve
    show Dimmed
    show Backpack 1 at projectCenter with dissolve
    B "Laptop, charger, headphones..."
    show Backpack 2 at projectCenter with dissolve
    B "...binder, pencil case, notepad..."
    show Backpack 3 at projectCenter with dissolve
    B "...water bottle, running shoes, spare shirt..."
    show Backpack 4 at projectCenter with dissolve
    B "...first-aid kit, flashlight, mini-stapler..."
    hide Backpack 4 with dissolve
    hide Dimmed with dissolve
    show Ben Walk Neut Spk at center, img_Scale(500, 800) with dissolve
    B "Okay, I think we're good. Now, what's on the agenda for today?"
    hide Ben with dissolve

    jump schedule_reminders

label Week_0_ARS:
    # Ben arrives at the Staller Center for the Arts.
    B "{i}First stop of the day: Staller Center for the Arts.{/i}"

    scene Staller with fade
    play sound "sounds/Sunny Day.mp3" loop

    B "{i}Okay, Ben. The sun is shining, and it's a bright new day.{/i}"
    B "{i}And now, I get to take an art class again."
    scene Staller Music with fade
    B "{i}If I remember correctly, all of the digital art classes are held on the Music side of the building…{/i}"
    B "{i}…because, clearly, {b}that{/b} makes {b}perfect{/b} sense.{/i}"

    stop sound
    scene eMedia Seats with fade

    show Ben Walk Bore Dark at center, img_Scale(500, 800) with dissolve
    B "{i}Hm. Nobody’s here yet. Guess I’ll just sit down here and wait…{/i}"
    show Ben Casual Sto Dark at seat_l_ARS, img_Scale(500, 800) with dissolve
    B "{i}…all by myself…{/i}"
    B "{i}…staring at a computer.{/i}"
    show Ben Casual Sto Spk at seat_l_ARS, img_Scale(500, 800) with dissolve
    B "Why did I leave my room, again?"
    show Ben Casual Sto Dark at seat_l_ARS, img_Scale(500, 800):
    show Faith Hello Spk Stan at center_stand, img_Scale(500, 1128) behind Ben:
    with dissolve
    F "Hello!"
    show Faith Walk Neut Spk Stan at center_stand, img_Scale(500, 1128) with dissolve
    F "Is this seat taken?"
    show Faith Walk Neut Dark Stan at center_stand, img_Scale(500, 1128):
    show Ben Casual Neut Spk at seat_l_ARS, img_Scale(500, 800):
    with dissolve
    B "Oh! No, it’s not taken. Go right ahead."
    show Ben Casual Neut Dark at seat_l_ARS, img_Scale(500, 800):
    show Faith Walk Neut Spk Stan at center_stand, img_Scale(500, 1128):
    with dissolve
    F "Thank you!"
    show Faith Walk Neut at seat_r_ARS, img_Scale(500, 800) with dissolve
    show Faith Mac Foc Neut Dark at seat_r_ARS, img_Scale(500, 800) with dissolve

    B "{i}It doesn't take much longer for class to start.{/i}"
    hide Ben
    hide Faith
    with dissolve

    scene eMedia Screen with dissolve
    show projector with dissolve
    play music "sounds/Miami Viceroy.mp3" loop
    show Composition Slide 1 with dissolve
    "Hello, everyone, and welcome back! I hope you enjoyed your break!"
    "We're going to get right into it, and start by going over the basics of graphic design."
    "There are seven elements that make up any composition."
    show Composition Slide 2a with dissolve
    "The first element is called {b}Point{/b}, or {b}Dot{/b}."
    show Composition Slide 2b with dissolve
    "Placing dots is a good way to focus the viewer's eye on one part of your composition."
    show Composition Slide 2c with dissolve
    "Using multiple dots can also help guide the viewer's attention in a certain direction."
    show Composition Slide 3a with dissolve
    "That brings us nicely to the next element - {b}Line{/b}."
    show Composition Slide 3b with dissolve
    "Lines are composed of many individual points, and give directions for the eye."
    show Composition Slide 4 with dissolve
    "When lines are joined together to enclose an area, we have a {b}Shape{/b}."
    "Well-defined shapes help the viewer make sense of your composition."
    show Composition Slide 5 with dissolve
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
    show Composition Slide 9 with dissolve
    "For your first assignment, I want you make three images, each demonstrating an element."
    "Make that element very visible in your image, and write short explanations for how you've used them."
    hide Composition with dissolve

    hide projector with dissolve
    stop music fadeout 1.0
    $ renpy.pause(0.5)

    scene eMedia Seats with dissolve
    show Ben Casual Neut Dark at seat_l_ARS, img_Scale(500, 800):
    show Faith Mac Foc Neut Dark at seat_r_ARS, img_Scale(500, 800):
    with dissolve

    B "{i}Okay, so that wasn't too complicated.{/i}"
    B "{i}Might as well get some work done while the professor's still talking.{/i}"

    jump week_phase_0_check

label Week_0_CSE:
    scene Black with fade
    B "{i}The next stop of the day is Javits.{/i}"

    scene Javits Front Door with fade
    play sound "sounds/Sunny Day.mp3" loop

    B "{i}The Javits Lecture Hall hosts a lot of different classes on campus.{/i}"
    B "{i}It's a crowded, worn-down building that, much like the students here, seems ready to give up on life.{/i}"

    stop sound
    scene Javits Seats with dissolve
    # show Maria Casual Hdphn Dark at seat_r with dissolve
    show Ben Walk Bore Dark at center_stand, img_Scale(600, 960) with dissolve

    B "{i}There's never really enough space in these seats. I feel like I'm invading someone's bubble just by breathing.{/i}"
    show Ben Casual Sto Dark at seat_l_CSE, img_Scale(600, 960) with dissolve
    B "{i}At least nobody ever makes eye contact long enough to ever complain about it.{/i}"

    hide Ben
    # hide Maria
    with dissolve
    scene Javits Screen with dissolve
    show projector_javits with dissolve

    show UML Slide 1 with dissolve
    "Hello, everyone, and welcome to your senior year of Computer Science!"
    "I'm sure you've heard plenty of things about this class, but don't worry! It's way worse than you think!"
    show UML Slide 2 with dissolve
    "We like to take you guys by surprise, though, so we're starting with something simple - UML diagrams!"
    show UML Slide 3a with dissolve
    show UML Slide 3b with dissolve
    "You've all seen these before. Done right, they're an intuitive and visual way to explain code."
    show UML Slide 3c with dissolve
    "For those of you who don't remember the format - shame on you! This is not hard to remember!"
    show UML Slide 4a with dissolve
    show UML Slide 4b with dissolve
    $ renpy.pause(0.5)
    show UML Slide 4c with dissolve
    "I hope you at least remember how the lines work. You know, the ones that tell you what your code does?"
    show UML Slide 5a with dissolve
    $ renpy.pause(0.5)
    show UML Slide 5b with dissolve
    "Well, whether you remember or not, you'll be making UML diagrams for your first assignment."
    show UML Slide 5c with dissolve
    "Make sure to get this right - you'll have to follow the plans you set for the rest of the semester!"

    scene Javits Seats with dissolve
    show Ben Casual Sto Dark at seat_l_CSE, img_Scale(600, 960) with dissolve
    # show Maria Casual Hdphn Dark at seat_r with dissolve

    B "{i}I don't think I've ever seen a professor this...honest before.{/i}"
    B "{i}Well, as long as he's going to keep talking, I might as well get some work done.{/i}"

    # hide Ben
    # # hide Maria
    # with dissolve

    jump week_phase_1_check

label Week_0_HON:
    jump week_phase_2_check
