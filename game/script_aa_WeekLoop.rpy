define week_num = 1

define ARS_principles = 0
define ARS_shapes = 0
define ARS_typography = 0
define ARS_poster = 0
define ARS_video = 0

define CSE_uml = 0
define CSE_srs = 0
define CSE_phase1 = 0
define CSE_phase2 = 0
define CSE_phase3 = 0

define CSE_study1 = 0
define CSE_study2 = 0
define CSE_study3 = 0

define resume = 0
define portfolio = 0

label start:

    label menu_morning:
        if week_num == 3:
            "Principles of Design: [ARS_principles]"

        elif week_num == 5:
            "Shapes: [ARS_shapes]"

        elif week_num == 7:
            "Typography: [ARS_typography]"

        elif week_num == 11:
            "Poster: [ARS_poster]"

        if week_num > 0 and week_num < 15:
            menu:
                "Work on the Principles of Design project." if week_num >= 1 and week_num <= 2:
                    if ARS_principles < 2:
                        $ ARS_principles = ARS_principles + 1

                "Work on the Shapes project." if week_num >= 3 and week_num <= 4:
                    if ARS_shapes < 2:
                        $ ARS_shapes = ARS_shapes + 1

                "Work on the Typography project." if week_num >= 5 and week_num <= 6:
                    if ARS_typography < 2:
                        $ ARS_typography = ARS_typography + 1

                "Work on the Poster project." if week_num >= 7 and week_num <= 10:
                    if ARS_poster < 4:
                        $ ARS_poster = ARS_poster + 1

                "Work on the \"Self-Portrait\" video project." if week_num >= 11 and week_num <= 14:
                    $ ARS_video = ARS_video + 1

                "Work on UML diagram for CSE 308." if week_num >= 1 and week_num <= 2:
                    $ CSE_uml = CSE_uml + 1

                "Work on SRS document for CSE 308." if week_num >= 3 and week_num <= 4:
                    $ CSE_srs = CSE_srs + 1

                "Work on Phase 1 project goals for CSE 308." if week_num >= 5 and week_num <= 7:
                    $ CSE_phase1 = CSE_phase1 + 1

                "Work on Phase 2 project goals for CSE 308." if week_num >= 8 and week_num <= 10:
                    $ CSE_phase2 = CSE_phase2 + 1

                "Work on Phase 3 project goals for CSE 308." if week_num >= 11 and week_num <= 14:
                    $ CSE_phase3 = CSE_phase3 + 1

                "Review CSE course material." if week_num >= 1 and week_num <= 2:
                    $ CSE_study1 = CSE_study1 + 1

                "Prepare for the first round of CSE midterms." if week_num >= 3 and week_num <= 4:
                    $ CSE_study1 = CSE_study1 + 1

                "Review material from the first round of CSE midterms." if week_num >= 6 and week_num <= 14:
                    $ CSE_study1 = CSE_study1 + 1

                "Prepare for the second round of CSE midterms." if week_num >= 6 and week_num <= 9:
                    $ CSE_study2 = CSE_study2 + 1

                "Review material from the second round of CSE midterms." if week_num >= 11 and week_num <= 14:
                    $ CSE_study2 = CSE_study2 + 1

                "Prepare for the CSE final exams." if week_num >= 11 and week_num <= 14:
                    $ CSE_study3 = CSE_study3 + 1

    label menu_afternoon:
        if week_num == 3:
            "UML Diagram: [CSE_uml]"

        elif week_num == 5:
            "SRS Document: [CSE_srs]"
            "Midterm 1: [CSE_study1]"

        elif week_num == 8:
            "CSE 308 Phase 1: [CSE_phase1]"

        elif week_num == 10:
            "Midterm 2: [CSE_study2]"

        elif week_num == 11:
            "CSE 308 Phase 2: [CSE_phase2]"

        elif week_num > 0 and week_num < 15:
            menu:
                "Work on the Principles of Design project." if week_num >= 1 and week_num <= 2:
                    $ ARS_principles = ARS_principles + 1

                "Work on the Shapes project." if week_num >= 3 and week_num <= 4:
                    $ ARS_shapes = ARS_shapes + 1

                "Work on the Typography project." if week_num >= 5 and week_num <= 6:
                    $ ARS_typography = ARS_typography + 1

                "Work on the Poster project." if week_num >= 7 and week_num <= 10:
                    $ ARS_poster = ARS_poster + 1

                "Work on the \"Self-Portrait\" video project." if week_num >= 11 and week_num <= 14:
                    $ ARS_video = ARS_video + 1

                "Work on UML diagram for CSE 308." if week_num >= 1 and week_num <= 2:
                    $ CSE_uml = CSE_uml + 1

                "Work on SRS document for CSE 308." if week_num >= 3 and week_num <= 4:
                    $ CSE_srs = CSE_srs + 1

                "Work on Phase 1 project goals for CSE 308." if week_num >= 5 and week_num <= 7:
                    $ CSE_phase1 = CSE_phase1 + 1

                "Work on Phase 2 project goals for CSE 308." if week_num >= 8 and week_num <= 10:
                    $ CSE_phase2 = CSE_phase2 + 1

                "Work on Phase 3 project goals for CSE 308." if week_num >= 11 and week_num <= 14:
                    $ CSE_phase3 = CSE_phase3 + 1

                "Review CSE course material." if week_num >= 1 and week_num <= 2:
                    $ CSE_study1 = CSE_study1 + 1

                "Prepare for the first round of CSE midterms." if week_num >= 3 and week_num <= 4:
                    $ CSE_study1 = CSE_study1 + 1

                "Review material from the first round of CSE midterms." if week_num >= 6 and week_num <= 14:
                    $ CSE_study1 = CSE_study1 + 1

                "Prepare for the second round of CSE midterms." if week_num >= 6 and week_num <= 9:
                    $ CSE_study2 = CSE_study2 + 1

                "Review material from the second round of CSE midterms." if week_num >= 11 and week_num <= 14:
                    $ CSE_study2 = CSE_study2 + 1

                "Prepare for the CSE final exams." if week_num >= 11 and week_num <= 14:
                    $ CSE_study3 = CSE_study3 + 1

    label menu_night:
        if week_num > 0 and week_num < 15:
            menu:
                "Work on the Principles of Design project." if week_num >= 1 and week_num <= 2:
                    $ ARS_principles = ARS_principles + 1

                "Work on the Shapes project." if week_num >= 3 and week_num <= 4:
                    $ ARS_shapes = ARS_shapes + 1

                "Work on the Typography project." if week_num >= 5 and week_num <= 6:
                    $ ARS_typography = ARS_typography + 1

                "Work on the Poster project." if week_num >= 7 and week_num <= 10:
                    $ ARS_poster = ARS_poster + 1

                "Work on the \"Self-Portrait\" video project." if week_num >= 11 and week_num <= 14:
                    $ ARS_video = ARS_video + 1

                "Work on UML diagram for CSE 308." if week_num >= 1 and week_num <= 2:
                    $ CSE_uml = CSE_uml + 1

                "Work on SRS document for CSE 308." if week_num >= 3 and week_num <= 4:
                    $ CSE_srs = CSE_srs + 1

                "Work on Phase 1 project goals for CSE 308." if week_num >= 5 and week_num <= 7:
                    $ CSE_phase1 = CSE_phase1 + 1

                "Work on Phase 2 project goals for CSE 308." if week_num >= 8 and week_num <= 10:
                    $ CSE_phase2 = CSE_phase2 + 1

                "Work on Phase 3 project goals for CSE 308." if week_num >= 11 and week_num <= 14:
                    $ CSE_phase3 = CSE_phase3 + 1

                "Review CSE course material." if week_num >= 1 and week_num <= 3:
                    $ CSE_study1 = CSE_study1 + 1

                "Prepare for the first round of CSE midterms." if week_num >= 3 and week_num <= 4:
                    $ CSE_study1 = CSE_study1 + 1

                "Review material from the first round of CSE midterms." if week_num >= 6 and week_num <= 14:
                    $ CSE_study1 = CSE_study1 + 1

                "Prepare for the second round of CSE midterms." if week_num >= 6 and week_num <= 9:
                    $ CSE_study2 = CSE_study2 + 1

                "Review material from the second round of CSE midterms." if week_num >= 11 and week_num <= 14:
                    $ CSE_study2 = CSE_study2 + 1

                "Prepare for the CSE final exams." if week_num >= 11 and week_num <= 14:
                    $ CSE_study3 = CSE_study3 + 1

    label week_end:
        $ week_num = week_num + 1

        if week_num < 15:
            jump start

    label End:
        return
