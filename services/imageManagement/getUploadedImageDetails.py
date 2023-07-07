import pandas as pd

from constants.mongoConstants import COLLECTION_FILE_UPLOAD_REQUEST_DETAILS, DB_VISUAL_INSPECTION, \
    COLLECTION_IMAGE_RECORDS
from constants.uploadFileConstants import STATUS_IMAGE_UNANNOTATED, STATUS_IMAGE_ANNOTATED, \
    STATUS_IMAGE_PARTIALLY_ANNOTATED
from repository.mongoRepository import getData


def getUploadedTrainingImageData(user):
    uploadedDataDF = pd.DataFrame(
        getData({'user': user, 'dataType': 'trainingData'}, COLLECTION_FILE_UPLOAD_REQUEST_DETAILS,
                DB_VISUAL_INSPECTION))
    if len(uploadedDataDF) == 0:
        return "No Images Uploaded by the User"
    UploadedImageDataDF = pd.DataFrame()
    for i in range(len(uploadedDataDF)):
        requestID = uploadedDataDF.loc[i, 'requestID']
        uploadedDateTime = uploadedDataDF.loc[i, 'datetime']
        label = uploadedDataDF.loc[i, 'label']
        uploadedAnnotatedImageLen = len(getData({'requestID': requestID,
                                                 'annotationStatus': STATUS_IMAGE_ANNOTATED},
                                                COLLECTION_IMAGE_RECORDS,
                                                DB_VISUAL_INSPECTION))
        uploadedUnannotatedImageLen = len(getData({'requestID': requestID,
                                                   'annotationStatus': STATUS_IMAGE_UNANNOTATED},
                                                  COLLECTION_IMAGE_RECORDS,
                                                  DB_VISUAL_INSPECTION))
        totalUploadedImages = uploadedAnnotatedImageLen + uploadedUnannotatedImageLen
        if uploadedAnnotatedImageLen == 0:
            status = STATUS_IMAGE_UNANNOTATED
        elif uploadedUnannotatedImageLen == 0:
            status = STATUS_IMAGE_ANNOTATED
        else:
            status = STATUS_IMAGE_PARTIALLY_ANNOTATED
        UploadedImageDataDict = {
            'requestID': requestID,
            'Upload DateTime': uploadedDateTime,
            'Label': label,
            'Total Images': totalUploadedImages,
            'Total Annotated Image': uploadedAnnotatedImageLen,
            'Total Unannotated Image': uploadedUnannotatedImageLen,
            'Status': status
        }
        UploadedImageDataDF = UploadedImageDataDF.append(UploadedImageDataDict, ignore_index=True)
    print(UploadedImageDataDF)
    return UploadedImageDataDF.to_dict('records')


def getUploadedDetectionImageData(user):
    uploadedDataDF = pd.DataFrame(
        getData({'user': user, 'dataType': 'detectionData'}, COLLECTION_FILE_UPLOAD_REQUEST_DETAILS, DB_VISUAL_INSPECTION))
    if len(uploadedDataDF) == 0:
        return "No Images Uploaded by the User"
    uploadedDataDF = uploadedDataDF.drop(['_id'], axis=1)
    uploadedDataDF = uploadedDataDF.fillna("Data Not Available")
    return uploadedDataDF.to_dict('records')
