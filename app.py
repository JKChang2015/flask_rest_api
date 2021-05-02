import argparse
import os

from flask import Flask, jsonify, make_response,redirect,url_for
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from routes import ensembl_api

app = Flask(__name__)

## swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Ensembl-Python-Flask-REST"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

app.register_blueprint(ensembl_api.get_blueprint())

# redirect root page to swagger
@app.route('/')
def hello():
    return redirect(SWAGGER_URL)

@app.errorhandler(400)
def handle_400_error(_error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def handle_404_error(_error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
        description="Ensembl-Python-Flask-REST")

    PARSER.add_argument('--debug', action='store_true',
                        help="Use flask debug/dev mode with file change reloading")
    ARGS = PARSER.parse_args()

    PORT = int(os.environ.get('PORT', 5000))

    if ARGS.debug:
        print("Running in debug mode")
        CORS = CORS(app)
        app.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        app.run(host='0.0.0.0', port=PORT, debug=False)
