import base64
from io import BytesIO

import pandas as pd
from PIL import Image

from constants.mongoConstants import COLLECTION_FILE_UPLOAD_REQUEST_DETAILS, DB_VISUAL_INSPECTION, \
    COLLECTION_IMAGE_RECORDS
from constants.uploadFileConstants import STATUS_IMAGE_UNANNOTATED, STATUS_IMAGE_ANNOTATED, \
    STATUS_IMAGE_PARTIALLY_ANNOTATED, IMAGE_FILE_EXTN
from repository.mongoRepository import getData


def getThumbnailImages(requestID):
    imageDetailsDF = pd.DataFrame(getData({'requestID': requestID}, COLLECTION_IMAGE_RECORDS, DB_VISUAL_INSPECTION))
    imageThumbnailDetailsList = []
    for i in range(len(imageDetailsDF)):
        imageLocation = imageDetailsDF.loc[i, 'destination']
        imageType = imageLocation.split(".")[-1]
        thumbnailBase64 = createThumbnail(imageLocation, imageType)
        imageThumbnailDetails = {
            'imageID': imageDetailsDF.loc[i, 'fileID'],
            'imageThumbnail': thumbnailBase64,
            'status': imageDetailsDF.loc[i, 'annotationStatus'],
        }
        imageThumbnailDetailsList.append(imageThumbnailDetails)
    return {"data": imageThumbnailDetailsList}


def createThumbnail(imagePath, imageType, size=(128, 128)):
    with Image.open(imagePath) as img:
        img.thumbnail(size)
        byte_io = BytesIO()
        print(IMAGE_FILE_EXTN[imageType])
        img.save(byte_io, IMAGE_FILE_EXTN['png'])
        byte_io.seek(0)
        byte_arr = byte_io.getvalue()
        base64_encoded_result = base64.b64encode(byte_arr).decode('ascii')
        return base64_encoded_result


