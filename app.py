from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>🇿🇦 South Africa Helper - LIVE!</h1><p>Site is working!</p>"

if __name__ == '__main__':
    app.run()
