import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = input_json, headers=header)  
    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]  #estraggo il dizionario delle emozioni
    
    #trovo l'emozione dominante 
    dominant_emotion = max(emotions, key=emotions.get) 
    
    return { 
        'anger': emotions.get('anger', 0), 
        'disgust': emotions.get('disgust', 0), 
        'fear': emotions.get('fear', 0), 
        'joy': emotions.get('joy', 0), 
        'sadness': emotions.get('sadness', 0), 
        'dominant_emotion': dominant_emotion
    }
