from werkzeug.security import generate_password_hash
from datetime import datetime

from constants.jsonConstant import userSuccessfullyRegisteredJsonResponse, userAlreadyExistJsonResponse
from constants.mongoConstants import COLLECTION_USER, DB_VISUAL_INSPECTION
from repository.mongoRepository import insertData
from services.userManagement.checkExistingUser import checkExistingUser


def registerUser(data):
    name = data['name']
    email = data['email']
    hashedPassword = generate_password_hash(data['password'])
    domain = data['domain']
    organizationName = data['organizationName']
    if checkExistingUser(email):
        return userAlreadyExistJsonResponse
    userDetails = {
        'name': name,
        'email': email,
        'domain': domain,
        'password': hashedPassword,
        'organizationName': organizationName,
        'registered on': datetime.now()
    }
    insertData(userDetails, COLLECTION_USER, DB_VISUAL_INSPECTION)
    return userSuccessfullyRegisteredJsonResponse
