from datetime import datetime

from constants.mongoConstants import COLLECTION_RULE_LIST, DB_VISUAL_INSPECTION, COLLECTION_FILE_UPLOAD_COUNTER
from constants.uploadFileConstants import INITIAL_UPLOAD_COUNTER
from repository.mongoRepository import insertData, getData, updateData


def createRules(data, user):
    modelName = data["modelName"]
    ruleName = data["ruleName"]
    ruleDescription = data["ruleDescription"]
    data = {
        "Rule ID": "RULE_" + str(getFileUploadIDCounter('ruleID')),
        "user": user,
        "Model Name": modelName,
        "Rule Name": ruleName,
        "Rule Description": ruleDescription,
        "Rule Creation Date": datetime.now()
    }
    insertData(data, COLLECTION_RULE_LIST, DB_VISUAL_INSPECTION)


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
