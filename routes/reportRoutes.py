from flask import Blueprint, send_file
from flask import request
from services.reports.getmodelUploadTestResultReport import getResultData, getReport

reportRoutesBP = Blueprint('reportRoutesBP', __name__)


@reportRoutesBP.route("/reports/getTestingResults", methods=['POST'])
def getTestingResultsRoute():
    testUploadID = request.form.get("testUploadID")
    excelReport = getReport(testUploadID)
    excelReport.seek(0)
    return send_file(excelReport, download_name='Model Test Report.xlsx')

