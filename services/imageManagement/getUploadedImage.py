import base64
from io import BytesIO

import pandas as pd
from PIL import Image

from constants.mongoConstants import COLLECTION_FILE_UPLOAD_REQUEST_DETAILS, DB_VISUAL_INSPECTION, \
    COLLECTION_IMAGE_RECORDS
from constants.uploadFileConstants import STATUS_IMAGE_UNANNOTATED, STATUS_IMAGE_ANNOTATED, \
    STATUS_IMAGE_PARTIALLY_ANNOTATED, IMAGE_FILE_EXTN
from repository.mongoRepository import getData


def getUploadedImage(imageID):
    data = getData({'fileID': imageID}, COLLECTION_IMAGE_RECORDS, DB_VISUAL_INSPECTION)
    print(data)
    imagePath = data[0]['destination']
    imageType = imagePath.split(".")[-1]
    base64Image = getBase64Image(imagePath, imageType)
    annotations = data[0]['annotations']
    annotationStatus = data[0]['annotationStatus']
    data = {
        'imageID' : imageID,
        'base64Image' : base64Image,
        'annotations' : annotations,
        'annotationStatus' : annotationStatus
    }
    return data


def getBase64Image(imagePath, imageType):
    with Image.open(imagePath) as img:
        byte_io = BytesIO()
        img.save(byte_io, IMAGE_FILE_EXTN[imageType])
        byte_io.seek(0)
        byte_arr = byte_io.getvalue()
        base64_encoded_result = base64.b64encode(byte_arr).decode('ascii')
        return base64_encoded_result


