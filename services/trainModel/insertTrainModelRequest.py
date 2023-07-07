from constants.mongoConstants import COLLECTION_TRAIN_MODEL_REQUEST_COUNTER, DB_VISUAL_INSPECTION, \
    COLLECTION_TRAIN_MODEL_REQUEST_DETAILS
from constants.uploadFileConstants import INITIAL_UPLOAD_COUNTER
from repository.mongoRepository import getData, insertData, updateData


def insertTrainModelRequest(data, user):
    modelName = data['modelName']
    imageDatasetID = data['imageDatasetID']
    modelID = getTrainModelIDCounter()
    data = {
        "modelName": modelName,
        "imageDatasetID": imageDatasetID,
        "modelID": modelID,
        "status": "SUBMITTED",
        "user": user
    }
    insertData(data, COLLECTION_TRAIN_MODEL_REQUEST_DETAILS, DB_VISUAL_INSPECTION)


def getTrainModelIDCounter():
    identifier = {'_id': "trainModelRequest"}
    data = getData(identifier, COLLECTION_TRAIN_MODEL_REQUEST_COUNTER, DB_VISUAL_INSPECTION)
    if len(data) == 0:
        fileUploadCounterData = {
            '_id': "trainModelRequest",
            'counter': str(INITIAL_UPLOAD_COUNTER["trainModelRequest"])
        }
        insertData(fileUploadCounterData, COLLECTION_TRAIN_MODEL_REQUEST_COUNTER, DB_VISUAL_INSPECTION)
        return str(INITIAL_UPLOAD_COUNTER["trainModelRequest"])
    else:
        currentCounter = int(data[0]['counter'])
        nextCounter = str(currentCounter + 1)
        updatedData = {
            '$set': {
                'counter': nextCounter
            }
        }
        updateData(identifier, updatedData, COLLECTION_TRAIN_MODEL_REQUEST_COUNTER, DB_VISUAL_INSPECTION)
        return nextCounter
