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

    voice "voice/start_f0ae3df4.mp3"
    p "The internet feels like such a risky place these days—cyberbullying, harmful content, surprise charges... it's overwhelming."
    
    voice "voice/start_52a3bc87.mp3"
    p "I just want to protect my child online without locking them out of everything fun."

    show guardian at left with fade

    voice "voice/start_04c15fe0.mp3"
    g "Hi there! I'm Guardian Bot, your trusty guide to creating a safe and balanced digital world for your child."
    
    voice "voice/start_e4983b11.mp3"
    g "The internet can be an amazing tool, but you're right—it has its challenges. Together, we'll tackle those dangers while keeping the fun intact."

    voice "voice/start_fc1a4465.mp3"
    p "That sounds wonderful! I could really use the help. Where do we start?"

    voice "voice/start_5020a4ff.mp3"
    g "We start in the Digital Realm, where every step we take will focus on a key area of online safety. First up, Content Filters! These are your best allies in keeping harmful material away from your child."

label level_1:

    scene bg forest with fade
    show guardian happy at middle_center

    voice "voice/level_1_560c4199.mp3"
    g "Welcome to the Digital Realm! This is the Content Filters Forest, where your mission is to block harmful content paths while keeping safe ones open for your child to explore."
    
    voice "voice/level_1_7d0f6fdb.mp3"
    g "Guide your child safely through this digital landscape by making smart decisions about what they can access. Let's get started!"

    scene bg quiz with fade
    
    $ level_score = 0
    $ questions = [
        {
            "question": "What should you do if a website has content that might harm your child?",
            "choices": [
                {"text": "Ignore the content and let them browse freely", "correct": False, "feedback": "Not ideal. Harmful content can impact your child's safety."},
                {"text": "Use parental controls to block harmful content", "correct": True, "feedback": "Correct! Parental controls help ensure a safe browsing experience."}
            ]
        },
        {
            "question": "How can you ensure your child stays safe while using the internet?",
            "choices": [
                {"text": "Set up parental controls and filters", "correct": True, "feedback": "Correct! These tools are essential for online safety."},
                {"text": "Allow them to access any site without supervision", "correct": False, "feedback": "Not recommended. Supervision is key to protecting children online."}
            ]
        },
        {
            "question": "How often should you check the online safety settings on your child's devices?",
            "choices": [
                {"text": "Only once, when setting them up", "correct": False, "feedback": "Not quite. Settings should be reviewed regularly for safety."},
                {"text": "Regularly, to make sure they stay up-to-date", "correct": True, "feedback": "That's right! Regular reviews keep your child protected as threats evolve."}
            ]
        },
        {
            "question": "What type of websites are best for your child to use?",
            "choices": [
                {"text": "Educational and child-friendly websites", "correct": True, "feedback": "Correct! These websites provide valuable learning resources and are safer."},
                {"text": "Social media and gaming websites", "correct": False, "feedback": "Be cautious. While gaming can be fun, prioritize safety and learning."}
            ]
        },
        {
            "question": "What should you do if your child asks to visit a new website?",
            "choices": [
                {"text": "Check the website for safety and suitability", "correct": True, "feedback": "Correct! Always review new sites to ensure they are safe for your child."},
                {"text": "Allow access without checking", "correct": False, "feedback": "Not ideal. Reviewing the website first helps avoid potential risks."}
            ]
        }
    ]

    call screen quiz_question("Content Filters", questions)

    scene bg forest with fade
    show guardian happy at middle_center

    voice "voice/level_1_d53f7c88.mp3"
    g "Well done! You've successfully configured content filters. Let's move on to the next challenge. Next, we're heading to Screen Time Tower to manage how much time is spent online."


