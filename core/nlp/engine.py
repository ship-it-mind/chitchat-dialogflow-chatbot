import os
from dotenv import load_dotenv
import dialogflow_v2 as dialogflow

from extensions import LOGGER

basedir = os.path.abspath(os.path.dirname(__file__))

dot_env_path = os.path.join(os.path.dirname(__file__),
                            os.path.join(os.getcwd(), '.env'))
load_dotenv(dot_env_path)

DIALOGFLOW_PROJECT_ID = os.getenv('DIALOGFLOW_PROJECT_ID')


class NLPEngine:
    def __init__(self):
        self.session_client = dialogflow.SessionsClient()
        self.session_context = dialogflow.ContextsClient()

    def detect_language(self, text, last_lang='ar', current_locale='ar'):
        locale = self.get_current_locale(current_locale)
        if locale is None and last_lang is not None:
            locale = last_lang
        elif locale is None and last_lang is None:
            locale = "ar"
        text = text.lower().strip()

        if len(text.split()) == 1:
            try:
                language = self.translate.detect(text)
                if language in ['en', 'ar']:
                    return language
                elif last_lang is not None:
                    return last_lang
                else:
                    return 'ar'
            except Exception:
                return last_lang
        try:
            language = self.translate.detect(text)
            if language in ['en', 'ar']:
                return language
            elif last_lang is not None:
                return last_lang
            else:
                return 'ar'
        except Exception:
            return last_lang

    @staticmethod
    def get_current_locale(locale):
        if locale.startswith("en"):
            return "en"
        elif locale.startswith("er"):
            return "er"
        else:
            return None

    def predict(self, user_id, message, last_lang='ar', current_locale='ar'):
        language = self.detect_language(message, last_lang, current_locale)
        intent = self.detect_intent_texts(
            user_id=user_id,
            text=message,
            language_code= language
        )
        return intent

    def detect_intent_texts(self, user_id, text, language_code):
        """Returns the result of detect intent with texts as inputs.
    
        Using the same `user_id` between requests allows continuation
        of the conversation."""
        LOGGER.info(user_id)
        LOGGER.info(language_code)
        LOGGER.info(text)
        session = self.session_client.session_path(DIALOGFLOW_PROJECT_ID, user_id)
        context = self.session_context.session_path(DIALOGFLOW_PROJECT_ID, user_id)
        text_input = dialogflow.types.TextInput(
            text=text, language_code="en")
    
        query_input = dialogflow.types.QueryInput(text=text_input)
    
        response = self.session_client.detect_intent(
            session=session, query_input=query_input)
        try:
            intent = response.query_result.fulfillment_text
        except:
            intent = ""
        try:
            action = response.query_result.action
        except:
            action = ""  
        return intent, action, language_code
