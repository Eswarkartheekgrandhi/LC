from datetime import datetime

from constants.mongoConstants import COLLECTION_RULE_LIST, DB_VISUAL_INSPECTION
from repository.mongoRepository import insertData


def createRules(data):
    modelName = data["modelName"]
    ruleName = data["ruleName"]
    ruleDescription = data["ruleDescription"]
    data = {
        "Model Name": modelName,
        "Rule Name": ruleName,
        "Rule Description": ruleDescription,
        "Rule Creation Date": datetime.now()
    }
    insertData(data, COLLECTION_RULE_LIST, DB_VISUAL_INSPECTION)

