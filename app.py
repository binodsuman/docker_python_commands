from flask import Flask
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

flaskApp = Flask(__name__)

@flaskApp.route("/")
def hello():
    logging.info("This is log for hello method")
    return "<h1>Binod Suman Academy YouTube 12 </h1>"

if __name__ == "__main__":
    #flaskApp.run(debug=True, host='0.0.0.0', port=8080) 
    flaskApp.run()
    