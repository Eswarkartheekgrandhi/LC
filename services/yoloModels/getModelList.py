import pandas as pd

from repository.mongoRepository import getData
from constants.mongoConstants import DB_VISUAL_INSPECTION, COLLECTION_MODEL_LIST


def getModelList():
    modelListData = getData({}, COLLECTION_MODEL_LIST, DB_VISUAL_INSPECTION)
    modelListDataDF = pd.DataFrame(modelListData)
    del (modelListDataDF["_id"])
    return {"modelList": modelListDataDF.to_dict("records")}
