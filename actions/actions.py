# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from fuzzywuzzy import process

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

APPS_db = {
    "YouTube",
    "tfg_chatbot_movil",
    "Google",
    "prueba_boton",
    "Messages",
    "Google Play Store",
    "Contacts",
    "Camera",
    "Clock",
    "Gmail",
    "Duo",
    "Drive",
    "Maps",
    "Chrome",
    "Phone",
    "Google Play Movies & TV",
    "webView shell",
    "Photos",
    "Calendar",
    "Files",
    "android_chatbot",
    "Settings",
    "YouTube Music",
    "System Tracing",
    "usage_stats_example"
}

class searchApp(Action):

     def name(self) -> Text:
         return "action_search_app"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         app = next(tracker.get_latest_entity_values("name_app"), None)
         action = next(tracker.get_latest_entity_values("action"), None)
         print(app)
         if app is None:
            fuzzy = process.extractOne(app, APPS_db)
            print(fuzzy)
            if fuzzy[1] >= 80:
                txt = "{}d notifications for app: {}".format(action,fuzzy[0])
                flutt = action+"_notification_"+fuzzy[0]
            else:
                txt = "{} not found in your device".format(fuzzy[0])
                flutt = "undefined"
            date_response = {
                "text": txt,
                "flutteraction": flutt
            }
            dispatcher.utter_message(json_message = date_response)
            return []
         else:
            txt = "Could not identify the application, please indicate a proper APP name"
            flutt = "undefined"
            date_response = {
                "text": txt,
                "flutteraction": flutt
            }
            dispatcher.utter_message(json_message = date_response)
