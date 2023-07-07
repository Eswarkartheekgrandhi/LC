from flask import Blueprint
from flask import request

from services.authentication.tokenRequiredDecorator import tokenRequired
from services.fileUpload.detectionData.detectionData import uploadDetectionData
from services.fileUpload.trainingData.dataWithAnnotations import uploadTrainingDataWithAnnotations
from services.fileUpload.trainingData.dataWithoutAnnotations import uploadTrainingDataWithoutAnnotations

fileUploadRoutesBP = Blueprint('fileUploadRoutesBP', __name__)


@fileUploadRoutesBP.route("/image/upload/trainingDataWithAnnotations", methods=['POST'])
@tokenRequired
def uploadTrainingDataWithAnnotationRoute(user):
    """ uploadTask = Test or Train """
    uploadID = uploadTrainingDataWithAnnotations(request)
    return {'requestID': format(str(uploadID)),
            'message': "Your Training has been successfully Uploaded with Request ID {}".format(str(uploadID))}


@fileUploadRoutesBP.route('/image/upload/trainingDataWithoutAnnotations', methods=['POST'])
@tokenRequired
def uploadTrainingDataWithoutAnnotationRoute(user):
    uploadID = uploadTrainingDataWithoutAnnotations(request, user)
    return {'requestID': format(str(uploadID)),
            'message': "Your Training has been successfully Uploaded with Request ID {}".format(str(uploadID))}


@fileUploadRoutesBP.route("/image/upload/detectionData", methods=['POST'])
@tokenRequired
def uploadTestingDataWithAnnotationRoute(user):
    """ uploadTask = Test or Train """
    uploadID = uploadDetectionData(request, user)
    # response = requests.post(ENDPOINT_START_TRAINING, json=startTrainingAPIData)
    return {'requestID': format(str(uploadID)),
            'message': "Your Detection Request has been successfully Uploaded with Request ID {}".format(str(uploadID))}


