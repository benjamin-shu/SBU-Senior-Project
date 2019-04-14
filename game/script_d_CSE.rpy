label CSE_sequences:
    # Retrieve index for CSE data using codes[].
    default CSE_index = codes.index("CSE")

    # Set scene in Javits 100.
    scene Javits Screen with fade

    $ renpy.jump("CSE_sequences_%d" % (progress[CSE_index]))

label CSE_sequences_1:
    show projector_javits with dissolve

    show uml_1 with dissolve
    B "Not too long ago, I had an idea for building my own website."
    B "To start planning it out, I’ve started making diagrams to outline what each page will have."
    hide uml_1 with dissolve

    hide projector_javits with dissolve

    $ i += 1
    jump show_skills

label CSE_sequences_2:
    show projector_javits with dissolve

    show uml_2 with dissolve
    B "I decided to add diagrams for other pieces of the website - the server, the design, and the interactive pages."
    show text "{color=#000000}{size=30}UML Diagrams: 2 / 2{/size}{/color}" at skill_check
    B "I'm done with the planning, and now I'm ready to begin coding."
    hide uml_2 with dissolve

    hide projector_javits with dissolve

    $ i += 1
    jump show_skills

label CSE_sequences_3:
    show Dimmed
    show Laptop
    with dissolve

    show html_1 with dissolve
    B "The plan calls for four pages - a home page, a bio, a photo gallery, and a projects page."
    B "I started by making a separate HTML document for each page and laying out the important elements."
    hide html_1 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    $ i += 1
    jump show_skills

label CSE_sequences_4:
    show Dimmed
    show Laptop
    with dissolve

    show html_2 with dissolve
    B "Basic HTML works, but doesn’t really look very good - to fix this, I've added some CSS."
    show text "{color=#000000}{size=30}HTML Designs: 2 / 2{/size}{/color}" at skill_check
    B "Now that the pages are set up, I'm free to put up some real content."
    hide html_2 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    $ i += 1
    jump show_skills

label CSE_sequences_5:
    show Dimmed
    show Laptop
    with dissolve

    show content_1 with dissolve
    B "Having the web pages is all well and good, but it doesn’t mean much if there’s no actual content."
    B "Despite the disgust I feel looking at my old artwork, I've added links to my Google Drive portfolio."
    hide content_1 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    $ i += 1
    jump show_skills

label CSE_sequences_6:
    show Dimmed
    show Laptop
    with dissolve

    show content_2a
    show content_2b
    with dissolve
    B "With the power of JavaScript, I’ve added a scrolling gallery feature - now visitors can see all of my work at once."
    B "I’m not sure how to feel about that, but I'll keep the feature regardless."
    hide content_2a
    hide content_2b
    with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    $ i += 1
    jump show_skills

label CSE_sequences_7:
    show Dimmed
    show Laptop
    with dissolve

    show content_3 with dissolve
    B "I've uploaded some of my old code, along with written explanations - hopefully, no one else will make the same mistakes I did."
    show text "{color=#000000}{size=30}Digital Content: 3 / 3{/size}{/color}" at skill_check
    B "And with that, all that’s left now is to put my website on the Internet."
    hide content_3 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    $ i += 1
    jump show_skills

label CSE_sequences_8:
    show Dimmed
    show Laptop
    with dissolve

    show web_1 with dissolve
    B "To get my website online, I wrote a Node.js server application - if this gets hosted, then anyone online can see it."
    B "I'm not sure if I should be excited or terrified by that, so I'll just be both."
    hide web_1 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    $ i += 1
    jump show_skills

label CSE_sequences_9:
    show Dimmed
    show Laptop
    with dissolve

    show web_2 with dissolve
    B "To make my website’s pages load faster, I spent some time deleting unnecessary text from every file I made."
    B "This is exactly as tedious as it sounds (and could probably be done faster, if I were smarter)."
    hide web_2 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    $ i += 1
    jump show_skills

label CSE_sequences_10:
    show Dimmed
    show Laptop
    with dissolve

    show web_3 with dissolve
    B "I eventually decided to use Microsoft Azure, because of its reputation and support for Node.js (and because I have a free account)."
    show text "{color=#000000}{size=30}Web Development: 3 / 3{/size}{/color}" at skill_check
    B "After hours upon hours of work, I’ve finally put myself out on the Internet for everyone to see."
    B "I'll try to contain my joy."
    hide web_3 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    $ i += 1
    jump show_skills
