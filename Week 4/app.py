
from flask import Flask, render_template, request, redirect, url_for, jsonify
from joblib import load
import sys
# from get_tweets import get_related_tweets


pipeline = load("text_classification.joblib")


# def requestResults(name):
#     tweets = get_related_tweets(name)
#     tweets['prediction'] = pipeline.predict(tweets['tweet_text'])
#     data = str(tweets.prediction.value_counts()) + '\n\n'
#     return data + str(tweets)
    
# start flask
app = Flask(__name__)  

# render default webpage
# @app.route('/')
# def home():
#     return render_template('index.html')

# when the post method detect, then redirect to success function
@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        # print('here we are!', file=sys.stderr)
        print(request.form)
        user = request.form['search']
    
        # Returns array, takes parameter as array
        # result = pipeline.predict([user])
        # return result[0]
        return redirect(url_for('/'))
        # return render_template(url_for('index.html'), name = user)
    else:
        return render_template('index.html')

@app.route('/get-sentiment', methods=['POST'])
def koisabhi():
    if request.method == 'POST':
        user = request.form['search']
        predarr = pipeline.predict([user])
        predarr = predarr[0]
        # return render_template(url_for('1.html'), result = result)
        return predarr

# @app.route('/result', methods=['POST','GET'])
# def routeHit():
#     if request.method == 'GET':
#         return render_template('index2.html')


# get the data for the requested query
# @app.route('/success/<name>')
# def success(name):
#     # return "<xmp>" + str(requestResults(name)) + " </xmp> "
#     user = request.form['search']
#     result = pipeline.predict(user)
#     result = result[0]
#     return render_template(url_for('index.html'), result = result)

if __name__ == '__main__' :
    app.run(debug=True)