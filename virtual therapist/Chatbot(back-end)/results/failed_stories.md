## happy path 1 (C:\Users\harsh\AppData\Local\Temp\tmpeeeungh1\046403ba64aa4b9fba4adad21234607c_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: day_good: amazing -->
    - utter_happy   <!-- predicted: utter_day_good -->


## happy path 2 (C:\Users\harsh\AppData\Local\Temp\tmpeeeungh1\046403ba64aa4b9fba4adad21234607c_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: day_good: amazing -->
    - utter_happy   <!-- predicted: utter_day_good -->
* goodbye: bye-bye!   <!-- predicted: affirm: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_test2 -->


## sad path 1 (C:\Users\harsh\AppData\Local\Temp\tmpeeeungh1\046403ba64aa4b9fba4adad21234607c_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: day_bad: not good -->
    - utter_cheer_up   <!-- predicted: utter_day_bad -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_test2 -->


## sad path 2 (C:\Users\harsh\AppData\Local\Temp\tmpeeeungh1\046403ba64aa4b9fba4adad21234607c_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: day_bad: not good -->
    - utter_cheer_up   <!-- predicted: utter_day_bad -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: free_time: not really -->
    - utter_goodbye   <!-- predicted: action_default_fallback -->


## sad path 3 (C:\Users\harsh\AppData\Local\Temp\tmpeeeungh1\046403ba64aa4b9fba4adad21234607c_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: day_bad: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_day_bad -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no   <!-- predicted: decline: no -->
    - utter_goodbye   <!-- predicted: utter_nodepression -->


## say goodbye (C:\Users\harsh\AppData\Local\Temp\tmpeeeungh1\046403ba64aa4b9fba4adad21234607c_conversation_tests.md)
* goodbye: bye-bye!   <!-- predicted: affirm: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_test2 -->


## bot challenge (C:\Users\harsh\AppData\Local\Temp\tmpeeeungh1\046403ba64aa4b9fba4adad21234607c_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: day_bad: are you a bot? -->
    - utter_iamabot   <!-- predicted: utter_day_bad -->


