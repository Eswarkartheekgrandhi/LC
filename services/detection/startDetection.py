import pandas as pd
import requests

from constants.mongoConstants import COLLECTION_FILE_UPLOAD_REQUEST_DETAILS, DB_VISUAL_INSPECTION, COLLECTION_RULE_LIST, \
    COLLECTION_MODEL_LIST
from constants.urlConstants import ENDPOINT_START_DETECTION
from repository.mongoRepository import getData, updateData


def startDetection(requestID):
    modelFileName = getModelFileName(requestID)
    data = {"modelName": modelFileName[0],
            "detectionID": requestID}
    response = requests.post(ENDPOINT_START_DETECTION, json=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        print(response.text)
        updateData({"requestID": requestID}, {"$set": {"status": "Completed"}}, COLLECTION_FILE_UPLOAD_REQUEST_DETAILS,
                   DB_VISUAL_INSPECTION)
    else:
        updateData({"requestID": requestID}, {"$set": {"status": "Completed"}}, COLLECTION_FILE_UPLOAD_REQUEST_DETAILS,
                   DB_VISUAL_INSPECTION)
        print("Request failed with status code:", response.status_code)


def getModelFileName(requestID):
    data = getData({"requestID": requestID}, COLLECTION_FILE_UPLOAD_REQUEST_DETAILS, DB_VISUAL_INSPECTION)
    rulesList = data[0].get("rulesList")
    modelData = pd.DataFrame(getData({"Rule ID": {"$in": rulesList}}, COLLECTION_RULE_LIST, DB_VISUAL_INSPECTION))
    modelNames = modelData["Model Name"].unique().tolist()
    modelFilesData = pd.DataFrame(
        getData({"modelName": {"$in": modelNames}}, COLLECTION_MODEL_LIST, DB_VISUAL_INSPECTION))
    return modelFilesData["modelFileName"].unique().tolist()
