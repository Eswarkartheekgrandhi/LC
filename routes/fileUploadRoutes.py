from flask import Blueprint
from flask import request
import requests

from constants.urlConstants import ENDPOINT_START_TRAINING
from services.yoloModels.fileUploads import uploadFiles
from services.yoloModels.getModelList import getModelList

fileUploadRoutesBP = Blueprint('fileUploadRoutesBP', __name__)


@fileUploadRoutesBP.route("/image/upload/<uploadTask>", methods=['POST'])
def uploadAndTest(uploadTask):
    """ uploadTask = Test or Train """
    modelName = request.form.get('modelName')
    uploadID = uploadFiles(request, uploadTask)
    if uploadTask == 'test':
        startTrainingAPIData = {
            'modelName': modelName,
            'testUploadID': uploadID
        }
        response = requests.post(ENDPOINT_START_TRAINING, json=startTrainingAPIData)
    return "Your File has been successfully Uploaded and Tested with Request ID {}".format(str(uploadID))
