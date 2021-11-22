# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

APPS_db = {
    "youTube",
    "tfg_chatbot_movil",
    "google",
    "prueba_boton",
    "messages",
    "google play store",
    "contacts",
    "camera",
    "clock",
    "gmail",
    "duo",
    "Drive",
    "Maps",
    "chrome",
    "phone",
    "google play movies & TV",
    "webView shell",
    "photos",
    "calendar",
    "files",
    "android_chatbot",
    "settings",
    "youTube music",
    "system tracing",
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
         if app in APPS_db:
            txt = "{}d notifications for app: {}".format(action,app)
            dispatcher.utter_message(text=txt)
         else:
            txt = "{} not found in your device".format(app)
            dispatcher.utter_message(text=txt)
         return []
