label interview:
    default projCountARS = 0
    default projCountCSE = 0
    default projScore = 0
    default arsTalked = False
    default cseTalked = False

    default question2Prompt = ""
    default interestARS = False
    default interestCSE = False

    default finalScore = 0

    # show Ben Interview Serious Spk with dissolve
    B "Alright - today's the day. Here's hoping I'm ready."

    scene Interview BG with fade

    # show Ben Interview Neutral at interview_l with dissolve
    # show Interviewer Back
    # show Raj Interview Neutral at interview_r
    # show Interviewer Front
    # with dissolve

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

        "{font='fonts/Courier Prime Bold.otf'}I've been building an art portolio.{/font}" if (progress[0] >= 2) and not arsTalked:
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
                $ projCountARS += 1

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
                $ projCountARS += 1

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
                $ projCountARS += 1

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
                $ projCountARS += 1

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

        "{font='fonts/Courier Prime Bold.otf'}I've been making my own website.{/font}" if (progress[1] >= 2) and not cseTalked:
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

                $ projCountCSE += 1

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

                $ projCountCSE += 1

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

                $ projCountCSE += 1

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

                $ projCountCSE += 1

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
    $ projScore += projCountARS
    $ projScore += projCountCSE

    # show Raj Interview Cheer at interview_r with dissolve
    R "Okay! So, from what I've seen so far, you seem to have quite a bit of work under your belt!"
    # show Raj Interview Neutral Spk at interview_r with dissolve
    if (projCountARS > projCountCSE):
        R "That's good, for front-end development - it helps to have experience making content."
        # show Raj Interview Guide at interview_r with dissolve
        R "So, correct me if I'm wrong, but your interest seems to be focused in art projects."
        $ question2Prompt = "So, correct me if I'm wrong, but your interest seems to be focused in art projects."
    elif (projCountARS < projCountCSE):
        R "If you've experience working with web programming, then that's very good."
        # show Raj Interview Guide at interview_r with dissolve
        R "I take it that your interest {i}is{/i} in web programming, correct?"
        $ question2Prompt = "I take it that your interest is in web programming, correct?"
    elif (projCountARS == projCountCSE) and (projCountARS != 0):
        R "I find it interesting that you have experience with both programming and graphic design."
        # show Raj Interview Guide at interview_r with dissolve
        R "Between the two, which would you say you lean more towards?"
        $ question2Prompt = "Between the two, which would you say you lean more towards?"

    # show Raj Interview Neutral at interview_r with dissolve
    menu:
        "{font='fonts/KaushanScript-Regular.otf'}[question2Prompt]{/font}"

        "I prefer my art projects." if projCountARS > 0:
            $ interestARS = True
            # show Ben Interview Neutral Spk at interview_l with dissolve
            B "I'd say that I prefer art projects, yeah."
            # show Ben Interview Neutral at interview_l with dissolve
            if (projCountARS > projCountCSE):
                # show Raj Interview Cheer at interview_r with dissolve
                R "I figured as much."
            elif (projCountARS < projCountCSE):
                # show Raj Interview Question at interview_r with dissolve
                R "Really? Based on what you've told me, I would have thought you'd be more interested in programming."
            else:
                # show Raj Interview Cheer at interview_r with dissolve
                R "Okay - that's good to know!"

        "I like web programming more." if projCountCSE > 0:
            $ interestCSE = True
            # show Ben Interview Neutral Spk at interview_l with dissolve
            B "I'd say I like web programming more."
            # show Ben Interview Neutral at interview_l with dissolve
            if (projCountARS > projCountCSE):
                # show Raj Interview Question at interview_r with dissolve
                R "That's interesting - with your experience, I thought you might have answered with \"art projects.\""
            elif (projCountARS < projCountCSE):
                # show Raj Interview Cheer at interview_r with dissolve
                R "Okay, that makes sense."
            else:
                # show Raj Interview Cheer at interview_r with dissolve
                R "Okay! I'll keep that in mind, then."

        "I like them both equally!" if (projCountARS > 0) and (projCountCSE > 0):
            $ interestARS = True
            $ interestCSE = True
            # show Ben Interview Neutral Spk at interview_l with dissolve
            B "I'd say that I like them both equally."
            # show Ben Interview Neutral at interview_l
            # show Raj Interview Question at interview_r
            # with dissolve
            R "Really? More often than not, the people we hire can only work with one or the other."
            if (projCountARS < projCountCSE) or (projCountARS < projCountCSE):
                # show Raj Interview Question at interview_r with dissolve
                R "Based off what you've told me, I would have assumed the same of you."
            else:
                # show Raj Interview Neutral Spk at interview_r with dissolve
                R "Though I guess that makes sense, from the work you've mentioned."

            if (progress[2] == 10):
                show text "{color=#00FF00}{size=30}{b}Interviewing: 3 / 3{/b}{/size}{/color}" at skill_check
                # show Raj Interview Neutral at interview_r
                # show Ben Interview Neutral Spk at interview_l
                # with dissolve
                B "I wouldn't necessarily say that I'm {i}good{/i} at working with both."
                # show Ben Interview Explain_1 at interview_l with dissolve
                B "Personally, I like to spend time thinking about how I can combine my skillsets."
                # show Ben Interview Neutral Spk at interview_l with dissolve
                B "I'm not the best at either content creation or web programming, so I try to use both whenever possible."
                # show Ben Interview Neutral at interview_l
                # show Raj Interview Cheer at interview_r
                # with dissolve
                R "Well, I'll be sure to keep that in mind!"

    # show Raj Interview Neutral Spk at interview_r with dissolve
    R "That actually leads nicely into my next question."
    # show Raj Interview Neutral Spk at interview_r with dissolve
    R "There's no shortage of companies looking for front-end web developers."
    # show Raj Interview Awkward Spk at interview_r with dissolve
    R "Most of them probably pay better, too."
    # show Raj Interview Neutral Spk at interview_r with dissolve
    R "With that in mind - why did you apply to Debugging Enterprises?"
    # show Raj Interview Neutral at interview_r with dissolve

    menu:
        "{font='fonts/KaushanScript-Regular.otf'}With that in mind - why did you apply to Debugging Enterprises?{/font}"

        "Because I want to develop my professional skills.":
            # show Ben Interview Neutral Spk at interview_l with dissolve
            B "I applied here because I wanted to develop my professional skills."
            # show Ben Interview Awkward Spk at interview_l with dissolve
            B "I'm well aware of my flaws, and my lack of work experience."
            # show Ben Interview Serious Spk at interview_l with dissolve
            B "But I still want to learn and improve."
            # show Ben Interview Serious Spk at interview_l with dissolve
            B "I don't just want to feel better about my skills - I want to {i}be{/i} better, and to do better work."
            # show Ben Interview Serious at interview_l
            # show Raj Interview Guide at interview_l
            # with dissolve
            R "And you believe Debugging Enterprises is the best place to start?"
            # show Raj Interview Neutral at interview_l
            # show Ben Interview Neutral Spk at interview_l
            # with dissolve
            B "Yes, sir."
            # show Ben Interview Neutral at interview_l
            jump question3

        "I'd like to work in marketing and digital communications." if (progress[0] == 10):
            # show Ben Interview Neutral Spk at interview_l with dissolve
            B "I applied here because I'd like to work in marketing and digital communications."
            if (not interestARS and interestCSE):
                # show Ben Interview Neutral at interview_l
                # show Raj Interview Question Spk at interview_r
                # with dissolve
                R "Hold on - I thought you preferred programming to content creation?"
                # show Raj Interview Question at interview_r
                # show Ben Interview Awkward Spk at interview_l
                # with dissolve
                B "Er, yeah, I do."
                # show Ben Interview Awkward Spk at interview_l with dissolve
                B "But I still think I would rather work with digital media."
                # show Ben Interview Awkward at interview_l
                # show Raj Interview Cheer at interview_r
                # with dissolve
                R "Oh, okay - I just wanted to clear that up!"

            elif (interestARS):
                # show Ben Interview Awkward at interview_l with dissolve
                B "I'm not quite as comfortable with programming as most other Computer Science majors."
                # show Ben Interview Explain_1 at interview_l with dissolve
                B "But on the other hand, I'm also more comfortable working with digital media than most."
                # show Ben Interview Neutral at interview_l with dissolve
                B "Given the chance, I'd like to put those skills to use."
                # show Ben Interview Neutral at interview_l
                # show Raj Interview Guide at interview_r
                # with dissolve
                R "And you believe Debugging Enterprises is the best place to start?"
                # show Raj Interview Neutral at interview_r
                # show Ben Interview Neutral Spk at interview_l
                # with dissolve
                B "Yes, sir."
                # show Ben Interview Neutral at interview_l

            jump question3

        "I wanted to learn more about web developement." if (progress[1] == 10):
            # show Ben Interview Neutral Spk at interview_l with dissolve
            B "I applied here because I want to learn more about web development."
            if (not interestCSE and interestARS):
                # show Ben Interview Neutral at interview_l
                # show Raj Interview Question Spk at interview_r
                # with dissolve
                R "Wait - I thought you preferred working with digital media instead of programming?"
                # show Raj Interview Question at interview_r
                # show Ben Interview Awkward Spk at interview_l
                # with dissolve
                B "Yes, I do."
                # show Ben Interview Awkward Spk at interview_l with dissolve
                B "But I still think I would rather work as a web developer."
                # show Ben Interview Awkward at interview_l
                # show Raj Interview Cheer at interview_r
                # with dissolve
                R "Alright, then - just wanted to make sure I had that right!"

            elif (interestCSE):
                # show Ben Interview Neutral at interview_l with dissolve
                B "I started learning about JavaScript and HTML a couple of years ago for a class."
                # show Ben Interview Explain_1 at interview_l with dissolve
                B "Those two languages have everything I want from programming - limitless potential, backed by the power of modern browsers."
                # show Ben Interview Awkward Spk at interview_l with dissolve
                B "There's a lot of trial and error, too, and learning about JavaScript has been pretty frustrating."
                # show Ben Interview Neutral Spk at interview_l with dissolve
                B "But I still want to learn more, because building my website was the most fun I've had in years."
                # show Ben Interview Neutral at interview_l
                # show Raj Interview Guide at interview_r
                # with dissolve
                R "And you believe Debugging Enterprises is the best place to learn more?"
                # show Raj Interview Neutral at interview_r
                # show Ben Interview Neutral Spk at interview_l
                # with dissolve
                B "Yes, sir."
                # show Ben Interview Neutral at interview_l

            jump question3

        "Because this company seemed like the best fit for me." if (progress[2] == 10):
            # show Ben Interview Neutral Spk at interview_l with dissolve
            B "I applied to Debugging Enterprises because this company seemed like the best fit for me."
            # show Ben Interview Explain_1 at interview_l with dissolve
            B "As I understand it, Debugging Enterprises does consultation work as well as in-house programming."
            # show Ben Interview Explain_2 at interview_l with dissolve
            B "It's been hiring recent graduates as interns, in the hopes of making them full-fledged developers."
            if (interestARS and not interestCSE):
                # show Ben Interview Explain_3 at interview_l with dissolve
                B "More recently, it's looking for digital artists, to help advertise for its clients and its software."
                # show Ben Interview Neutral Spk at interview_l with dissolve
                B "I know how to make digital content, and I know how to make a pitch."
                # show Ben Interview Neutral Spk at interview_l with dissolve
                B "If Debugging Enterprises wants to build a marketing team, then I know exactly where I would fit."
            elif (interestCSE and not interestARS):
                # show Ben Interview Explain_3 at interview_l with dissolve
                B "It's also started expanding further into web development, by building websites for its clients."
                # show Ben Interview Neutral Spk at interview_l with dissolve
                B "Applying here meant a chance at training with a respected company, and possibly working for its client base."
                # show Ben Interview Neutral Spk at interview_l with dissolve
                B "If Debugging Enterprises would have me, then I'd make it more than worth the time and effort."
            elif (interestARS and interestCSE):
                # show Ben Interview Explain_3 at interview_l with dissolve
                B "And it's also looking into making training videos, in the same vein as W3Schools or Khan Academy."
                # show Ben Interview Neutral Spk at interview_l with dissolve
                B "I'm familiar with a lot of the web development stack, and I know how to explain it to people who aren't."
                # show Ben Interview Neutral Spk at interview_l with dissolve
                B "If Debugging Enterprises wants to teach people to program, then I'd love to be a part of that."

label question3:
    # show Ben Interview Neutral at interview_l with dissolve
    # show Raj Interview Guide at interview_r with dissolve
    R "So what is it about yourself, then, that makes you a good fit for this company?"
    # show Raj Interview Neutral at interview_r with dissolve
    menu:
        "{font='fonts/KaushanScript-Regular.otf'}So, what is it about yourself, then, that makes you a good fit for this company?{/font}"

        "My work ethic.":

        "My skillset.":

        "My ability to communicate and cooperate." if (progress[2] == 10):



label final_Score:
    scene Black with fade
    show

    return
