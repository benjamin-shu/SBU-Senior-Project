# ==============================================================================
# Game starts here.
# ==============================================================================
label start:
    # jump schedule_show
    scene West F 301 Hallway with fade

    show static with dissolve
    show Ben Intro Cas Sto Dark at center behind static with dissolve
    play sound "sounds/Record Player Static.mp3" loop
    B "..."

    show Ben Intro Cas Sto Spk with dissolve
    B "...okay, is this piece of junk recording?"

    show Ben Intro Cas Fru Spk with dissolve
    B "...no, I suppose not."
    show Ben Intro Cas Sto Spk Dark with dissolve
    B "Alright, guess I'll just have to cut this-"

    show fadeInOut
    hide static with dissolve
    stop sound

    window hide
    show Ben Intro Hel Spk:
    show take1:
    with dissolve
    play sound "sounds/Banana Slap.mp3"
    $ renpy.pause(1.0)
    window show

    play music "sounds/Ben/Loopster.mp3" loop
    B "Hey, guys. My name is Benjamin Shu."
    B "I'm in my senior year here, and-"
    play music "sounds/Phone Vibrating.mp3" loop
    show Ben Intro Hel Awk with dissolve
    B "..."
    show Ben Intro Hel Fru with dissolve
    play sound "sounds/Censored Beep.mp3"
    B "...son of a {i}bitch{/i}!"
    show Ben Intro Pho Chk Fru Spk Dark with dissolve
    B "Why {i}now{/i}?"
    stop music
    play sound "sounds/Checkout Scanner Beep.mp3"
    show Ben Intro Pho Spk Dark with dissolve
    B "Hello?"
    B "No, everything's fine here. I finished unpacking a while ago."
    play sound "sounds/Cartoon Voice Baritone.mp3" fadeout 1.0
    show Ben Intro Pho Dark with dissolve
    B "..."
    show Ben Intro Pho Spk Dark with dissolve
    B "Okay. Where is this internship?"
    play sound "sounds/Cartoon Voice Baritone.mp3" fadeout 1.0
    show Ben Intro Pho Dark with dissolve
    B "..."
    show Ben Intro Pho Spk Dark with dissolve
    B "...no, I don't really have any experience with that."
    play sound "sounds/Cartoon Voice Baritone.mp3" fadeout 1.0
    show Ben Intro Pho Dark with dissolve
    B "..."
    show Ben Intro Pho Spk Dark with dissolve
    B "I know. I'll look in a bit."
    B "Yeah, I know. I'll go see an advisor soon."
    play sound "sounds/Cartoon Voice Baritone.mp3" fadeout 1.0
    show Ben Intro Pho Fru Spk Dark with dissolve
    B "...{i}yes{/i}, I know. I won't let it happen again."
    show Ben Intro Pho Spk Dark with dissolve
    B "Okay. I will. Bye, mom."
    play sound "sounds/Checkout Scanner Beep.mp3"
    show Ben Intro Pho Chk Dark with dissolve
    B "..."

    window hide
    show Ben Intro Cas Sto Spk:
    show take2:
    with dissolve
    play sound "sounds/Banana Slap.mp3"
    $ renpy.pause(1.0)
    window show

    B "Okay, here goes. From the top..."

    window hide
    show projector
    hide Ben with dissolve

    window show
    play music "sounds/Ben/Loopster.mp3" fadein 1.0 loop

    $ renpy.pause(2.0)

    show Intro Slide 1 with dissolve
    B Intro Hel Spk Si "Hello! My name is Benjamin Shu."
    show Intro Slide 2 with dissolve
    B Intro Hands Sml Si "I am a senior computer science major, here at Stony Brook..."
    show Intro Slide 3 with dissolve
    B Intro Hands Ddpn "...and like a lot of people my age, I have no idea what I'm doing with my life."
    B Intro Cas Neut Spk Si "Recently, I've started thinking that this {i}might{/i} be a problem."
    show Intro Slide 4 with dissolve
    B Intro Cas Sto Spk Si "I can't say that I've accomplished much over the last four years..."
    B "...but hopefully, this semester is where I can turn things around."
    show Intro Slide 5 with dissolve
    B Intro Hands Ddpn Si "The great and terrifying thing about my life is that I don't know what comes next."
    B "Without a job lined up, there's no security or guarantees."
    B Intro Hands Sml Si "But that also means there's a lot of possibilities."

    window hide
    hide Intro Slide 5 with dissolve
    hide projector with Dissolve(1.0)
    show Ben Intro Cas Neut Spk with dissolve
    window show

    B "I'm going to try to keep that in mind this semester."
    B "So, to whoever you are watching, wish me luck!"
    stop music fadeout 1.0
    hide Ben with dissolve
    scene Black with fade

    jump schedule_show
