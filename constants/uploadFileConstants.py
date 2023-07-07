DATA_DIRECTORY = {
    "trainImage": "./Data/Train Data/{}/Image",
    "trainAnnotation": "./Data/Train Data/{}/Annotations",
    "dataYamlFile": "./Data/Train Data/{}",
    "detectionData": "./Data/Detection Data/{}",
    "trainModel": "./Data/Model Training/{}/train"
}

INITIAL_UPLOAD_COUNTER = {
    'trainDataUpload': 10000,
    'detectionDataUpload': 20000,
    "trainModelRequest": 30000,
    'ruleID': 40000
}

STATUS_FILE_UPLOADED = "File Uploaded"

STATUS_IMAGE_UNANNOTATED = "Unannotated"
STATUS_IMAGE_ANNOTATED = "Annotated"
STATUS_IMAGE_PARTIALLY_ANNOTATED = "Annotated"

IMAGE_FILE_EXTN = {
    'png': 'PNG',
    'PNG': 'PNG',
    'jpg': 'jpg',
    'JPG': 'jpg',
    'JPEG': 'JPEG',
    'jpeg': 'JPEG'
}
