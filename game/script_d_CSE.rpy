label CSE_sequences:
    # Retrieve index for CSE data using codes[].
    default CSE_index = codes.index("CSE")
    # Retrive player's current progress in this skill tree.
    default CSE_progress = progress[CSE_index]

    # Set scene in Javits 100.
    scene Javits Screen with fade

    #$ renpy.jump("CSE_sequences_%d" % (CSE_progress))

label CSE_sequences_1:
    show projector_javits with dissolve

    show uml_1 with dissolve
    B "Not too long ago, you had an idea for building your own website."
    B "To start planning it out, you’ve started making diagrams to outline what each page will have."
    hide uml_1 with dissolve

    hide projector_javits with dissolve

    # $ i += 1
    # jump show_skills

label CSE_sequences_2:
    show projector_javits with dissolve

    show uml_2 with dissolve
    B "You decide to add diagrams for other pieces of the website - the server, the design, and the interactive pieces."
    B "You’re done with the planning stage, and you’re now ready to begin coding."
    hide uml_2 with dissolve

    hide projector_javits with dissolve

    # $ i += 1
    # jump show_skills

label CSE_sequences_3:
    show Dimmed
    show Laptop
    with dissolve

    show html_1 with dissolve
    B "The plan calls for four pages - a home page, a bio, a photo gallery, and a projects page."
    B "You start by making a separate HTML document for each page and laying out the important elements."
    hide html_1 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    # $ i += 1
    # jump show_skills

label CSE_sequences_4:
    show Dimmed
    show Laptop
    with dissolve

    show html_2 with dissolve
    B "Basic HTML works, but doesn’t really look very good - to fix this, you add some CSS styling."
    B "Now that your pages are set up, you’re free to put up more content."
    hide html_2 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    # $ i += 1
    # jump show_skills

label CSE_sequences_5:
    show Dimmed
    show Laptop
    with dissolve

    show content_1 with dissolve
    B "Having the web pages is all well and good, but it doesn’t mean much if there’s no actual content."
    B "Despite the disgust you feel at looking at your old artwork, you decide to add links to files from your Google Drive portfolio."
    hide content_1 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    # $ i += 1
    # jump show_skills

label CSE_sequences_6:
    show Dimmed
    show Laptop
    with dissolve

    show content_2a
    show content_2b
    with dissolve
    B "With the power of JavaScript, you’ve added a scrolling gallery feature - now visitors can view all of your work at once."
    B "You’re not sure how to feel about that, but decide to keep the feature regardless."
    hide content_2a
    hide content_2b
    with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    # $ i += 1
    # jump show_skills

label CSE_sequences_7:
    show Dimmed
    show Laptop
    with dissolve

    show content_3 with dissolve
    B "You decide to upload some of your old code, along with written explanations - hopefully, no one else will make the same mistakes you did."
    B "All that’s left now is to put your website on the Internet."
    hide content_3 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    # $ i += 1
    # jump show_skills

label CSE_sequences_8:
    show Dimmed
    show Laptop
    with dissolve

    show web_1 with dissolve
    B "To get your website online, you write a Node.js server application - if you can get this hosted, then anyone can see it."
    B "You’re not sure if you should be excited or terrified by that, so you decide to be both."
    hide web_1 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    # $ i += 1
    # jump show_skills

label CSE_sequences_9:
    show Dimmed
    show Laptop
    with dissolve

    show web_2 with dissolve
    B "To make your website’s pages load faster, you spend some time deleting unnecessary characters from every text file you made."
    B "This is exactly as tedious as it sounds (and could probably be done faster, if you were smarter)."
    hide web_2 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    # $ i += 1
    # jump show_skills

label CSE_sequences_10:
    show Dimmed
    show Laptop
    with dissolve

    show web_3 with dissolve
    B "You eventually decide to use Microsoft Azure, because of its reputation and support for Node.js (and because you have a free account)."
    B "After hours upon hours of work, you’ve finally put yourself out on the Internet for everyone to see."
    hide web_3 with dissolve

    hide Dimmed
    hide Laptop
    with dissolve

    # $ i += 1
    # jump show_skills
