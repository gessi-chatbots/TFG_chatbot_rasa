from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class checkPackageStatus(Action):

    def name(self) -> Text:
        return "action_check_package_status"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        days = random.random(0, 31)
        if (days < 10):
            dispatcher.utter_message(text="Your order hasn't left yet.")
        elif (days < 30):
            dispatcher.utter_message(text="Your order has just arrived to its destination.")
        else:
            dispatcher.utter_message(text="Your order has just left.")
        
        return []
    