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
import psycopg2
import re

class controlNotifications(Action):

     def name(self) -> Text:
         return "action_notification"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         app = next(tracker.get_latest_entity_values("name_app"), None)
         action = next(tracker.get_latest_entity_values("action"), None)
         print(app)
         print(action)
         installed_apps = conectionToDB(tracker)
         if action is None: 
             syntaxAction = "controlled"
             action = "control"
         else:
             syntaxAction = sintaxAction(action)
         if app is not None:
            fuzzy = process.extractOne(app, installed_apps)
            if fuzzy[1] >= 80:
                txt = "{} notifications for {}".format(syntaxAction,fuzzy[0])
                flutt = action+"_notification_"+fuzzy[0]
            else:
                txt = "{} not found in your device".format(app)
                flutt = "undefined"
            date_response = {
                "text": txt,
                "flutteraction": flutt
            }
            dispatcher.utter_message(json_message = date_response)
            return []
         else:
            txt = "Could not identify the application, please indicate a proper app name"
            flutt = "undefined"
            date_response = {
                "text": txt,
                "flutteraction": flutt
            }
            dispatcher.utter_message(json_message = date_response)


class restrictData(Action):

     def name(self) -> Text:
         return "action_restrict_data"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         app = next(tracker.get_latest_entity_values("name_app"), None)
         action = next(tracker.get_latest_entity_values("action"), None)
         print(app)
         installed_apps = conectionToDB(tracker)
         print("Installed apps"+str(installed_apps))
         if action is None: 
             syntaxAction = "controlled"
             action = "control"
         else:
             syntaxAction = sintaxAction(action)
         if app is not None:
            fuzzy = process.extractOne(app, installed_apps)
            print(fuzzy)
            if fuzzy[1] >= 80:
                txt = "{} data usage for {}".format(syntaxAction,fuzzy[0])
                flutt = action+"_datausage_"+fuzzy[0]
            else:
                txt = "{} not found in your device".format(app)
                flutt = "undefined"
            date_response = {
                "text": txt,
                "flutteraction": flutt
            }
            dispatcher.utter_message(json_message = date_response)
            return []
         else:
            txt = "Could not identify the application, please indicate a proper app name"
            flutt = "undefined"
            date_response = {
                "text": txt,
                "flutteraction": flutt
            }
            dispatcher.utter_message(json_message = date_response)


class batteryOptimization(Action):

     def name(self) -> Text:
         return "action_battery_opt"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         app = next(tracker.get_latest_entity_values("name_app"), None)
         action = next(tracker.get_latest_entity_values("action"), None)
         print(app)
         print("Sender_id"+str(tracker.sender_id))
         installed_apps = conectionToDB(tracker)
         print("Installed apps"+str(installed_apps))
         if action is None: 
             syntaxAction = "controlled"
             action = "control"
         else:
             syntaxAction = sintaxAction(action)
         if app is not None:
            fuzzy = process.extractOne(app, installed_apps)
            print(fuzzy)
            if fuzzy[1] >= 80:
                txt = "{} battery optimization for {}".format(syntaxAction,fuzzy[0])
                flutt = action+"_batteryopt_"+fuzzy[0]
            else:
                txt = "{} not found in your device".format(app)
                flutt = "undefined"
            date_response = {
                "text": txt,
                "flutteraction": flutt
            }
            dispatcher.utter_message(json_message = date_response)
            return []
         else:
            txt = "Could not identify the application, please indicate a proper app name"
            flutt = "undefined"
            date_response = {
                "text": txt,
                "flutteraction": flutt
            }
            dispatcher.utter_message(json_message = date_response)

class permissionsApp(Action):

     def name(self) -> Text:
         return "action_permissions_app"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         app = next(tracker.get_latest_entity_values("name_app"), None)
         action = next(tracker.get_latest_entity_values("action"), None)
         print(app)
         print("Sender_id"+str(tracker.sender_id))
         installed_apps = conectionToDB(tracker)
         print("Installed apps"+str(installed_apps))
         if action is None: 
             syntaxAction = "controlled"
             action = "control"
         else:
             syntaxAction = sintaxAction(action)
         if app is not None:
            fuzzy = process.extractOne(app, installed_apps)
            print(fuzzy)
            if fuzzy[1] >= 80:
                txt = "{} permissions for {}".format(syntaxAction,fuzzy[0])
                flutt = action+"_permissions_"+fuzzy[0]
            else:
                txt = "{} not found in your device".format(app)
                flutt = "undefined"
            date_response = {
                "text": txt,
                "flutteraction": flutt
            }
            dispatcher.utter_message(json_message = date_response)
            return []
         else:
            txt = "Could not identify the application, please indicate a proper app name"
            flutt = "undefined"
            date_response = {
                "text": txt,
                "flutteraction": flutt
            }
            dispatcher.utter_message(json_message = date_response)


def conectionToDB(tracker):
    try:
        connection = psycopg2.connect(host="chatbot_rasa-postgres-1",dbname="rasa",user="project_admin",password="root")
        cursor = connection.cursor()
        query =  "SELECT app_names FROM public.users WHERE email = %s"
        cursor.execute(query, (tracker.sender_id,))
        result = cursor.fetchall()[0][0]
        cursor.close()
        connection.close()
        return result
    except:
        return []

def sintaxAction(action):
    if re.search("[aeiou]$",action):
        return action[:-1]+"ed"
    elif re.search("[lp]$",action):
        return action+action[-1]+"ed"
    return action