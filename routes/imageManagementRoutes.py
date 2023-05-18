from flask import Blueprint, send_file
from flask import request

from services.imageManagement.getThumbnailImages import getThumbnailImages
from services.imageManagement.getUploadedImage import getUploadedImageData

imageManagementRoutesBP = Blueprint('imageManagementRoutesBP', __name__)


@imageManagementRoutesBP.route("/getImagesUploadDetailsByUsername", methods=['POST'])
def getImagesUploadDetailsByUsernameRoutes():
    user = request.get_json()['user']
    print(user)
    response = getUploadedImageData(user)
    return response


@imageManagementRoutesBP.route("/getImageThumbnailsByRequestID", methods=['POST'])
def getImageThumbnailsByRequestIDRoutes():
    requestID = request.get_json()['requestID']
    print(requestID)
    response = getThumbnailImages(requestID)
    return response