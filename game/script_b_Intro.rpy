# Game starts here.
label start:
    scene West F 301 Hallway with fade

    show Ben Intro Cas Sto Dark at center with dissolve
    B "..."

    show Ben Intro Cas Sto Spk with dissolve
    B "...okay, is this thing recording?"

    show Ben Intro Cas Fru Spk with dissolve
    B "...ah crap, it is!"
    show Ben Intro Cas Sto Spk Dark with dissolve
    B "Okay, going to have to cut this-"

    window hide
    show Ben Intro Hel Spk:
    show take1:
    with dissolve
    $ renpy.pause(1.0)
    window show

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
    show Ben Intro Pho Chk Dark with dissolve
    B "..."

    window hide
    show Ben Intro Cas Sto Spk:
    show take2:
    with dissolve
    $ renpy.pause(1.0)
    window show

    B "Okay, here goes. From the top..."
    show Ben Intro Cas Brth with dissolve
    B "..."

    window hide
    show projector
    hide Ben with dissolve

    $ renpy.pause(4)

    window show
    play music "sounds/Ben/Loopster.mp3" fadein 1.0 loop

    show Intro Slide 1 with dissolve
    B Intro Hel Spk Si "Hello! My name is Benjamin Shu."
    show Intro Slide 2 with dissolve
    B Intro Hands Sml Si "I am a senior computer science major, here at Stony Brook..."
    show Intro Slide 3 with dissolve
    B Intro Hands Ddpn "...and like a lot of people my age, I have no idea what I'm doing with my life."
    B Intro Cas Neut Spk Si "Recently, I've started thinking that this {i}might{/i} be a problem."
    show Intro Slide 4 with dissolve
    B Intro Cas Sto Spk Si "I can't say that I've accomplished much over the last four years..."
    B "...but I wanted to make something of my time here before I left."
    show Intro Slide 5 with dissolve
    B Intro Hands Ddpn Si "So I’m going to try and turn the disorganized mess in my head into something coherent."
    B "Something people might actually {i}care{/i} about."
    B Intro Hands Sml Si "And hopefully, something worth their time."

    window hide
    hide Intro Slide 5 with dissolve
    hide projector with Dissolve(1.0)
    show Ben Intro Cas Neut Spk with dissolve
    window show

    B "With that in mind, welcome to the show. I hope you enjoy your stay."
    stop music fadeout 1.0
    hide Ben with dissolve
    scene Black with fade

    jump Day1
