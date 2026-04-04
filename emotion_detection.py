'''
An emotion detection application using the Watson NLP library
'''
import json
import operator
import requests # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):
    '''
    A function that takes a string input (text_to_analyse)
    '''
    # URL of the emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/'
    url += 'NlpService/EmotionPredict'
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json = myobj, headers=header, timeout=5)
    #return response.text # Return the response text from the API
    # Parse the response from the API
    formatted_response = json.loads(response.text)
    #return formatted_response
    # Extracting required set of emotions,
    # including anger, disgust, fear, joy and sadness,
    # along with their scores from the resp
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion_key = max(emotions.items(), key=operator.itemgetter(1))[0]
    emotions['dominant_emotion'] = dominant_emotion_key
    return emotions

