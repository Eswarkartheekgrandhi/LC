import pandas as pd

from constants.mongoConstants import COLLECTION_FILE_UPLOAD_REQUEST_DETAILS, DB_VISUAL_INSPECTION, COLLECTION_RULE_LIST
from repository.mongoRepository import getData


def getDetailedReportData(requestID):
    reportData = pd.DataFrame(
        getData({"requestID": requestID}, COLLECTION_FILE_UPLOAD_REQUEST_DETAILS, DB_VISUAL_INSPECTION)[0].get(
            "Detailed Report"))
    return reportData


def getRulesDescription(requestID):
    ruleID = getData({"requestID": requestID}, COLLECTION_FILE_UPLOAD_REQUEST_DETAILS, DB_VISUAL_INSPECTION)[0].get(
        "rulesList")
    rulesDescriptionList = \
        pd.DataFrame(getData({"Rule ID": {"$in": ruleID}}, COLLECTION_RULE_LIST, DB_VISUAL_INSPECTION))[
            "Rule Description"]
    return rulesDescriptionList


def makeDeployedRulesReport(requestID):
    reportData = getDetailedReportData(requestID)
    print(reportData)
    rulesDescriptionList = getRulesDescription(requestID)
    rulesDescriptionDF = pd.DataFrame()
    for rulesDescription in rulesDescriptionList:
        rulesDescriptionDF = pd.concat([rulesDescriptionDF, pd.DataFrame(rulesDescription)], ignore_index=True)
    print(rulesDescriptionDF)
    categories = rulesDescriptionDF["category"].unique()
    for category in categories:
        labels = rulesDescriptionDF[rulesDescriptionDF["category"] == category].reset_index()["label"].unique()



        pass

makeDeployedRulesReport("20016")
