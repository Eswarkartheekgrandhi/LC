from flask import Blueprint
from flask import request

from services.authentication.tokenRequiredDecorator import tokenRequired
from services.rulesManagement.createRules import createRules
from services.rulesManagement.getRules import getRulesFromMongoDB

ruleManagementRoutesBP = Blueprint('ruleManagementRoutesBP', __name__)


@ruleManagementRoutesBP.route("/createRuleRequest", methods=['POST'])
@tokenRequired
def createRulesRoute(user):
    data = request.get_json()
    createRules(data, user)
    return "Rule has been Created"


@ruleManagementRoutesBP.route("/getRules", methods=['POST'])
@tokenRequired
def getRules(user):
    print(user)
    rules = getRulesFromMongoDB(user)
    return {"data": rules}
