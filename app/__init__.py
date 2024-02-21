import os
from flask import Flask, render_template, request

app = Flask(__name__)

# main page    
@app.route('/')
def index():
    return render_template('index.html', title="Pets", url=os.getenv("URL"))