import requests
import json

def emotion_detector(text_to_analyse):  

    emotions = {}

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = input_json, headers=header)
    status_code = response.status_code

    if status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]  #estraggo il dizionario delle emozioni
    
        #trovo l'emozione dominante 
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion 
    
    elif status_code == 400:
        emotions['anger'] = None
        emotions['disgust'] = None
        emotions['fear'] = None
        emotions['joy'] = None
        emotions['sadness'] = None
        emotions['dominant_emotion'] = None
    
    return emotions
