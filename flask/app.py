from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

port = int(os.getenv('PORT', 81))
app.run(host='0.0.0.0', port=port)