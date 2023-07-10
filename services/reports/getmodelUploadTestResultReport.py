import io
import os

import pandas as pd
import xlsxwriter

from constants.uploadFileConstants import DATA_DIRECTORY
from constants.mongoConstants import COLLECTION_FILE_UPLOAD_REQUEST_DETAILS, DB_VISUAL_INSPECTION
from repository.mongoRepository import getData


def getReport(testUploadID):
    detailedReportDataDF, quickReportDataDF = getResultData(testUploadID)
    excelFile = makeExcelFile(detailedReportDataDF, quickReportDataDF, testUploadID)
    return excelFile


def getResultData(testUploadID):
    identifier = {
        'requestID': testUploadID
    }
    collectionName = COLLECTION_FILE_UPLOAD_REQUEST_DETAILS
    detectionDF = pd.DataFrame(getData(identifier, collectionName, DB_VISUAL_INSPECTION))
    detailedReportDataDF = pd.DataFrame(detectionDF.loc[0, 'Detailed Report'])
    quickReportDataDF = pd.DataFrame(detectionDF.loc[0, 'Quick Report'])
    return detailedReportDataDF, quickReportDataDF


def makeExcelFile(detailedReportDataDF, quickReportDataDF, testUploadID):
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        quickReportDataDF.to_excel(writer, sheet_name="Quick Report", index=False, engine=xlsxwriter)
        # detailedReportDataDF.to_excel(writer, sheet_name="Detailed Report", index=False, engine=xlsxwriter)

        worksheetQuickReport = writer.sheets['Quick Report']
        border_format = writer.book.add_format({
            'border': 1,
            'align': 'left',
            'font_size': 10
        })
        cellFormat = writer.book.add_format({
            'align': 'left',
            'font_size': 10
        })
        cellFormat.set_text_wrap()
        worksheetQuickReport.set_column("A:C", width=25)
        worksheetQuickReport.set_column("B:B", width=100, cell_format=cellFormat)
        worksheetQuickReport.set_column("F:G", width=25)

        worksheetQuickReport.conditional_format('A1:D12', {'type': 'no_blanks', 'format': border_format})

        imageNameList = quickReportDataDF['Image Name'].unique()
        linkCounter = 2
        for imageName in imageNameList:
            rowCounter = 3
            sheetName = imageName
            tempDF = detailedReportDataDF[detailedReportDataDF['Image Name'] == imageName].reset_index()
            del (tempDF['index'])
            tempDfCount = tempDF.groupby(['Defect Detected'], as_index=False).count()
            tempDfCount = tempDfCount.rename(columns={"Image Name": "Count"})
            del (tempDfCount["Confidence"])

            print(tempDfCount)
            tempDF.to_excel(writer, sheet_name=sheetName, index=False, engine=xlsxwriter, startrow=rowCounter)
            tempDfCount.to_excel(writer, sheet_name=sheetName, index=False, engine=xlsxwriter, startrow=rowCounter,
                                 startcol= 5)
            rowCounter = rowCounter + len(tempDF) + 4
            worksheetDetailedReport = writer.sheets[sheetName]

            worksheetDetailedReport.insert_image("A{}".format(str(rowCounter+20)),
                                                 DATA_DIRECTORY['detectionData'].format(testUploadID) + "/Results/{}".format(imageName),
                                                 {'x_scale': 0.4, 'y_scale': 0.4})

            worksheetDetailedReport.set_column("A:C", width=25)
            worksheetDetailedReport.set_column("F:G", width=25)
            chart = writer.book.add_chart({'type' : 'pie'})
            chart.add_series({'values' : "'${}'$F${}:$G${}".format(sheetName, str(4), str(6+len(tempDfCount)))})
            chart.add_series({
                'name': 'Detection Count',
                'categories': "'{}'!$F${}:$F${}".format(sheetName, str(5), str(4+len(tempDfCount))),
                'values': "'{}'!$G${}:$G${}".format(sheetName, str(5), str(4+len(tempDfCount)))
            })
            chart.set_title({'name': 'Detection Count Pie Chart'})

            worksheetDetailedReport.insert_chart('C{}'.format(str(rowCounter)), chart, {'x_offset': 25, 'y_offset': 10})
            worksheetDetailedReport.conditional_format('A1:J100', {'type': 'no_blanks', 'format': border_format})
            worksheetDetailedReport.write_url("A1", url="internal:'Quick Report'!A1", string="Go back to Quick Report")
            worksheetQuickReport.write_url("C{}".format(str(linkCounter)), url="internal:'{}'!A1".format(sheetName),
                                           string="Go to Detailed Report")

            linkCounter = linkCounter + 1

    return buffer
