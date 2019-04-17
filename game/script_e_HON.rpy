label HON_sequences:
    # Retrieve index for HON data using codes[].
    default HON_index = codes.index("HON")

    # Set scene in West F 301C.
    scene West F 301C with fade

    $ renpy.jump("HON_sequences_%d" % (progress[HON_index]))

label HON_sequences_1:
    show projector_emedia with dissolve

    show resume_1a
    with dissolve
    B "I had a look at my resume, and it...left a lot to be desired."
    hide resume_1a
    show resume_1b
    with dissolve
    show text "{color=#000000}{size=30}{b}Resume: 1 / 2{/b}{/size}{/color}" at skill_check
    B "With help from the Career Center, though, I've made the format more presentable."
    hide resume_1b
    with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label HON_sequences_2:
    show projector_emedia with dissolve

    show resume_1b
    with dissolve
    B "A counselor from the Career Center was nice enough to give more tips on resume formatting."
    hide resume_1b
    show resume_2a
    with dissolve
    B "Current contact information and most recent work experience goes up top..."
    hide resume_2a
    show resume_2b
    with dissolve
    B "...and skills and extracurriculars goes at the bottom (if they actually read the whole thing)."
    show text "{color=#000000}{size=30}{b}Resume: 2 / 2{/b}{/size}{/color}" at skill_check
    B "Now, I have a resume that I'm not totally ashamed of!"
    hide resume_2b
    with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label HON_sequences_3:
    show Dimmed
    show Laptop
    with dissolve

    show linkedin_1
    with dissolve
    B "A few of my friends explained the importance of a LinkedIn profile, and told me to make sure mine is complete."
    hide linkedin_1
    show linkedin_1a
    with dissolve
    show text "{color=#000000}{size=30}{b}LinkedIn: 1 / 2{/b}{/size}{/color}" at skill_check
    B "At their insistence, I’ve added a profile picture, a cover photo, and a short bio."
    hide linkedin_1a
    with dissolve

    hide Laptop
    hide Dimmed
    with dissolve

    $ i += 1
    jump show_skills

label HON_sequences_4:
    show Dimmed
    show Laptop
    with dissolve

    show linkedin_2a
    with dissolve
    B "In order to shut my friends up, I’ve also uploaded my resume to my LinkedIn profile."
    hide linkedin_2a
    show linkedin_2b
    with dissolve
    show text "{color=#000000}{size=30}{b}LinkedIn: 2 / 2{/b}{/size}{/color}" at skill_check
    B "Doing so built the rest of my profile for me, so that employers get a better sense of who they're rejecting."
    hide linkedin_2b
    with dissolve

    hide Laptop
    hide Dimmed
    with dissolve

    $ i += 1
    jump show_skills

label HON_sequences_5:
    show projector_emedia with dissolve

    show present_1a
    with dissolve
    B "One of my courses has assigned a project that involves presenting to the class."
    hide present_1a
    show present_1b
    with dissolve
    show text "{color=#000000}{size=30}{b}Presentation: 1 / 3{/b}{/size}{/color}" at skill_check
    B "Before stage fright could take over, I practiced breaking information into simplified, panic-proof pieces."
    hide present_1b
    with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label HON_sequences_6:
    show projector_emedia with dissolve

    show present_2
    with dissolve
    B "Some quick testing shows most people can't pay attention to me for more than 30 seconds at a time."
    show text "{color=#000000}{size=30}{b}Presentation: 2 / 3{/b}{/size}{/color}" at skill_check
    B "To counter this, I've started shortening my scripts and speaking at a higher volume."
    hide present_2
    with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label HON_sequences_7:
    show projector_emedia with dissolve

    show present_3
    with dissolve
    B "Further tests show that people pay attention to pretty pictures - in response, I've started adding visual aids to my PowerPoint slides."
    show text "{color=#000000}{size=30}{b}Presentation: 3 / 3{/b}{/size}{/color}" at skill_check
    B "With some practice under my belt, I think I can better explain subjects I understand."
    B "Because of course, I'll only ever have to explain things I understand."
    hide present_3
    with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label HON_sequences_8:
    show projector_emedia with dissolve

    show interview_1a
    with dissolve
    B "To the horror of my friends and colleagues, I joked about doing an interview in casual clothes."
    hide interview_1a
    show interview_1b
    with dissolve
    B "Some of them had stronger reactions (and arms) than others."
    hide interview_1b
    show interview_1c
    with dissolve
    show text "{color=#000000}{size=30}{b}Interviewing: 1 / 3{/b}{/size}{/color}" at skill_check
    B "Under threat of further bodily harm, I've found some more formal clothes for the interview."
    hide interview_1c
    with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills

label HON_sequences_9:
    show Dimmed
    show Laptop
    with dissolve

    show interview_2
    with dissolve
    B "I applied for this job months ago, and I’ve forgotten everything about Debugging Enterprises."
    show text "{color=#000000}{size=30}{b}Interviewing: 2 / 3{/b}{/size}{/color}" at skill_check
    B "I spent some time reviewing, as these details {i}{b}just{/b}{/i} might come up during the interview."
    hide interview_2
    with dissolve

    hide Laptop
    hide Dimmed
    with dissolve

    $ i += 1
    jump show_skills

label HON_sequences_10:
    show projector_emedia with dissolve

    show interview_3a
    with dissolve
    B "While I feel mostly prepared, I'm still worried about actually speaking to the interviewer."
    hide interview_3a
    show interview_3b
    with dissolve
    B "To help with my crippling fear of failure, one of my friends offered to do a mock interview."
    hide interview_3b
    show interview_3c
    with dissolve
    show text "{color=#000000}{size=30}{b}Interviewing: 3 / 3{/b}{/size}{/color}" at skill_check
    B "The experience was very unprofessional, but I think the practice made me less afraid of the interviewer."
    hide interview_3c
    with dissolve

    hide projector_emedia with dissolve

    $ i += 1
    jump show_skills
