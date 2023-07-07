from flask import Blueprint, send_file
from flask import request

from services.authentication.tokenRequiredDecorator import tokenRequired
from services.imageManagement.getThumbnailImages import getThumbnailImages
from services.imageManagement.getUploadedImage import getUploadedImage
from services.imageManagement.getUploadedImageDetails import getUploadedTrainingImageData, getUploadedDetectionImageData

imageManagementRoutesBP = Blueprint('imageManagementRoutesBP', __name__)


@imageManagementRoutesBP.route("/getImagesUploadDetailsByUsername", methods=['POST'])
@tokenRequired
def getImagesUploadDetailsByUsernameRoutes(user):
    response = getUploadedTrainingImageData(user)
    return response


@imageManagementRoutesBP.route("/getImageThumbnailsByRequestID", methods=['POST'])
@tokenRequired
def getImageThumbnailsByRequestIDRoutes(user):
    requestID = request.get_json()['requestID']
    response = getThumbnailImages(requestID)
    return response


@imageManagementRoutesBP.route("/getImageByImageID", methods=['POST'])
@tokenRequired
def getImageByImageIDRoutes(user):
    imageID = request.get_json()['imageID']
    response = getUploadedImage(imageID)
    return response



@imageManagementRoutesBP.route("/getDetectionImagesUploadDetails", methods=['POST'])
@tokenRequired
def getDetectionImagesUploadDetailsByUsername(user):
    response = getUploadedDetectionImageData(user)
    return response