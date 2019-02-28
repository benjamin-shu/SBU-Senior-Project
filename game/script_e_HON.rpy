label HON_study1:
    if (HON_progress == 1):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        show Study1 A01 with dissolve
        B "Proof by Contradition is an odd form of logical argument."
        show Study1 A02 with dissolve
        B "As an example, suppose you have a friend who has a favorite sports team."
        show Study1 A03 with dissolve
        B "They are {b}very{/b} insistent that their team is the best in the league."
        show Study1 A04 with dissolve
        B "So, out of interest and annoyance, you check that league's rankings."
        show Study1 A05 with dissolve
        B "If your friend's team is the best, then surely they've won the most games, right?"
        show Study1 A06 with dissolve
        B "As it turns out, that team has far from the most wins. Therefore, they cannot be the best in the league."
        show Study1 A07 with dissolve
        B "This helps demonstrate the argument's general format - an initial assumption..."
        show Study1 A08 with dissolve
        B "...followed to its logical conclusion..."
        show Study1 A09 with dissolve
        "...and proven wrong when that conclusion contradicts established fact."

        hide Study1
        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 2):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        show Study1 B01 with dissolve
        B "Binary Search Trees are a special kind of structure used to store date."
        show Study1 B02 with dissolve
        B "Each piece of data (numbers, letters, etc.) is stored in a {b}Node{/b}."
        show Study1 B03 with dissolve
        B "These nodes link to other nodes, which are called its left and right children."
        show Study1 B04 with dissolve
        B "The tree needs a way to compare the two children, so that the greater of the two goes to the left."
        show Study1 B05 with dissolve
        show Study1 B06 with dissolve
        show Study1 B07 with dissolve
        B "The Node at the top of the tree is called the {b}Root{/b}, while the Nodes at the bottom are called {b}Leaves{/b}."
        show Study1 B08 with dissolve
        B "To search for something in this tree, we would start at the Root and check its children."
        show Study1 B09 with dissolve
        show Study1 B10 with dissolve
        B "With the right tree, you can cut half of the elements from your search with each check."

        hide Study1
        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 3):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Study1
        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 4):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label HON_study2:
    if (HON_progress == 1):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Study2
        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 2):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Study2
        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 3):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Study2
        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 4):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Study2
        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end

label HON_study3:
    if (HON_progress == 1):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Study3
        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 2):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Study3
        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 3):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Study3
        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve
    elif (HON_progress == 4):
        show Dimmed with dissolve
        show Laptop with dissolve
        show Browser PDF with dissolve

        $ renpy.pause()

        hide Study3
        hide Browser PDF
        hide Laptop
        hide Dimmed
        with dissolve

    $ phase += 1
    if phase < 3:
        $ renpy.jump("week_phase_%d" % phase)
    else:
        jump week_end
