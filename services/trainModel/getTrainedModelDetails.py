import pandas as pd

from constants.mongoConstants import COLLECTION_MODEL_LIST, DB_VISUAL_INSPECTION
from repository.mongoRepository import getData


def getTrainedModelDetails():
    data = getData({}, COLLECTION_MODEL_LIST, DB_VISUAL_INSPECTION)
    dataDF = pd.DataFrame(data)
    dataDF = dataDF.drop(['_id'], axis=1)
    return dataDF.to_dict("records")


