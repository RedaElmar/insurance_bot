# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "info_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["name", "puissance", "carburant", "genre"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit", name=tracker.get_slot('name'),
                                 puissance=tracker.get_slot('puissance'),
                                 carburant=tracker.get_slot('carburant'),
                                 genre=tracker.get_slot('genre'))
        return []

        
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [self.from_entity(entity="name", intent='inform_name'),
                     self.from_text()],
            "puissance": [self.from_entity(entity="puissance", intent="inform_puissance"),
                        self.from_text()],
            "carburant": [self.from_entity(entity="carburant", intent="inform_carburant"),
                        self.from_text()],
            "genre": [self.from_entity(entity="genre", intent="inform_genre"),
                        self.from_text()],
        }
        
    @staticmethod
    def name_db() -> List[Text]:
        return ["anonyme",]
    
    def validate_name(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        print(value)
        if value in self.name_db():
            dispatcher.utter_message(template="utter_anon")
            return {"name": "anonyme"}
        else:
            print(value)
            dispatcher.utter_message(template="utter_welcome", name=tracker.get_slot('name'),)
            dispatcher.utter_message(template="utter_intro")
            return {"name": value}
    
    @staticmethod
    def puissance_db() -> List[Text]:


        return ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21"]
        
    def validate_puissance(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        print(value)
        if value in self.puissance_db():
            # validation succeeded, set the value of the "puissance" slot to value
            return {"puissance": value}
        else:
            print(value)
            dispatcher.utter_message(template="utter_wrong_puissance")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"puissance": None}

    @staticmethod
    def carburant_db() -> List[Text]:


        return ["diesel","essence","electrique"]

    def validate_carburant(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        print(value)
        if value.lower() in self.carburant_db():
            # validation succeeded, set the value of the "puissance" slot to value
            return {"carburant": value}
        else:
            print(value)
            dispatcher.utter_message(template="utter_wrong_carburant")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"carburant": None}

    @staticmethod
    def genre_db() -> List[Text]:

        return ["homme","femme"]

    def validate_genre(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        print(value)
        if value.lower() in self.genre_db():
            # validation succeeded, set the value of the "puissance" slot to value
            return {"genre": value}
        else:
            print(value)
            dispatcher.utter_message(template="utter_wrong_genre")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"genre": None}
