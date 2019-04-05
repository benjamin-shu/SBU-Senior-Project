label HON_sequences:
    # Retrieve index for HON data using codes[].
    default HON_index = codes.index("HON")
    # Retrive player's current progress in this skill tree.
    default HON_progress = progress[HON_index]

    # Set scene in West F 301C.
    scene West F 301C with fade

    # $ renpy.jump("HON_sequences_%d" % (HON_progress))

label HON_sequences_1:
    show projector_emedia with dissolve

    show resume_1a
    with dissolve
    B "You had a look at your resume, and it...left a lot to be desired."
    hide resume_1a
    show resume_1b
    with dissolve
    B "Thanks to some advice from the Career Center, you now have a more presentable format."
    hide resume_1b
    with dissolve

    hide projector_emedia with dissolve

    # $ i += 1
    # jump show_skills

label HON_sequences_2:
    show projector_emedia with dissolve

    show resume_1b
    with dissolve
    B "A counselor from the Career Center was nice enough to give you more tips on resume formatting."
    hide resume_1b
    show resume_2a
    with dissolve
    B "Current contact information and most recent work experience goes up top..."
    hide resume_2a
    show resume_2b
    with dissolve
    B "...and skills and extracurriculars goes at the bottom (if they actually read the whole thing)."
    B "Now, you have a resume that you're not ashamed of."
    hide resume_2b
    with dissolve

    hide projector_emedia with dissolve

    # $ i += 1
    # jump show_skills

label HON_sequences_3:
    show Dimmed
    show Laptop
    with dissolve

    show linkedin_1
    with dissolve
    B "A few of your friends explained the importance of a LinkedIn profile, and told you to make sure yours is complete."
    hide linkedin_1
    show linkedin_1a
    with dissolve
    B "At their insistence, you’ve added a profile picture, a cover photo, and a short bio."
    hide linkedin_1a
    with dissolve

    hide Laptop
    hide Dimmed
    with dissolve

    # $ i += 1
    # jump show_skills

label HON_sequences_4:
    show Dimmed
    show Laptop
    with dissolve

    show linkedin_2a
    with dissolve
    B "In order to shut your friends up, you’ve uploaded your resume to your LinkedIn profile."
    hide linkedin_2a
    show linkedin_2b
    with dissolve
    B "Doing so has built the rest of your profile for you and given employers a better sense of who they're rejecting."
    hide linkedin_2b
    with dissolve

    hide Laptop
    hide Dimmed
    with dissolve

    # $ i += 1
    # jump show_skills

label HON_sequences_5:
    show projector_emedia with dissolve

    show present_1a
    with dissolve
    B "One of your courses has assigned a project that involves presenting to the class."
    hide present_1a
    show present_1b
    with dissolve
    B "Expecting stage fright to destroy your higher-order thought, you start breaking information into simplified, panic-proof pieces."
    hide present_1b
    with dissolve

    hide projector_emedia with dissolve

    # $ i += 1
    # jump show_skills

label HON_sequences_6:
    show projector_emedia with dissolve

    show present_2
    with dissolve
    B "Some quick testing shows most people incapable of paying attention to you for more than 30 seconds at a time."
    B "To counter this, you start shortening your scripts and speaking at a higher volume."
    hide present_2
    with dissolve

    hide projector_emedia with dissolve

    # $ i += 1
    # jump show_skills

label HON_sequences_7:
    show projector_emedia with dissolve

    show present_3
    with dissolve
    B "Further tests show that people pay more attention to pretty pictures - in response, you start adding visual aids to your PowerPoint slides."
    B "With some practice under your belt, you now feel more comfortable giving presentations on subjects you understand."
    hide present_3
    with dissolve

    hide projector_emedia with dissolve

    # $ i += 1
    # jump show_skills

label HON_sequences_8:
    show projector_emedia with dissolve

    show interview_1a
    with dissolve
    B "To the horror of your friends and colleagues, you joked about doing an interview in your casual clothes."
    hide interview_1a
    show interview_1b
    with dissolve
    B "Some of them had stronger reactions (and arms) than others."
    hide interview_1b
    show interview_1c
    with dissolve
    B "Under threat of further bodily harm, you find some more formal clothes for your interview."
    hide interview_1c
    with dissolve

    hide projector_emedia with dissolve

    # $ i += 1
    # jump show_skills

label HON_sequences_9:
    show Dimmed
    show Laptop
    with dissolve

    show interview_2
    with dissolve
    B "Having applied for this job months ago, you’ve long since forgotten every detail about the company (and why you applied in the first place)."
    B "You spend some time refreshing your memory, as these details might come up during the interview."
    hide interview_2
    with dissolve

    hide Laptop
    hide Dimmed
    with dissolve

    # $ i += 1
    # jump show_skills

label HON_sequences_10:
    show projector_emedia with dissolve

    show interview_3a
    with dissolve
    B "While you feel mostly prepared, you’re still worried about actually speaking to the interviewer."
    hide interview_3a
    show interview_3b
    with dissolve
    B "To help with your crippling fear of failure, one of your friends offers to do mock interview questions."
    hide interview_3b
    show interview_3c
    with dissolve
    B "While the experience takes an unprofessional turn, the practice helps you feel more comfortable in an interview setting."
    hide interview_3c
    with dissolve

    hide projector_emedia with dissolve

    # $ i += 1
    # jump show_skills