label level_2:

    scene bg clock_tower with fade
    show guardian happy at middle_center
    
    voice "voice/level_2_9c42c24b.mp3"
    g "Welcome to the Screen Time Tower! This is where you'll master the art of setting healthy screen time limits for your child."
    
    voice "voice/level_2_96984814.mp3"
    g "In front of you is a towering clock with sliders for Gaming, Streaming, and Homework. Your task is to adjust the sliders to wisely allocate time while keeping the total screen time within a healthy daily limit."

    scene bg quiz with fade
    
    $ questions = [
        {
            "question": "What is a healthy daily limit for gaming time?",
            "choices": [
                {"text": "4+ hours", "correct": False, "feedback": "Not ideal. Excessive gaming can interfere with other important activities."},
                {"text": "2 hours or less", "correct": True, "feedback": "Correct! Limiting gaming to 2 hours or less helps maintain balance."}
            ]
        },
        {
            "question": "How much time should be spent streaming content daily?",
            "choices": [
                {"text": "Unlimited time", "correct": False, "feedback": "Not ideal. Unlimited streaming can lead to unhealthy habits."},
                {"text": "1-2 hours", "correct": True, "feedback": "Correct! This allows time for other productive and engaging activities."}
            ]
        },
        {
            "question": "How should a school-aged child prioritize screen time?",
            "choices": [
                {"text": "Gaming and streaming first", "correct": False, "feedback": "Not recommended. Homework and responsibilities should come first."},
                {"text": "Homework first, then leisure activities", "correct": True, "feedback": "Correct! This approach helps build discipline and balance."}
            ]
        },
        {
            "question": "How often should a child's screen time schedule be reviewed?",
            "choices": [
                {"text": "Only when there is a problem", "correct": False, "feedback": "Not ideal. Regular reviews help maintain a healthy balance."},
                {"text": "Regularly, to ensure a healthy balance", "correct": True, "feedback": "Correct! Proactive reviews keep screen time in check."}
            ]
        }
    ]

    call screen quiz_question("Screen Time Management", questions)

    scene bg clock_tower with fade
    show guardian happy at middle_center

    voice "voice/level_2_6c94d999.mp3"
    g "Fantastic work! You've successfully managed screen time limits. Let's move on to the next area of the Digital Realm."


label level_3:
    scene bg market with fade
    show guardian happy at middle_center
    
    voice "voice/level_3_03a90dcd.mp3"
    g "Welcome to the App Approvals Arena! Here, you'll decide which apps your child can download."
    
    voice "voice/level_3_96c685ea.mp3"
    g "Each app has a description. Your task is to approve or deny the request based on its suitability."

    scene bg quiz with fade

    $ questions = [
        {
            "question": "An educational app designed to teach math, science, and language skills. Approve or deny?",
            "choices": [
                {"text": "Approve", "correct": True, "feedback": "Great choice! Educational apps encourage learning and development in various subjects."},
                {"text": "Deny", "correct": False, "feedback": "Not ideal. Educational apps provide valuable learning opportunities for your child."}
            ]
        },
        {
            "question": "A social media app that allows sharing of pictures, videos, and private messages. Approve or deny?",
            "choices": [
                {"text": "Approve", "correct": False, "feedback": "Be cautious. Social media can expose your child to privacy and security risks."},
                {"text": "Deny", "correct": True, "feedback": "Good decision! Social media might not be suitable for children without proper guidance."}
            ]
        },
        {
            "question": "A gaming app with frequent ads, in-app purchases, and chat features. Approve or deny?",
            "choices": [
                {"text": "Approve", "correct": False, "feedback": "Not recommended. Apps with ads, in-app purchases, and chat features can pose financial and privacy risks."},
                {"text": "Deny", "correct": True, "feedback": "Smart choice! Games with these features should be monitored or avoided."}
            ]
        },
        {
            "question": "A productivity app that helps with managing school projects, deadlines, and schedules. Approve or deny?",
            "choices": [
                {"text": "Approve", "correct": True, "feedback": "Excellent choice! Productivity apps foster time management and organizational skills."},
                {"text": "Deny", "correct": False, "feedback": "Not ideal. Productivity apps can be highly beneficial for improving your child's habits."}
            ]
        }
    ]

    call screen quiz_question("App Approvals", questions)

    scene bg market with fade
    show guardian happy at middle_center

    voice "voice/level_3_4c9cf543.mp3"
    g "Well done! You've mastered app approvals. Let's move forward to handle purchases."


