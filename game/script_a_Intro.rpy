label start:
    scene West F 301C with fade

    play music "sounds/Snoring.mp3" loop

    $ renpy.pause(5.0)

    play sound "sounds/Phone Ringing 8x.mp3" loop
    stop music

    $ renpy.pause(2.0)

    B "Just a minute..."
    B "Just let me get out of -"

    play sound "sounds/Bounce.mp3"

    "THUD" with vpunch
    play sound "sounds/Phone Ringing 8x.mp3" loop

    $ renpy.pause(2.0)

    # show Ben Phone Check Sleepy with dissolve
    B "Who the hell is calling me {i}now{/i}?"
    # show Ben Phone Talk Sleepy with dissolve
    play sound "sounds/Checkout Scanner Beep.mp3"
    B "Hello?"
    play sound "sounds/Cartoon Voice Baritone.mp3"
    R "Hello! I'm calling from Debugging Enterprises about a job application."
    # show Ben Phone Talk Panic with dissolve
    R "Am I speaking to Benjamin Shu?"
    # show Ben Phone Talk Panic Spk with dissolve
    B "Yes! Hello! It's good to hear back from you!"
    B "So, um...how can I help you?"
    # show Ben Phone Talk Panic with dissolve
    play sound "sounds/Cartoon Voice Baritone.mp3"
    R "Well, I'm just calling to let you know that you've been selected for an interview!"
    R "Would you be available on April 1st to come to our offices?"
    # show Ben Phone Talk Panic Spk with dissolve
    B "Oh! Yeah! I mean, that would be great!"
    # show Ben Phone Talk Panic with dissolve
    play sound "sounds/Cartoon Voice Baritone.mp3"
    R "Excellent! You'll be receiving an email with more information after this call."
    R "We look forward to speaking with you soon. Have a nice day!"
    play sound "sounds/Checkout Scanner Beep.mp3"
    # show Ben Phone Check Panic with dissolve
    $ renpy.pause(3.0)
    # show Ben Phone Check Curse with dissolve
    play sound "sounds/Censored Beep.mp3"
    $ renpy.pause(1.0)

    hide Ben with dissolve
    scene Black with fade

    jump day_start
