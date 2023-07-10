from constants.mongoConstants import COLLECTION_DOMAIN_DETAILS, DB_VISUAL_INSPECTION
from repository.mongoRepository import getData


def getDomainDetails():
    data = getData({}, COLLECTION_DOMAIN_DETAILS, DB_VISUAL_INSPECTION)
    print(data)


getDomainDetails()