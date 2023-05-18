import os
from datetime import datetime

from werkzeug.utils import secure_filename

from constants.mongoConstants import COLLECTION_FILE_UPLOAD_COUNTER, DB_VISUAL_INSPECTION, \
    COLLECTION_FILE_UPLOAD_REQUEST_DETAILS, COLLECTION_IMAGE_RECORDS
from constants.uploadFileConstants import INITIAL_UPLOAD_COUNTER, DATA_DIRECTORY, STATUS_FILE_UPLOADED, \
    STATUS_IMAGE_UNANNOTATED
from repository.mongoRepository import getData, updateData, insertData


def uploadTrainingDataWithoutAnnotations(data):
    imageList = data.files.getlist("imageFiles")
    label = data.form['label']
    user = data.form['user']
    requestID = getFileUploadIDCounter("train")
    saveRecord(requestID, label, user, "train")
    imageFileDirectory = getFileDirectory("trainImage", requestID)
    saveFileToDirectory(imageList, imageFileDirectory, requestID)
    return requestID


def getFileUploadIDCounter(uploadTask):
    identifier = {'_id': uploadTask}
    data = getData(identifier, COLLECTION_FILE_UPLOAD_COUNTER, DB_VISUAL_INSPECTION)
    if len(data) == 0:
        fileUploadCounterData = {
            '_id': uploadTask,
            'counter': str(INITIAL_UPLOAD_COUNTER[uploadTask])
        }
        insertData(fileUploadCounterData, COLLECTION_FILE_UPLOAD_COUNTER, DB_VISUAL_INSPECTION)
        return str(INITIAL_UPLOAD_COUNTER[uploadTask])
    else:
        currentCounter = int(data[0]['counter'])
        nextCounter = str(currentCounter + 1)
        updatedData = {
            '$set': {
                'counter': nextCounter
            }
        }
        updateData(identifier, updatedData, COLLECTION_FILE_UPLOAD_COUNTER, DB_VISUAL_INSPECTION)
        return nextCounter


def getFileDirectory(uploadTask, requestID):
    fileDirectory = DATA_DIRECTORY[uploadTask].format(requestID)
    try:
        os.makedirs(fileDirectory)
    except:
        pass
    return fileDirectory


def saveRecord(requestID, label, user, uploadTask):
    recordDict = {
        'requestID': requestID,
        'datetime': datetime.now(),
        'label': label,
        'user': user,
        'status': STATUS_FILE_UPLOADED,
        'annotations': []
    }
    collectionName = COLLECTION_FILE_UPLOAD_REQUEST_DETAILS
    insertData(recordDict, collectionName, DB_VISUAL_INSPECTION)


def saveFileToDirectory(fileList, fileDirectory, requestID):
    for i in range(len(fileList)):
        fileElement = fileList[i]
        filename = fileElement.filename
        filename = secure_filename(filename)
        destination = os.path.join(fileDirectory, filename)
        saveFileRecordToMongo(filename, requestID, i + 1, destination)
        fileElement.save(destination)


def saveFileRecordToMongo(filename, requestID, fileID, destination):
    fileRecordData = {
        "filename": filename,
        "requestID": requestID,
        "fileID": "IMG_{}_{}".format(str(requestID), str(fileID)),
        "destination": destination,
        "annotationStatus": STATUS_IMAGE_UNANNOTATED
    }
    insertData(fileRecordData, COLLECTION_IMAGE_RECORDS, DB_VISUAL_INSPECTION)
