import dialogflow_v2
from config import Config

class Chat():

    client = dialogflow_v2.AgentsClient()
    parent = client.project_path
    SESSION_ID = Config.DIALOGFLOW_CONFIG_JSON['session_id']
    PROJECT_ID = Config.DIALOGFLOW_CONFIG_JSON['project_id']
    LANGUAGE_CODE = Config.DIALOGFLOW_CONFIG_JSON['language']

    session_client = dialogflow_v2.SessionsClient()
    session = session_client.session_path(PROJECT_ID, SESSION_ID)

    def send_message(self, text):
        text_input = dialogflow_v2.types.TextInput(text=text, language_code=self.LANGUAGE_CODE)

        query_input = dialogflow_v2.types.QueryInput(text=text_input)
        try:
            response = self.session_client.detect_intent(session=self.session, query_input=query_input)
        except:
            print('Exception')
        
        return 'Fulfillment text: {}'.format(response.query_result.fulfillment_text)