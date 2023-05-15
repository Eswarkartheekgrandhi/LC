from werkzeug.security import check_password_hash, generate_password_hash

from constants.jsonConstant import userEmailNotFoundJsonResponse, userSuccessfullyValidatedJsonResponse, \
    incorrectPasswordJsonResponse
from constants.mongoConstants import COLLECTION_USER, DB_VISUAL_INSPECTION
from repository.mongoRepository import getData
from services.userManagement.checkExistingUser import checkExistingUser


def validateUser(data):
    email = data['email']
    password = data['password']

    if not checkExistingUser(email):
        return userEmailNotFoundJsonResponse

    hashedPassword = getData({"email": email}, COLLECTION_USER, DB_VISUAL_INSPECTION)[0]['password']

    is_password_valid = check_password_hash(hashedPassword, password)

    if is_password_valid:
        return userSuccessfullyValidatedJsonResponse
    else:
        return incorrectPasswordJsonResponse
