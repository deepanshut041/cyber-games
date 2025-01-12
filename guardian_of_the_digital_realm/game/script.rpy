define g = Character("Guardian Bot", color="#00BFFF")
define p = Character("Parent", color="#FFA500")
transform middle_center:
    xpos 0.5
    ypos 0.45
    anchor (0.5, 0.5)

screen level_title(title_text, width=200, height=200):
    vbox:
        xalign 0.5
        yalign 0.0

        # Display the question text with a background
        frame:
            background im.Scale("title.png", width, height)  # Scale the background to fit the frame
            xsize width
            ysize height

            text title_text:
                size 40
                color "#FFFFFF"
                outlines [(1, "#000000", 0.5, 0, 0)]  # Add an outline for better visibility
                xalign 0.5
                yalign 0.5


screen quiz_question(title, questions):
    default current_question_index = 0  # Initialize the question index
    default feedback = None  # Initialize feedback to None
    default selected_option = None  # Track the selected option

    $ current_question = questions[current_question_index]

    frame:
        background im.Scale("board.png", 1100, 700)  # Scale the background to fit the frame
        xsize 1100
        ysize 700
        xalign 0.5
        yalign 0.5

        vbox:
            xsize 1100
            ysize 700
            xalign 0.5
            yalign 0.5
            spacing 0
            
            vbox:
                xsize 700
                ysize 150
                xalign 0.5
                text title:
                    size 30
                    color "#FFFFFF"
                    outlines [(1, "#FFFFFF", 0.5, 0, 0)]
                    yalign 0.35
                    xalign 0.5

            vbox:
                xsize 700
                ysize 100
                xalign 0.5
                text current_question["question"]:
                    color "#1C1C1C"
                    outlines [(1, "#1C1C1C", 0.2, 0, 0)]
                    size 24
                    

            $ choices = current_question["choices"]
            vbox:
                xsize 700
                ysize 250
                xalign 0.5
                yalign 0.0
                
                for choice_index, choice in enumerate(choices):
                    button:
                        xsize 600
                        ysize 100
                        xalign 0.5
                        background im.Scale(
                            "success_button.png" if selected_option == choice_index and choice["correct"] else
                            "error_button.png" if selected_option == choice_index and not choice["correct"] else
                            "gold_button.png",
                            600, 100
                        )
                        action [
                            SetScreenVariable("selected_option", choice_index),
                            SetScreenVariable("feedback", choice["feedback"]),
                        ]
                        sensitive feedback is None  # Disable after selection

                        text choice["text"]:
                            size 20
                            xalign 0.5
                            yalign 0.5
                            color "#FFFFFF"
                            outlines [(0.5, "#FFFFFF", 0.2, 0, 0)]

            hbox:
                xsize 700
                ysize 200
                xalign 0.5
                yalign 0.0
                spacing 20
                if selected_option is not None:
                    frame:
                        xsize 600
                        ysize 150
                        xalign 0.5
                        yalign 0.0
                        background im.Scale("text_output.png", 600, 150)

                        text feedback:
                            size 20
                            xsize 530
                            ysize 130
                            xalign 0.5
                            yalign 0.5
                            color "#FFFFFF"
                            outlines [(0.5, "#FFFFFF", 0.2, 0, 0)]
                    
                    button:
                        xsize 100
                        ysize 100
                        xalign 0.5
                        yalign 0.3
                        background im.Scale("next_arrow.png", 100, 100)
                        action [
                            SetScreenVariable("feedback", None),
                            SetScreenVariable("selected_option", None),
                            SetScreenVariable("current_question_index", current_question_index + 1) if current_question_index + 1 != len(questions) else Return(),
                        ]
 

label start:

    # Scene 1: Parent's Concern
    scene bg living_room with fade
    show parent at right

    p "I keep hearing about the dangers of the internet. Cyberbullying, harmful content, unexpected expenses..."
    p "I wish I could keep my child safe online without restricting everything."

    show guardian at left with fade

    g "Hello! I'm your friendly Guardian Bot. I've come to help you create a safe digital environment for your child."
    g "The digital world can be wonderful, but it's also full of hidden dangers. Together, we'll secure your child's devices and teach them safe habits."

    p "That sounds amazing! Where do we start?"

    g "We begin in the Digital Realm. Each step we take will focus on one aspect of online safety. Let's start with Content Filters!"

    scene bg digital_realm with fade
    show guardian happy at middle_center

    g "Welcome to the Digital Realm! This is the Content Filters Forest. Your first mission is to block harmful content paths while keeping safe ones open for exploration."

