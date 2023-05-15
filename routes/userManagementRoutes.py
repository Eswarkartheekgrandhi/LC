from flask import Blueprint, send_file
from flask import request

from services.userManagement.registerUser import registerUser
from services.userManagement.validateUser import validateUser

userManagementRoutesBP = Blueprint('userManagementRoutesBP', __name__)


@userManagementRoutesBP.route("/user/register", methods=['POST'])
def registerUserRoute():
    data = request.get_json()
    response = registerUser(data)
    print(data)
    return response


@userManagementRoutesBP.route("/user/validate", methods=['POST'])
def validateUserRoute():
    data = request.get_json()
    response = validateUser(data)
    return response

