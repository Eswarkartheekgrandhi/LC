from flask import Blueprint
from flask import request

from services.rules.createRules import createRules

ruleManagementRoutesBP = Blueprint('ruleManagementRoutesBP', __name__)


@ruleManagementRoutesBP.route("/createRuleRequest", methods=['POST'])
def setAnnotationRoutes():
    data = request.get_json()
    createRules(data)
    return "Rule has been Created"


