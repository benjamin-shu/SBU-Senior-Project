# ==============================================================================
# Variables and constants used to track the player's progress in various areas.
# ==============================================================================

# String constants to use as codes for various activities.
define code_A = "ARS"
define code_C = "CSE"
define code_S = "HON"

# Current week in the semester.
default week_num = 0

# Dates for introductory cutscenes at start of each week.
define week_events = ( 0, 14 )

# Control variables for selecting activities.
default week_cnt = 0
default week_dict = {}
default week_act = ""
default week_proj = ""

# Progress counters for the different ARS projects.
default ARS_scores = {
"composition": 0,
"shapes": 0,
"typography": 0,
"poster": 0,
"video": 0
}

# Progress counters for the different CSE projects.
default CSE_scores = {
"uml": 0,
"srs": 0,
"phase1": 0,
"phase2": 0,
"phase3": 0
}

# Progress counters for the three CS midterms.
default HON_scores = {
"study1": 0,
"study2": 0,
"study3": 0
}

# Progress counters for non-class-related activities.
default EXT_scores = {
"resume": 0,
"portfolio": 0,
"career": 0,
"apps": 0
}

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

# Tuple for dates of ARS presentations/events.
define ARS_events = ( 0, 2, 4, 6, 10 )

# Dictionary for CSE project deadlines.
define CSE_deadlines = {
2:"uml",
4:"srs",
7:"phase1",
10:"phase2",
14:"phase3"
}

# Tuple for dates of CSE presentations/events.
define CSE_events = (0, 2, 4, 7, 10 )

# Dictionary for midterm dates.
define HON_deadlines = {
4:"study1",
9:"study2",
14:"study3"
}

# Tuple for dates of extra events.
define HON_events = ( 4, 9 )

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
"The Compositional Elements project for {b}ARS{/b} is due in 2 weeks.",
"That {b}ARS{/b} Compositional Elements Project is due next week.",
"The {b}ARS{/b} Shapes project is due in 2 weeks.",
"I need to finish the {b}ARS{/b} Shapes project for next week.",
"I have 2 weeks to finish the Typography project for {b}ARS{/b}.",
"The {b}ARS{/b} Typography project is due next week.",
"There are 4 weeks left to do the {b}ARS{/b} Poster project.",
"I've got 3 weeks left for the {b}ARS{/b} Poster project.",
"There's just 2 weeks left for the {b}Poster{/b} project."
"That {b}ARS{/b} Poster project is due next week."
"The final {b}ARS{/b} Video project is due 4 weeks from now.",
"I've only got 3 weeks to finish the {b}ARS{/b} Video project.",
"Just 2 more weeks for the {b}ARS{/b} Video project.",
"The {b}ARS{/b} Video project is due next week."
)

# List of reminders that ARS projects are finished.
define ARS_completed = (
"I've already finished the Compositional Elements project for {b}ARS{/b}.",
"The {b}ARS{/b} Compositional Elements project is already done.",
"I've finished the {b}ARS{/b} Shapes project - no sense in doing more work on it.",
"The {b}ARS{/b} Shapes project is finished. I should work on something else.",
"I'm done with the Typography project for {b}ARS{/b}. Time to move on.",
"There's no need to work on the {b}ARS{/b} Typography project - it's finished.",
"I've already finished the {b}ARS{/b} Poster project.",
"The {b}ARS{/b} Poster's done - I should move on to the next task.",
"I'm done with the {b}ARS{/b} Poster. I should do something else this week.",
"Why am I working on the {b}ARS{/b} Poster? It's done.",
"The final {b}ARS{/b} Video project is done. What else is there to do?",
"I'm already done with the final Video for {b}ARS{/b}.",
"I've finished the {b}ARS{/b} Video already. I really should do something else.",
"The final {b}ARS{/b} Video project is done. I should be focusing on another project."
)

