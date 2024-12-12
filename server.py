"""app flask"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """render index page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    richiama la funzione per analizzare il testo
    """
    text_to_analyse = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyse)

    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    emotion_dominant = emotion_result['dominant_emotion']

    if emotion_dominant is None:
        return "Invalid text! Try again"
    return (
        f"For the given statement, the system response is 'anger': {anger}," 
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}."
        f" The dominant emotion is {emotion_dominant}."
    )

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5000)
