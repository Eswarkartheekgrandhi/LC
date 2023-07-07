import pandas as pd

from constants.mongoConstants import COLLECTION_MODEL_LIST, DB_VISUAL_INSPECTION, COLLECTION_USER
from repository.mongoRepository import getData


def getTrainedModelDetails(user):
    userData = pd.DataFrame(getData({'email': user}, COLLECTION_USER, DB_VISUAL_INSPECTION))
    domain = userData["domain"].unique()[0]
    data = getData({'domain': domain}, COLLECTION_MODEL_LIST, DB_VISUAL_INSPECTION)
    dataDF = pd.DataFrame(data)
    dataDF = dataDF.drop(['_id'], axis=1)
    return dataDF.to_dict("records")
