label interview:
    default finalScore = 0
    default projCount = 0
    default arsTalked = False
    default cseTalked = False

    # B "Alright - today's the day. Here's hoping I'm ready."

    # scene Interview with fade

    # show Raj Interview Neutral at interview_r with dissolve
    # show Ben Interview Neutral at interview_l with dissolve

    # show Raj Interview Neutral Spk at interview_r with dissolve
    R "It's very good to finally meet you, Benjamin!"
    $ r_name = "Rajesh"
    # show Raj Interview Cheer Spk at interview_r with dissolve
    R "My name is Rajesh - I'm the person who spoke to you over the phone."
    # show Raj Interview Neutral Spk at interview_r with dissolve
    R "I'm glad you could make it today."
    # show Raj Interview Neutral at interview_r
    # show Ben Interview Neutral Spk at interview_l
    # with dissolve
    B "Likewise - I'm glad I could be here."
    # show Ben Interview Neutral at interview_l with dissolve

    $ check_num = (progress[2] if (progress[2] > 0) else 0) if (progress[2] < 2) else 2
    if (check_num == 2):
        show text "{color=#00FF00}{size=30}{b}Resume: [check_num] / 2{/b}{/size}{/color}" at skill_check
        # show Raj Interview Cheer Spk at interview_r with dissolve
        R "Before we begin, I really must say - I like the way your resume is formatted!"
        # show Raj Interview Awkward Spk at interview_r with dissolve
        R "So many applicants think that I {i}like{/i} reading tiny text crammed into a single page!"
        # show Raj Interview Neutral Spk at interview_r with dissolve
        R "Seeing yours made for a...{i}refreshing{/i} change of pace."
        # show Raj Interview Neutral at interview_r
        # show Ben Interview Neutral Spk at interview_l
        # with dissolve
        B "Oh! Well, that's good to hear. I'm glad you liked it!"
        # show Ben Interview Neutral at interview_l with dissolve
        $ finalScore += 1
    else:
        # show Raj Interview Neutral Spk at interview_r with dissolve
        R "Now, before we begin, I wanted to ask a question about your resume."
        show Dimmed
        show resume_1a
        with dissolve
        # show Raj Interview Awkward Spk at interview_r with dissolve
        show text "{color=#FF0000}{size=30}{b}Resume: [check_num] / 2{/b}{/size}{/color}" at skill_check
        R "I have to say, this a...unique resume compared what we usually receive."
        R "Am I correct in assuming that you've no professional experience?"
        # show Raj Interview Awkward at interview_r
        # show Ben Interview Awkward Spk at interview_l
        # with dissolve
        B "Uh, yes, that would be correct."
        B "I'm sorry about the state of my resume - it's been a busy semester."
        hide resume_1a
        hide Dimmed
        with dissolve
        # show Raj Interview Cheer Spk at interview_r
        # show Ben Interview Awkward at interview_l
        # with dissolve
        R "Oh, no, I completely understand."

    # show Raj Interview Neutral Spk at interview_r with dissolve
    R "I also just wanted to confirm - you are a senior Computer Science major at Stony Brook, correct?"
    # show Raj Interview Neutral at interview_r
    # show Ben Interview Neutral Spk at interview_l
    # with dissolve
    B "Yes, that's correct."

    $ check_num = (progress[2] - 2 if (progress[2] - 2 > 0) else 0) if (progress[2] < 4) else 2
    if (check_num == 2):
        # show Raj Interview Cheer Spk at interview_r
        # show Ben Interview Neutral at interview_l
        # with dissolve
        show text "{color=#00FF00}{size=30}{b}LinkedIn: [check_num] / 2{/b}{/size}{/color}" at skill_check
        R "Oh, good! Your LinkedIn profile was correct, then. That makes the paperwork easier."
        $ finalScore += 1
    else:
        # show Raj Interview Cheer Spk at interview_r
        # show Ben Interview Neutral at interview_l
        # with dissolve
        show text "{color=#FF0000}{size=30}{b}LinkedIn: [check_num] / 2{/b}{/size}{/color}" at skill_check
        R "Okay, good - I wasn't sure, since I didn't see much on your LinkedIn profile."
        # show Raj Interview Neutral Spk at interview_r
        R "You may want to update that, by the way."

    # show Raj Interview Neutral Spk at interview_r with dissolve
    R "Now that that's out of the way, let's get to the actual interview questions."
    # show Raj Interview Cheer Spk at interview_r with dissolve
    R "I'm not trying to scare you or anything - this is just to get a sense of who you are."
    # show Raj Interview Guide at interview_r with dissolve
    R "So, just as a start, could you tell me about some previous projects you've done?"
    # show Raj Interview Neutral at interview_r with dissolve

