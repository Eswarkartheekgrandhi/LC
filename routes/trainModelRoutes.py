from services.authentication.tokenRequiredDecorator import tokenRequired
from services.trainModel.getTrainedModelDetails import getTrainedModelDetails
from services.trainModel.insertTrainModelRequest import insertTrainModelRequest

from flask import Blueprint
from flask import request

trainModelRoutesBP = Blueprint('trainModelRoutesBP', __name__)


@trainModelRoutesBP.route("/trainModelRequest", methods=['POST'])
@tokenRequired
def setAnnotationRoutes(user):
    data = request.get_json()
    insertTrainModelRequest(data, user)
    return "Model Training Request has been Submitted"


@trainModelRoutesBP.route("/getModelDetails", methods=["POST"])
@tokenRequired
def getModelDetailsBP(user):
    data = getTrainedModelDetails(user)
    return {"responseData": data}
