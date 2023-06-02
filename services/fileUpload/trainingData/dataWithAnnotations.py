import os
from datetime import datetime

from werkzeug.utils import secure_filename

from constants.mongoConstants import COLLECTION_FILE_UPLOAD_COUNTER, DB_VISUAL_INSPECTION, COLLECTION_FILE_UPLOAD_REQUEST_DETAILS
from constants.uploadFileConstants import INITIAL_UPLOAD_COUNTER, DATA_DIRECTORY, STATUS_FILE_UPLOADED
from repository.mongoRepository import getData, updateData, insertData


def uploadTrainingDataWithAnnotations(data):
    imageList = data.files.getlist("imageFiles")
    imageList = data.files.getlist("imageFiles")
    annotationList = data.files.getlist("annotationFiles")
    dataYamlFileList = data.files.getlist("dataYamlFile")
    requestID = getFileUploadIDCounter("train")
    saveRecord(requestID, "train")
    imageFileDirectory = getFileDirectory("trainImage", requestID)
    saveFileToDirectory(imageList, imageFileDirectory)
    annotationFileDirectory = getFileDirectory("trainAnnotation", requestID)
    saveFileToDirectory(annotationList, annotationFileDirectory)
    dataYamlFileDirectory = getFileDirectory("dataYamlFile", requestID)
    saveFileToDirectory(dataYamlFileList, dataYamlFileDirectory)
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


def saveRecord(requestID, uploadTask):
    recordDict = {
        'requestID': requestID,
        'datetime': datetime.now(),
        'datetime': datetime.now(),
        'status': STATUS_FILE_UPLOADED
    }
    collectionName = COLLECTION_FILE_UPLOAD_REQUEST_DETAILS
    insertData(recordDict, collectionName, DB_VISUAL_INSPECTION)


def saveFileToDirectory(fileList, fileDirectory):
    for fileElement in fileList:
        filename = fileElement.filename
        filename = secure_filename(filename)
        destination = os.path.join(fileDirectory, filename)
        fileElement.save(destination)
