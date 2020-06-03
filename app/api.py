import json
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



authenticator = IAMAuthenticator('kEjPZFaAFyeqY0Fh6CKouCJ2linC5LEHbsO34UH73sWq')

assistant = AssistantV1(
    version='2019-02-06',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/ceb1df42-ea16-4a1a-b553-0d811055a1ec')


def parseResponseText(responseText):
    jsonString = json.loads(responseText) 
    return jsonString['output']['text'][0]

def getMessage(requestText):
    response = assistant.message(
        workspace_id='4d7b8bcf-c19c-4989-8b8c-0db66812b8ca',
        input={
            'message_type': 'text',
            'text': requestText
        }
    ).get_result()
    parsedResponse = parseResponseText(json.dumps(response, indent=2)) 
    return parsedResponse



    