label question1:
    menu:
        "{font='fonts/KaushanScript-Regular.otf'}So, just as a start, could you tell me about some previous projects you've done?{/font}"

        "{font='fonts/Courier Prime Bold.otf'}[[Art]] I've been building an art portolio.{/font}" if (progress[0] >= 2) and not arsTalked:
            $ projCount = 0

            # show Ben Interview Neutral Spk at interview_l with dissolve
            if cseTalked:
                B "I've also been building a portfolio out of projects from an old art class."
            else:
                B "Lately, I've been making a portfolio of art projects from a class I took."

            $ check_num = (progress[0] if (progress[0] > 0) else 0) if (progress[0] < 2) else 2
            if (check_num == 2):
                show text "{color=#00FF00}{size=30}{b}{b}Composition: [check_num] / 2{/b}{/b}{/size}{/color}" at skill_check
                if (progress[2] > 6):
                    B "The first thing I worked on was an animated demonstration on arranging and improving drawings."
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "I wanted to show people how to make better drawings rather than boring them with lots of text."
                else:
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "I started with a PowerPoint presentation about the visual elements of composition."
                $ projCount += 1

            $ check_num = (progress[0] - 2 if (progress[0] - 2 > 0) else 0) if (progress[0] < 4) else 2
            if (check_num == 2):
                show text "{color=#00FF00}{size=30}{b}Typography: [check_num] / 2{/b}{/size}{/color}" at skill_check
                if (progress[2] > 6):
                    # show Ben Interview Explain_2 at interview_l with dissolve
                    B "I also made a poster using only the letters from \"Graphic Design\"."
                    # show Ben Interview Explain_2 at interview_l with dissolve
                    B "My class assigned that as a way to get us thinking creatively about text."
                    # show Ben Interview Neutral Spk at interview_l with dissolve
                    B "I broke it down into an instruction set, to demonstrate how I did it."
                else:
                    # show Ben Interview Explain_2 at interview_l with dissolve
                    B "Then I did a typography challenge where I could only use text elements for a composition."
                $ projCount += 1

            $ check_num = (progress[0] - 4 if (progress[0] - 4 > 0) else 0) if (progress[0] < 7) else 3
            if (check_num == 3):
                show text "{color=#00FF00}{size=30}{b}Poster Design: [check_num] / 3{/b}{/size}{/color}" at skill_check
                if (progress[2] > 6):
                    # show Ben Interview Neutral Spk at interview_l with dissolve
                    B "For the next project, we were told to pick a favorite concert or show and make a poster for it."
                    # show Ben Interview Explain_3 at interview_l with dissolve
                    B "I drew out each piece of the poster, as well as how they were supposed to come together."
                else:
                    # show Ben Interview Explain_3 at interview_l with dissolve
                    B "After that, I made a fictional poster design for a comedy show by Bo Burnham."
                $ projCount += 1

            $ check_num = (progress[0] - 7 if (progress[0] - 7 > 0) else 0) if (progress[0] < 10) else 3
            if (check_num == 3):
                show text "{color=#00FF00}{size=30}{b}Video Editing: [check_num] / 3{/b}{/size}{/color}" at skill_check
                if (progress[2] > 6):
                    # show Ben Interview Neutral Spk at interview_l with dissolve
                    B "The biggest art project I did was a \"Self-Portrait\" video."
                    # show Ben Interview Explain_4 at interview_l with dissolve
                    B "We were supposed to summarize our personalities and experiences in under two minutes."
                    # show Ben Interview Explain_4 at interview_l with dissolve
                    B "I did that with video clips of myself writing code and making pixel art."
                else:
                    # show Ben Interview Explain_4 at interview_l with dissolve
                    B "The last thing I did was a quick video project, as a sort of \"Self-Portrait,\" or introduction for myself."
                $ projCount += 1

            if (projCount <= 1):
                $ finalScore += 1
            elif (projCount == 3):
                $ finalScore += 4
            else:
                $ finalScore += projCount

            $ arsTalked = True

            if (progress[2] > 6):
                show text "{color=#00FF00}{size=30}{b}Presentation: 3 / 3{/b}{/size}{/color}" at skill_check
                if (progress[0] == 10):
                    # show Ben Interview Awkward Spk at interview_l with dissolve
                    B "Those was it as far as the big projects I did for that art class."
                    # show Ben Interview Neutral Spk at interview_l with dissolve
                    B "Given more time, I think I'd like to combine them into an instructional pamphlet."
                    # show Ben Interview Neutral at interview_l
                    # show Raj Interview Question Spk at interview_r
                    # with dissolve
                    R "Really? Why that, specifically?"
                    # show Ben Interview Neutral Spk at interview_l
                    # show Raj Interview Question at interview_r
                    # with dissolve
                    B "A pamphlet would condense everything we learned into something short and beginner-friendly."
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "It would be easily understood, and it might get more people interested in graphic design."
                    # show Ben Interview Neutral at interview_l
                    # show Raj Interview Cheer at interview_r
                    # with dissolve
                    R "Well, it's good that you're thinking about things like that!"
                else:
                    # show Ben Interview Awkward Spk at interview_l with dissolve
                    B "I was planning on doing more art projects, but this semester's been pretty busy."
            else:
                # show Ben Interview Neutral Spk at interview_l with dissolve
                B "And, yeah, that about covers all of my art projects."

            # show Ben Interview Neutral at interview_l
            # show Raj Interview Guide at interview_r
            # with dissolve
            R "Are there any other projects you'd like to tell me about?"
            # show Raj Interview Neutral at interview_r with dissolve
            jump question1

        "{font='fonts/Courier Prime Bold.otf'}[[Web]] I've been making my own website.{/font}" if (progress[1] >= 2) and not cseTalked:
            $ projectCount = 0

            # show Ben Interview Neutral Spk at interview_l with dissolve
            if arsTalked:
                B "I've also been working on my own personal website."
            else:
                B "I've been making a personal website as a portfolio of sorts."

            $ check_num = (progress[1] if (progress[1] > 0) else 0) if (progress[1] < 2) else 2
            if (check_num == 2):
                show text "{color=#00FF00}{size=30}{b}UML Diagrams: [check_num] / 2{/b}{/size}{/color}" at skill_check
                if (progress[2] > 6):
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "I started by making UML diagrams of everthing it would need - web pages, content, and a server."
                    # show Ben Interview Neutral Spk at interview_l with dissolve
                    B "I wanted to make the plans detailed, so that anyone could understand how it was built and how it worked."
                else:
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "The first thing I did was draw a bunch of mock-ups to plan out the website."

                $ projectCount += 1

            $ check_num = (progress[1] - 2 if (progress[1] - 2 > 0) else 0) if (progress[1] < 4) else 2
            if (check_num == 2):
                show text "{color=#00FF00}{size=30}{b}HTML Designs: [check_num] / 2{/b}{/size}{/color}" at skill_check
                if (progress[2] > 6):
                    # show Ben Interview Neutral Spk at interview_l with dissolve
                    B "The next stage was to design each individual page on the web site."
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "I wrote HTML documents for each one, then added CSS to make them look nicer."
                else:
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "After that, I made each of the pages in HTML and CSS."

                $ projectCount += 1

            $ check_num = (progress[1] - 4 if (progress[1] - 4 > 0) else 0) if (progress[1] < 7) else 3
            if (check_num == 3):
                show text "{color=#00FF00}{size=30}{b}Digital Content: [check_num] / 3{/b}{/size}{/color}" at skill_check
                if (progress[2] > 6):
                    # show Ben Interview Neutral Spk at interview_l with dissolve
                    B "Once the pages were made, I needed to add links for displaying content."
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "With those links, I could add images, code, and videos from my Google Drive account."
                else:
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "The next step was to add actual content to each of the pages."

                $ projectCount += 1

            $ check_num = (progress[1] - 7 if (progress[1] - 7 > 0) else 0) if (progress[1] < 10) else 3
            if (check_num == 3):
                show text "{color=#00FF00}{size=30}{b}Web Development: [check_num] / 3{/b}{/size}{/color}" at skill_check
                if (progress[2] > 6):
                    # show Ben Interview Neutral Spk at interview_l with dissolve
                    B "The final step was to make an actual server, so people could view the pages."
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "I wrote an application on Node.js, and then got that hosted on Google Firebase."
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "It's online now - I can give you the address, if you're interested."
                    # show Ben Interview Neutral at interview_l
                    # show Raj Interview Cheer at interview_r
                    # with dissolve
                    R "Really? I think I might have a look later, then!"
                else:
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "Finally, I wrapped everything up in a Node.js application and posted it on Google Firebase."

                $ projectCount += 1

            if (projCount <= 1):
                $ finalScore += 1
            elif (projCount == 3):
                $ finalScore += 4
            else:
                $ finalScore += projCount

            $ cseTalked = True

            if (progress[2] > 6):
                show text "{color=#00FF00}{size=30}{b}Presentation: 3 / 3{/b}{/size}{/color}" at skill_check
                if (progress[1] == 10):
                    # show Ben Interview Explain_1 at interview_l with dissolve
                    B "Overall, it wasn't too bad - it was definitely easier than the CS projects at Stony Brook."
                    # show Ben Interview Explain_2 at interview_l with dissolve
                    B "But it was nice, to essentially develop an app from start to finish."
                    # show Ben Interview Neutral at interview_l
                    # show Raj Interview Neutral Spk at interview_r
                    # with dissolve
                    R "It certainly sounds like an experience!"
                    # show Raj Interview Cheer at interview_r with dissolve
                    R "I've heard the Computer Science major described as \"a slow and painful death.\""
                    # show Raj Interview Neutral at interview_r
                    # show Ben Interview Neutral Spk at interview_l
                    # with dissolve
                    B "Whoever said it was not wrong."
                else:
                    # show Ben Interview Awkward Spk at interview_l
                    B "Sadly, I didn't get much further than that - the actual website isn't online."
                    # show Ben Interview Awkward at interview_l
                    # show Raj Interview Neutral Spk at interview_r
                    # with dissolve
                    R "Aw, well that's a shame. I'm sure it'll look great when you're finished!"
            else:
                # show Ben Interview Neutral Spk at interview_l with dissolve
                B "And that covers all the coding I've done so far."

            # show Ben Interview Neutral at interview_l
            # show Raj Interview Guide at interview_r
            # with dissolve
            R "So, is there anything else you'd like to tell me about?"
            jump question1

        "I haven't had the time to do much else." if (arsTalked or cseTalked):
            # show Ben Interview Neutral Spk at interview_l with dissolve
            B "Those were all of the projects I've done recently."
            # show Ben Interview Awkward Spk at interview_l with dissolve
            B "Between exams and midterms, I haven't had time to do much else."
            # show Ben Interview Awkward at interview_l
            # show Raj Interview Cheer at interview_r
            # with dissolve
            R "Don't worry - I'm not judging you for anything!"
            # show Raj Interview Neutral Spk at interview_r with dissolve
            R "I just thought I'd ask."
            
            jump question2

label question2:
    R ""

label final_Score:

    return
