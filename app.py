from flask import Flask
from flask_cors import CORS

import logging

from routes.annotationRoutes import annotationRoutesBP
from routes.imageManagementRoutes import imageManagementRoutesBP
from routes.modelRoutes import modelRoutesBP
from routes.fileUploadRoutes import fileUploadRoutesBP
from routes.reportRoutes import reportRoutesBP
from routes.ruleManagementRoutes import ruleManagementRoutesBP
from routes.trainModelRoutes import trainModelRoutesBP
from routes.userManagementRoutes import userManagementRoutesBP
from services.domain.getDomainDetails import getDomainDetails
from services.reports.getDeployedRulesResult import getRulesDescription

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')
app = Flask(__name__)
CORS(app)

app.register_blueprint(modelRoutesBP)
app.register_blueprint(fileUploadRoutesBP)
app.register_blueprint(reportRoutesBP)
app.register_blueprint(userManagementRoutesBP)
app.register_blueprint(imageManagementRoutesBP)
app.register_blueprint(annotationRoutesBP)
app.register_blueprint(trainModelRoutesBP)
app.register_blueprint(ruleManagementRoutesBP)


@app.route('/status', methods=['GET'])
def getStatus():
    return "Visual Inspection APIs are running"


if __name__ == "__main__":
    # app.secret_key = os.urandom(24)
    # app.run(debug=True,host="0.0.0.0",use_reloader=False)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
