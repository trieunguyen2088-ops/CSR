import requests
import json

def emotion_detector(text_to_analyze)
    # Define the API URL and Headers
    url = 'httpssn-watson-emotion.labs.skills.networkv1watson.runtime.nlp.v1NlpServiceEmotionPredict'
    headers = {grpc-metadata-mm-model-id emotion_aggregated-workflow_lang_en_stock}
    
    # Construct the JSON payload with the text to analyze
    input_json = { raw_document { text text_to_analyze } }
    
    # Send the POST request to the Watson API
    response = requests.post(url, json=input_json, headers=headers)
    
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the emotion scores from the API response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Create a dictionary of the extracted scores to find the dominant emotion
    emotion_scores = {
        'anger' anger_score,
        'disgust' disgust_score,
        'fear' fear_score,
        'joy' joy_score,
        'sadness' sadness_score
    }
    
    # Determine the dominant emotion by finding the key with the highest value
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return the results in the required format
    return {
        'anger' anger_score,
        'disgust' disgust_score,
        'fear' fear_score,
        'joy' joy_score,
        'sadness' sadness_score,
        'dominant_emotion' dominant_emotion
    }