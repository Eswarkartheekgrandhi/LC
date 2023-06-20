from datetime import datetime

from constants.mongoConstants import COLLECTION_MODEL_LIST, DB_VISUAL_INSPECTION
from repository.mongoRepository import insertData


def insertModelDetailsToMongo():
    labels = ['Cap1', 'Cap2', 'Cap3', 'Cap4', 'MOSFET', 'Mov', 'Resestor', 'Resistor', 'Transformer']
    data = {
        "modelID": "MODEL_1",
        "modelName": "PCB Component Detection Model",
        "modelDescription": "This model is trained on https://www.kaggle.com/datasets/animeshkumarnayak/pcb-fault"
                            "-detection. This model can be used to detect multiple compnent in a PCB",
        "modelCreationTime": datetime.now(),
        "labels": labels,
        "totalLabels": len(labels)
    }
    insertData(data, COLLECTION_MODEL_LIST, DB_VISUAL_INSPECTION)
    labels = ['Missing Hole', 'Mouse Bite', 'Open Circuit', 'Short', 'Spur', 'Spurious Copper']
    data = {
        "modelID": "MODEL_2",
        "modelName": "PCB Defect Detection Model",
        "modelDescription": "This model is trained on https://www.kaggle.com/datasets/akhatova/pcb-defects. This "
                            "model can be used to detect multiple defects in a PCB",
        "modelCreationTime": datetime.now(),
        "labels": labels,
        "totalLabels": len(labels)
    }
    insertData(data, COLLECTION_MODEL_LIST, DB_VISUAL_INSPECTION)


