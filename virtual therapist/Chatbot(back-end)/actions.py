# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker

from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        msg = "Hello {}. How was your day?".format(name)
        dispatcher.utter_message(text=msg)

        return []

class ActionSleepTracker(Action):

    def name(self) -> Text:
        return "action_sleep_tracker"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time = int(tracker.get_slot("ti"))
        if time < 3:
            msg = "That is too less to what a person needs. You should sleep at least for 6 to 8 hours."
        elif time >= 3 and time < 6:
            msg = "Not bad! but this is not enough. You should sleep at least for 6 to 8 hours."
        elif time >= 6 and time < 8:
            msg = "You are doing good. keep it up."
        elif time >= 8 and time < 12:
            msg = "That's great. keep it up."
        else:
            msg = "Sleeping too much is also not preferred. adequate sleep time is from 7-9 hours.\n"
        msg1 = "Balanced sleep prevents anxiety, it makes worries go away, and it keeps us focused and in good shape. \n" \
               "Also, other main benefits of getting proper sleep are a strong immune system, enhanced memory,\n " \
               "improved learning abilities, plus a balanced level of hormones in our body and brain.\n"
        dispatcher.utter_message(text=msg)
        dispatcher.utter_message(text=msg1)


        return []

