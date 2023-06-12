from services.trainModel.getTrainModelRequest import insertTrainModelRequest


from flask import Blueprint
from flask import request


trainModelRoutesBP = Blueprint('trainModelRoutesBP', __name__)


@trainModelRoutesBP.route("/trainModelRequest", methods=['POST'])
def setAnnotationRoutes():
    data = request.get_json()
    insertTrainModelRequest(data)
    return "Model Training Request has been Submitted"
