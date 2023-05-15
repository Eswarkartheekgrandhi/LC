from flask import Blueprint
from flask import request

from services.fileUpload.trainingData.dataWithAnnotations import uploadTrainingDataWithAnnotations

fileUploadRoutesBP = Blueprint('fileUploadRoutesBP', __name__)


@fileUploadRoutesBP.route("/image/upload/trainingDataWithAnnotations", methods=['POST'])
def uploadTrainingDataWithAnnotationRoute():
    """ uploadTask = Test or Train """
    uploadID = uploadTrainingDataWithAnnotations(request)
    return {'requestID': format(str(uploadID)),
            'message': "Your Training has been successfully Uploaded with Request ID {}".format(str(uploadID))}


@fileUploadRoutesBP.route("/image/upload/testingData", methods=['POST'])
def uploadTestingDataWithAnnotationRoute():
    """ uploadTask = Test or Train """
    uploadID = uploadTrainingDataWithAnnotations(request)
    # response = requests.post(ENDPOINT_START_TRAINING, json=startTrainingAPIData)
    return {'requestID': format(str(uploadID)),
            'message': "Your Training has been successfully Uploaded with Request ID {}".format(str(uploadID))}

