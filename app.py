from flask import Flask, jsonify
import tweepy

app = Flask(__name__)


@app.route('/<username>')
def feed(username):
    tweets = [{'some': 'tweets'}] #tweepy.api.user_timeline(username)
    return jsonify(tweets=tweets)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
