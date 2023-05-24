from constants.mongoConstants import DB_VISUAL_INSPECTION, \
    COLLECTION_IMAGE_RECORDS
from constants.uploadFileConstants import STATUS_IMAGE_ANNOTATED
from repository.mongoRepository import updateData


def setAnnotations(imageID, annotations):
    updateData({"fileID": imageID}, {"$set": {"annotations": annotations,
                                              "annotationStatus": STATUS_IMAGE_ANNOTATED}}, COLLECTION_IMAGE_RECORDS,
               DB_VISUAL_INSPECTION)
    return