label level_4:
    scene bg canyon with fade
    show guardian happy at middle_center

    voice "voice/level_4_4394883a.mp3"
    g "Welcome to Purchase Lock Canyon! Here, you'll learn how to disable in-app purchases and protect against unexpected charges."
    
    voice "voice/level_4_93e86691.mp3"
    g "Your task is to identify purchase traps and toggle settings to block them."

    scene bg quiz with fade

    $ questions = [
        {
            "question": "Should in-app purchases be disabled on your child's device?",
            "choices": [
                {"text": "Yes, disable them", "correct": True, "feedback": "Excellent! Disabling in-app purchases prevents accidental or unauthorized spending."},
                {"text": "No, leave them enabled", "correct": False, "feedback": "Not the best choice. Leaving them enabled can lead to unexpected charges."}
            ]
        },
        {
            "question": "How should you handle subscription alerts on apps or services?",
            "choices": [
                {"text": "Review and monitor them regularly", "correct": True, "feedback": "Correct! Monitoring subscriptions helps you avoid unnecessary expenses."},
                {"text": "Ignore them to save time", "correct": False, "feedback": "Not ideal. Ignoring alerts can lead to surprise charges."}
            ]
        },
        {
            "question": "Should you require a password for every purchase on your child's device?",
            "choices": [
                {"text": "Yes, always require a password", "correct": True, "feedback": "Great decision! Password protection adds an extra layer of security."},
                {"text": "No, allow purchases without a password", "correct": False, "feedback": "Not recommended. Requiring a password prevents unauthorized spending."}
            ]
        },
        {
            "question": "How should you manage free apps that include in-app purchases?",
            "choices": [
                {"text": "Review the app and disable in-app purchases", "correct": True, "feedback": "Correct! Reviewing apps ensures they are safe and won't lead to unexpected costs."},
                {"text": "Allow them freely without restrictions", "correct": False, "feedback": "Not ideal. Apps with in-app purchases can lead to financial risks if unmanaged."}
            ]
        }
    ]

    call screen quiz_question("Purchase Restrictions", questions)

    scene bg canyon with fade
    show guardian happy at middle_center

    voice "voice/level_4_e19617b7.mp3"
    g "Fantastic work! You've successfully secured purchase settings. Finally, let's move to Monitoring Mountain for the last challenge."


label level_5:

    # Level 5: Activity Monitoring
    scene bg mountain with fade
    show guardian happy at middle_center

    voice "voice/level_5_f2ba2862.mp3"
    g "Welcome to Monitoring Mountain! Here, you'll learn how to analyze activity reports and ensure safe usage."
    
    voice "voice/level_5_1f945519.mp3"
    g "You'll see a dashboard with reports like time spent on apps and flagged activities. Your task is to highlight potential risks and suggest solutions."

    scene bg quiz with fade

    $ level_score = 0
    $ questions = [
        {
            "question": "Your child spent several hours playing an online game yesterday. What should you do?",
            "choices": [
                {"text": "Discuss and set time limits for gaming", "correct": True, "feedback": "Good approach! Setting limits helps maintain a healthy balance."},
                {"text": "Ignore it if it happens occasionally", "correct": False, "feedback": "Not ideal. It's important to address excessive gaming to form good habits."}
            ]
        },
        {
            "question": "Your child spent 2 hours on an educational website. How should you handle it?",
            "choices": [
                {"text": "Encourage and praise their learning effort", "correct": True, "feedback": "Great choice! Positive reinforcement encourages productive screen time."},
                {"text": "Limit time on educational activities", "correct": False, "feedback": "Not necessary. Educational activities support learning and growth."}
            ]
        },
        {
            "question": "Your child's activity log shows a visit to an unsafe or suspicious site. What should you do?",
            "choices": [
                {"text": "Investigate and block the website immediately", "correct": True, "feedback": "Correct! Ensuring safety requires prompt action and monitoring."},
                {"text": "Ignore it as it may not happen again", "correct": False, "feedback": "Not recommended. Suspicious activities should be addressed to prevent risks."}
            ]
        },
        {
            "question": "Your child's activity report shows responsible online behavior all week. What action should you take?",
            "choices": [
                {"text": "Praise and encourage their safe habits", "correct": True, "feedback": "Excellent! Positive reinforcement builds confidence and responsible behavior."},
                {"text": "Do nothing since everything is fine", "correct": False, "feedback": "Not ideal. Recognizing their effort encourages continued good behavior."}
            ]
        }
    ]

    call screen quiz_question("Activity Monitoring", questions)

    scene bg mountain with fade
    show guardian happy at middle_center

    voice "voice/level_5_668cfb8e.mp3"
    g "Outstanding! You've mastered activity monitoring."

label end:
    scene bg digital_realm with fade

    show parent at right
    show guardian at left

    voice "voice/end_2ef071f0.mp3"
    g "Congratulations! You've successfully completed all challenges in the Digital Realm."

    voice "voice/end_70b6fb72.mp3"
    g "You're now a certified Guardian of the Digital Realm!"