# Notices that too many points are allocated to ARS.
define ARS_overflow = (
"That {b}ARS{/b} Composition project shouldn't take long. I need space for something else.",
"This schedule needs to change - there's too much time in the {b}ARS{/b} Composition project.",
"The {b}ARS{/b} Shapes project doesn't need this much time.",
"Why is there so much time in {b}ARS{/b}? The Shapes project shouldn't be too bad.",
"I don't need that much time for the {b}ARS{/b} Typography project.",
"The {b}ARS{/b} Typography project won't need this much time.",
"I've already made good progress on the {b}ARS{/b} Poster project. Time for something else.",
"I should redo the schedule - the {b}ARS{/b} Poster project shouldn't take this long.",
"The {b}ARS{/b} Poster project doesn't need this many time slots.",
"I should be focusing on things other than the {b}ARS{/b} Poster project.",
"As much as I like the {b}ARS{/b} Video project, the time should go to other things.",
"I'm putting too much time into the {b}ARS{/b} Video project.",
"The {b}ARS{/b} Video project won't need that much time to finish.",
"I shouldn't spend more time on the {b}ARS{/b} Video project than necessary."
)

# List of reminders for each CSE project.
define CSE_reminders = (
"The {b}CSE 308's{/b} professor wants us to hand in UML diagrams in 2 weeks.",
"Those UML diagrams for {b}CSE 308{/b} are due next week.",
"The {b}CSE 308{/b} SRS document is due 2 weeks from now.",
"The {b}CSE 308{/b} SRS is due next week.",
"The Phase 1 goals for {b}CSE 308{/b} are due in 3 weeks.",
"I have 2 weeks left for the {b}CSE 308{/b} Phase 1 goals.",
"The {b}CSE 308{/b} Phase 1 goals are due next week.",
"I've got 3 weeks to finish those {b}CSE 308{/b} Phase 2 goals.",
"There are 2 weeks left to finish {b}CSE 308{/b}'s Phase 2.",
"Just 1 more week to finish Phase 2 of the {b}CSE 308{/b} project.",
"I've got 4 weeks for the last phase of the {b}CSE 308{/b} project.",
"There's 3 more weeks left for the {b}CSE 308{/b} project.",
"Just 2 more weeks...just two more weeks of {b}CSE 308{/b}.",
"It's almost over. The {b}CSE 308{/b} project is due next week."
)

# List of reminders that each CSE project is completed.
define CSE_completed = (
"I'm already done with the UML diagrams for {b}CSE 308{/b}. I should do something else.",
"Those UML diagrams for {b}CSE 308{/b} are finished. What else can I do?",
"I've finished the SRS for {b}CSE 308{/b}. I need to get some other work done.",
"The {b}CSE 308{/b} SRS document is done. The time should go elsewhere.",
"Phase 1 for {b}CSE 308{/b} is done. There's other projects that need attention.",
"I'm done with Phase 1 for {b}CSE 308{/b}. Time to work on something else. ",
"{b}CSE 308{/b}'s Phase 1 is complete. I should spend time on other things.",
"Phase 2 of the {b}CSE 308{/b} project is done. I should work on something else.",
"The goals for Phase 2 of the {b}CSE 308{/b} project are already finished.",
"I'm done with Phase 2 of {b}CSE 308{/b}. I ought to be working on something else.",
"Phase 3 of {b}CSE 308{/b} is done. Is there something else I can do with that time?",
"The Phase 3 goals for {b}CSE 308{/b} are done. What else can I do with my time?",
"I've already finished Phase 3 of the {b}CSE 308{/b} project.",
"The {b}CSE 308{/b} project is already finished, Phase 3 included."
)

# Notices that too many points are allocated to CSE.
define CSE_overflow = (
"The UML diagrams for {b}CSE 308{/b} don't need that much time to finish.",
"I shouldn't put that much time into {b}CSE 308{/b}'s UML diagram.",
"The SRS for {b}CSE 308{/b} won't take that long - the time should go to something else.",
"There's not much left of the SRS to write for {b}CSE 308{/b}. I should use that time for something else.",
"I can't spare this much time for Phase 1 for {b}CSE 308{/b}. Can I work on something else?",
"The Phase 1 goals for {b}CSE 308{/b} don't need this much time. I can use that time for other things.",
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
