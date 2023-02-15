from flask import Blueprint
from flask import request
from services.yoloModels.getModelList import getModelList

modelRoutesBP = Blueprint('modelRoutesBP', __name__)


@modelRoutesBP.route("/models/getModelsList", methods=['GET'])
def getModelListRoute():
    modelList = getModelList()
    return modelList

