# ==========================================================================
# Integer counters used to track the player's progress in various areas.
# ==========================================================================

# Current week in the semester.
default week_num = 0

# Progress counters for the different ARS projects.
default ARS_composition = 0
default ARS_shapes = 0
default ARS_typography = 0
default ARS_poster = 0
default ARS_video = 0

# Progress counters for the different CSE projects.
default CSE_uml = 0
default CSE_srs = 0
default CSE_phase1 = 0
default CSE_phase2 = 0
default CSE_phase3 = 0

# Progress counters for the three CS midterms.
default HON_study1 = 0
default HON_study2 = 0
default HON_study3 = 0

# Progress counters for non-class-related activities.
default resume = 0
default portfolio = 0

# Boolean flag for whether or not the player's schedule is valid.
default valid_schedule = True

# Progress counters for current available activities.
default ARS_progress = 0
default CSE_progress = 0
default HON_progress = 0

# Maximum point caps for each week of the game.
define ARS_caps = ( 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4 )
default ARS_max = 2
define CSE_caps = ( 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4 )
default CSE_max = 2
default HON_max = 4

# Dictionary for ARS project deadlines.
define ARS_deadlines = {
2:"composition",
4:"shapes",
6:"typography",
10:"poster",
14:"video"
}

# Dictionary for CSE project deadlines.
define CSE_deadlines = {
2:"uml",
4:"srs",
7:"phase1",
10:"phase2",
14:"phase3"
}

# Dictionary for midterm dates.
define HON_deadlines = {
4:"study1",
9:"study2",
14:"study3"
}

# ==========================================================================
# Control Variables For schedule() Screen.
# ==========================================================================

# Int counter to track current phase of the week.
default phase = 0

# Image array for the clock's left slot.
default L_src = [ "Schedule/L ARS.png", "Schedule/L CSE.png", "Schedule/L Study.png" ]
# File path for currently displayed image left slots.
default L_img = "Schedule/L Placeholder.png"
# Index of current image in L_src[].
default L_ind = 0

# Image array for the clock's center slot.
default M_src = [ "Schedule/M ARS.png", "Schedule/M CSE.png", "Schedule/M Study.png" ]
# File path for currently-displayed image in center slot.
default M_img = "Schedule/M Placeholder.png"
# Index of current image in M_src[].
default M_ind = 0

# Image array for the clock's right slot.
default R_src = [ "Schedule/R ARS.png", "Schedule/R CSE.png", "Schedule/R Study.png" ]
# File path for currently-displayed image in right slot.
default R_img = "Schedule/R Placeholder.png"
# Index of current image in R_src[].
default R_ind = 0

# Array of integers to be checked when the player confirms their schedule.
# Should be checked against current progress counters to avoid going over the limit for a project/activity.
define act_cnt = [ 0, 0, 0, 0 ]

# A composite image for the clock itself.
# Note that it uses the L_img, M_img, and R_img file paths.
image schedule_img = Composite(
    (1280, 720),
    (0, 0), "Schedule/Clock Back.png",
    (0, 0), "Schedule/Sleep Slot.png",
    (0, 0), "[L_img]",
    (0, 0), "[M_img]",
    (0, 0), "[R_img]",
    (0, 0), "Schedule/Clock Face.png")

# Screen definition for the interactive buttons that the player uses.
# Each section on the clock has a button which toggles through the different activities.
# There is also a "Continue" button included to confirm a schedule.
# For smooth transitions, make sure to use "show schedule_img" first!
screen schedule():
    modal True

    imagebutton:
        focus_mask True
        idle "Schedule/L Idle.png"
        hover "Schedule/L Hover.png"
        action [SetVariable("L_ind", ((L_ind + 1) % len(L_src))), SetVariable("L_img", L_src[L_ind])]

    imagebutton:
        focus_mask True
        idle "Schedule/M Idle.png"
        hover "Schedule/M Hover.png"
        action [SetVariable("M_ind", ((M_ind + 1) % len(M_src))), SetVariable("M_img", M_src[M_ind])]

    imagebutton:
        focus_mask True
        idle "Schedule/R Idle.png"
        hover "Schedule/R Hover.png"
        action [SetVariable("R_ind", ((R_ind + 1) % len(R_src))), SetVariable("R_img", R_src[R_ind])]

    imagebutton:
        focus_mask True
        pos (551, 626)
        idle "Schedule/Continue Idle.png"
        hover "Schedule/Continue Hover.png"
        action [SetVariable("valid_schedule", True), Jump("schedule_check")]

