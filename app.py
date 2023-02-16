from flask import Flask
from flask_cors import CORS

import logging
from routes.modelRoutes import modelRoutesBP
from routes.fileUploadRoutes import fileUploadRoutesBP
from routes.reportRoutes import reportRoutesBP
from services.fileUpload.sftpConnection import *


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')
app = Flask(__name__)
CORS(app)


app.register_blueprint(modelRoutesBP)
app.register_blueprint(fileUploadRoutesBP)
app.register_blueprint(reportRoutesBP)

@app.route('/status', methods=['GET'])
def getStatus():
    return "Visual Inspection API's are runningggggg"


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    # app.run(debug=True,host="0.0.0.0",use_reloader=False)
    app.run(host='127.0.0.1',port=5000,debug=True, use_reloader=False)
