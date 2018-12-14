import os
from flask import Flask, render_template, jsonify
from genTweet import TweetGenerator
import pickle
from markov import markovChain, sentenceStarters

app = Flask(__name__)

tweetGenerator = TweetGenerator(markovChain, sentenceStarters)

@app.route('/')
def index():
    return render_template('index.html', tweet="Arrrr ya ready? I talk like spongebob! Click below to see more!")

@app.route('/tweets')
def tweets():
	tweet = tweetGenerator.makeSentence()
	return jsonify({'tweet': tweet})

if __name__ == '__main__':
    app.run(debug=False)