label level_1:

    scene bg forest with fade
    show guardian happy at middle_center

    g "You find yourself in a dense, magical forest where each path ahead represents a type of online content."
    g "Your task is to guide your child safely through this digital landscape by making smart decisions about what they can access. Let's get started!"

    scene bg quiz with fade
    
    $ level_score = 0
    $ questions = [
        {
            "question": "Click on a path to either block it or allow it, depending on its safety level.",
            "choices": [
                {"text": "Block Explicit Content", "correct": True, "feedback": "Correct! Parental controls and filters are essential for online safety."},
                {"text": "Ignore Social Media Restriction", "correct": False, "feedback": "Not ideal. Unrestricted access can expose children to harm."}
            ]
        },
        {
            "question": "What is the best way to protect your child from harmful online content?",
            "choices": [
                {"text": "Enable parental controls and filters", "correct": True, "feedback": "Correct! Parental controls and filters are essential for online safety."},
                {"text": "Give full access without restrictions", "correct": False, "feedback": "Not ideal. Unrestricted access can expose children to harm."}
            ]
        },
        {
            "question": "How often should you review online safety settings?",
            "choices": [
                {"text": "Regularly, to ensure they are up-to-date", "correct": True, "feedback": "That's correct! Regular reviews help maintain a safe online environment."},
                {"text": "Only once when setting them up", "correct": False, "feedback": "Not quite. Settings should be reviewed regularly for safety."}
            ]
        },
        {
            "question": "Which type of websites should you prioritize for your child?",
            "choices": [
                {"text": "Educational and child-friendly websites", "correct": True, "feedback": "Correct! Educational websites provide valuable resources for learning."},
                {"text": "Social media and entertainment sites", "correct": False, "feedback": "Be cautious. Entertainment is fine, but prioritize safety."}
            ]
        }
    ]

    call screen quiz_question("Content Filters", questions)

    scene bg forest with fade
    show guardian happy at middle_center

    g "Well done! You've successfully configured content filters. Let's move on to the next challenge. Next, we're heading to Screen Time Tower to manage how much time is spent online."


label level_2:

    scene bg clock_tower with fade
    show guardian happy at middle_center
    
    g "Welcome to the Screen Time Tower! Here, you'll learn how to set healthy limits for your child's screen usage."
    g "You see a large clock with sliders representing different types of activities: Gaming, Streaming, and Homework. Your task is to adjust the sliders to allocate time wisely while keeping total screen time under the daily limit."

    scene bg quiz with fade
    
    $ questions = [
        {
            "question": "How many hours should you allocate for gaming each day?",
            "choices": [
                {"text": "2 hours or less", "correct": True, "feedback": "Correct! This ensures gaming is enjoyed in moderation."},
                {"text": "4+ hours", "correct": False, "feedback": "Not ideal. Excessive gaming can interfere with other activities."}
            ]
        },
        {
            "question": "What is a good daily limit for streaming content?",
            "choices": [
                {"text": "1-2 hours", "correct": True, "feedback": "Correct! This allows time for other productive tasks."},
                {"text": "Unlimited time", "correct": False, "feedback": "Not ideal. Unrestricted streaming can lead to overuse."}
            ]
        },
        {
            "question": "How should screen time be prioritized for a school-aged child?",
            "choices": [
                {"text": "Homework first, then leisure activities", "correct": True, "feedback": "Correct! Prioritizing schoolwork helps build discipline."},
                {"text": "Gaming and streaming first", "correct": False, "feedback": "Not ideal. Homework should take precedence."}
            ]
        },
        {
            "question": "How often should you review your child's screen time schedule?",
            "choices": [
                {"text": "Regularly, to ensure a healthy balance", "correct": True, "feedback": "That's correct! Regular reviews help maintain balance."},
                {"text": "Only when there is a problem", "correct": False, "feedback": "Not quite. Proactive reviews are better than reactive ones."}
            ]
        }
    ]

    call screen quiz_question("Screen Time Management", questions)

    scene bg clock_tower with fade
    show guardian happy at middle_center

    g "Fantastic work! You've successfully managed screen time limits. Let's move on to the next area of the Digital Realm."


label level_3:
    scene bg market with fade
    show guardian happy at middle_center
    
    g "Welcome to the App Approvals Arena! Here, you'll decide which apps your child can download."
    g "Each app has a description. Your task is to approve or deny the request based on its suitability."

    scene bg quiz with fade

    $ questions = [
        {
            "question": "An educational app designed to teach math and science concepts. Approve or deny?",
            "choices": [
                {"text": "Approve", "correct": True, "feedback": "Great choice! Educational apps encourage learning and growth."},
                {"text": "Deny", "correct": False, "feedback": "Not ideal. Educational apps are beneficial for your child."}
            ]
        },
        {
            "question": "A social media app that allows sharing of pictures and messages. Approve or deny?",
            "choices": [
                {"text": "Approve", "correct": False, "feedback": "Be cautious. Social media can expose your child to risks at this age."},
                {"text": "Deny", "correct": True, "feedback": "Good decision! Social media might not be suitable for your child yet."}
            ]
        },
        {
            "question": "A gaming app with in-app purchases and chat features. Approve or deny?",
            "choices": [
                {"text": "Approve", "correct": False, "feedback": "Be cautious! Ensure the game is age-appropriate and time-limited."},
                {"text": "Deny", "correct": True, "feedback": "Good call! Apps with chat features can pose privacy risks."}
            ]
        },
        {
            "question": "A productivity app for managing homework and schedules. Approve or deny?",
            "choices": [
                {"text": "Approve", "correct": True, "feedback": "Excellent choice! Productivity apps help build good habits."},
                {"text": "Deny", "correct": False, "feedback": "Not ideal. Productivity apps can be highly beneficial for your child."}
            ]
        }
    ]

    call screen quiz_question("App Approvals", questions)

    scene bg market with fade
    show guardian happy at middle_center

    g "Well done! You've mastered app approvals. Let's move forward to handle purchases."


