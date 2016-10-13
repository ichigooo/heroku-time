from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def countdown():
    sec = str(time.time())
    return sec + " seconds from the start of Jan. 1st, 1970!"

if __name__ == '__main__':
    app.run()
