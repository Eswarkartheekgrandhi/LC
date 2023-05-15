from constants.mongoConstants import COLLECTION_USER, DB_VISUAL_INSPECTION
from repository.mongoRepository import getData


def checkExistingUser(email):
    if len(getData({'email': email}, COLLECTION_USER, DB_VISUAL_INSPECTION)) == 0:
        return False
    else:
        return True
