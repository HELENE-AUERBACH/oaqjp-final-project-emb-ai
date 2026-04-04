''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
# render_template function for deploying the HTML file
# and request function to initiate the GET request from the web page
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app and name it Emotion Detector :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector() function.
        The output returned shows the emotions and the dominant
        emotion for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    #if len(text_to_analyze) == 0:
    #    return "None input! Try again."

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the emotions and dominant emotion
    # Check if the dominant_emotion is None, indicating a blank entrie
    if dominant_emotion is None:
        return "<b>Invalid text! Please try again!</b>"

    # Return a formatted string with the emotions and dominant emotion
    return f"For the given statement, the system response is 'anger': {anger}, \
        'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
        The dominant emotion is <b>{dominant_emotion}</b>."

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template('index.html')

#This functions executes the flask app and deploys it on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