label level_4:
    scene bg canyon with fade
    show guardian happy at middle_center

    g "Welcome to Purchase Lock Canyon! Here, you'll learn how to disable in-app purchases and protect against unexpected charges."
    g "Your task is to identify purchase traps and toggle settings to block them."

    scene bg quiz with fade

    $ questions = [
        {
            "question": "Should you disable in-app purchases on your child's device?",
            "choices": [
                {"text": "Yes, disable them", "correct": True, "feedback": "Excellent! This prevents accidental or unauthorized purchases."},
                {"text": "No, leave them enabled", "correct": False, "feedback": "Not the best choice. Disabling them helps avoid unexpected charges."}
            ]
        },
        {
            "question": "What should you do about subscription alerts?",
            "choices": [
                {"text": "Review and monitor them", "correct": True, "feedback": "Correct! Monitoring subscriptions helps manage expenses."},
                {"text": "Ignore them", "correct": False, "feedback": "Not ideal. Ignoring them can lead to unchecked expenses."}
            ]
        },
        {
            "question": "Should you allow one-time purchases without a password?",
            "choices": [
                {"text": "No, always require a password", "correct": True, "feedback": "Great decision! This adds a layer of security."},
                {"text": "Yes, allow without a password", "correct": False, "feedback": "Not ideal. Requiring a password prevents unauthorized purchases."}
            ]
        },
        {
            "question": "How should you handle free apps with in-app purchases?",
            "choices": [
                {"text": "Review the app and block in-app purchases", "correct": True, "feedback": "Correct! Reviewing apps ensures they are safe and appropriate."},
                {"text": "Allow them freely", "correct": False, "feedback": "Not ideal. In-app purchases can lead to unexpected charges."}
            ]
        }
    ]

    call screen quiz_question("Purchase Restrictions", questions)

    scene bg canyon with fade
    show guardian happy at middle_center

    g "Fantastic work! You've successfully secured purchase settings. Finally, let's move to Monitoring Mountain for the last challenge."


label level_5:

    # Level 5: Activity Monitoring
    scene bg mountain with fade
    show guardian happy at middle_center

    g "Welcome to Monitoring Mountain! Here, you'll learn how to analyze activity reports and ensure safe usage."
    g "You'll see a dashboard with reports like time spent on apps and flagged activities. Your task is to highlight potential risks and suggest solutions."

    scene bg quiz with fade

    $ level_score = 0
    $ questions = [
        {
            "question": "Your child spent 5 hours gaming yesterday. What action should you take?",
            "choices": [
                {"text": "Flag excessive gaming time", "correct": True, "feedback": "Good observation! Limiting gaming time promotes balance."},
                {"text": "Ignore the activity", "correct": False, "feedback": "Not ideal. Addressing excessive gaming is important for balance."}
            ]
        },
        {
            "question": "An educational app was used for 3 hours yesterday. How should you respond?",
            "choices": [
                {"text": "Highlight safe educational usage", "correct": True, "feedback": "Excellent! Encouraging safe usage is just as important as monitoring risks."},
                {"text": "Reduce time on educational apps", "correct": False, "feedback": "Not necessary. Educational apps are beneficial for learning."}
            ]
        },
        {
            "question": "Your child visited a suspicious website. What action should you take?",
            "choices": [
                {"text": "Investigate and block the website", "correct": True, "feedback": "Correct! Addressing flagged activities promptly ensures safety."},
                {"text": "Ignore the visit", "correct": False, "feedback": "Not the best choice. Suspicious activities should always be addressed."}
            ]
        },
        {
            "question": "Your child's activity report shows no flagged activities. What should you do?",
            "choices": [
                {"text": "Commend their safe usage", "correct": True, "feedback": "Great! Positive reinforcement encourages continued safe behavior."},
                {"text": "Ignore the report", "correct": False, "feedback": "Not ideal. Recognizing good behavior is important for motivation."}
            ]
        }
    ]

    call screen quiz_question("Activity Monitoring", questions)

    scene bg mountain with fade
    show guardian happy at middle_center
    g "Outstanding! You've mastered activity monitoring."

label end:
    scene bg digital_realm with fade

    show parent at right
    show guardian at left

    g "Congratulations! You've successfully completed all challenges in the Digital Realm."

    g "You're now a certified Guardian of the Digital Realm!"

