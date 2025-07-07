import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=payload, headers=headers)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 400:
        emotion = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
    
    else:
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        print("'anger':", emotions['anger'])
        print("'disgust':", emotions['disgust'])
        print("'fear':", emotions['fear'])
        print("'joy':", emotions['joy'])
        print("'sadness':", emotions['sadness'])
        
        max_score = emotions['anger']
        feel = 'anger'

        if(max_score < emotions['disgust']):
            max_score = emotions['disgust']
            feel = 'disgust'
        if(max_score < emotions['fear']):
            max_score = emotions['fear']
            feel = 'fear'
        if(max_score < emotions['joy']):
            max_score = emotions['joy']
            feel = 'joy'
        if(max_score < emotions['sadness']):
            max_score = emotions['sadness']
            feel = 'sadness'

        print("'dominant_emotion': " + feel)

        emotion = {"anger": emotions['anger'], "disgust": emotions['disgust'], "fear": emotions['fear'], "joy": emotions['joy'], "sadness": emotions['sadness'], "dominant_emotion": feel}
    

    return emotion