# ==============================================================================
# Schedule Making Dialogue
# ==============================================================================
# String variable for printing reminders and completion notices.
default reminder = ""

# List of reminders for each ARS project.
define ARS_reminders = (
"There's a Compositional Elements project due in 2 weeks.",
"The Compositional Elements Project is due next week.",
"The Shapes project is due in 2 weeks.",
"I need to finish the Shapes project for next week.",
"I have 2 weeks to finish the Typography project.",
"The Typography project is due next week.",
"There are 4 weeks left to do the Poster project.",
"I've got 3 weeks left for the Poster project.",
"There's just 2 weeks left for the Poster project."
"That Poster project is due next week."
"The final Video project is due 4 weeks from now.",
"I've only got 3 weeks to finish the Video project.",
"Just 2 more weeks for the Video project.",
"The Video project is due next week."
)

# List of reminders that ARS projects are finished.
define ARS_completed = (
"I've already finished the Compositional Elements project.",
"The Compositional Elements project is already done.",
"I've finished the Shapes project - no sense in doing more work on it.",
"The Shapes project is finished. I should work on something else.",
"I'm done with the Typography project. Time to move on.",
"There's no need to work on the Typography project - it's finished.",
"I've already finished the Poster project.",
"The Poster's done - on to the next task.",
"I'm done with the Poster. I should do something else this week.",
"Why am I working on the Poster? It's done.",
"The final Video project is done. What else is there to do?",
"I'm already done with the final Video.",
"I've finished the Video already. I really should do something else.",
"The final Video project is done. I should be focusing on another project."
)

# Notices that too many points are allocated to ARS.
define ARS_overflow = (
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
""
)

# List of reminders for each CSE project.
define CSE_reminders = (
"The CSE 308 professor wants us to hand in UML diagrams in 2 weeks.",
"Those UML diagrams for CSE 308 are due next week.",
"The SRS document is due 2 weeks from now.",
"The SRS is due next week.",
"The Phase 1 goals for CSE 308 are due in 3 weeks.",
"I have 2 weeks left for the Phase 1 goals.",
"The Phase 1 goals are due next week.",
"I've got 3 weeks to finish those Phase 2 goals.",
"There are 2 weeks left to finish CSE 308's Phase 2.",
"Just 1 more week to finish Phase 2 of the CSE project.",
"I've got 4 weeks for the last phase of the CSE 308 project.",
"There's 3 more weeks left for the CSE 308 project.",
"Just 2 more weeks...just two more weeks of CSE 308.",
"It's almost over. The CSE 308 project is due next week."
)

# List of reminders that each CSE project is completed.
define CSE_completed = (
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
""
)

# Notices that too many points are allocated to CSE.
define CSE_overflow = (
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
""
)

# List of reminders for midterms/exams.
define HON_reminders = (
"The first round of midterms comes up in 4 weeks.",
"I have 3 weeks until midterms.",
"T-minus 2 weeks until the first midterms arrive.",
"Only one week before the attack of the midterms.",
"The first midterms are this week. We can all panic now.",
"The second wave of midterms comes in 4 weeks.",
"I have 3 weeks before the second round of midterms.",
"Just two weeks before the next midterms come to finish me off.",
"The second round of midterms is next week. I'll let that sink in for a bit.",
"Round 2 of midterms is here, with pain and misery for all.",
"Final exams are 4 weeks from now.",
"There's 3 weeks left until the final exams come for us all.",
"And only 2 more weeks before final exams. Just enough time to write a will.",
"Final exams are next week. Time to make peace with my gods."
)

# List of reminders that exam review is finished.
define HON_completed = (
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
)
