from datetime import datetime, timedelta

import jwt
from werkzeug.security import check_password_hash, generate_password_hash

from constants.applicationConstant import SECRET_KEY
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
        token = jwt.encode({
            'user': email,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, SECRET_KEY)
        return {"statusCode": 200,
                "token": token,
                "message": "User Successfully Validated"}
    else:
        return incorrectPasswordJsonResponse
