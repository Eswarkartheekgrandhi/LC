import os

import pandas as pd
import shutil

from constants.mongoConstants import DB_VISUAL_INSPECTION, COLLECTION_IMAGE_RECORDS
from constants.uploadFileConstants import DATA_DIRECTORY
from repository.mongoRepository import getData


def getImageList(requestID):
    data = getData({'requestID': '10012', "annotationStatus": "Unannotated"}, COLLECTION_IMAGE_RECORDS,
                   DB_VISUAL_INSPECTION)
    dataDF = pd.DataFrame(data)
    return dataDF['destination']


def getImages(requestArray, modelRequestID):
    trainingDirectory = getFileDirectory(modelRequestID)
    for requestID in requestArray:
        imageList = getImageList(requestID)
        for imageDirectory in imageList:
            print(imageDirectory)
            copyImages(imageDirectory, trainingDirectory)


def copyImages(imageDirectory, trainingDirectory):
    shutil.copy(imageDirectory, trainingDirectory)


def getFileDirectory(requestID):
    fileDirectory = DATA_DIRECTORY["trainModel"].format(requestID)
    try:
        os.makedirs(fileDirectory)
    except:
        pass
    return fileDirectory


print(getImages(["100012"], "30002"))
