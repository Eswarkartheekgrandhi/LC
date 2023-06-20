import pandas as pd
import cv2

from constants.mongoConstants import DB_VISUAL_INSPECTION, \
    COLLECTION_IMAGE_RECORDS
from repository.mongoRepository import getData


def getAnnotationData():
    data = getData({'requestID': '10016', "annotationStatus": "Annotated"}, COLLECTION_IMAGE_RECORDS,
                   DB_VISUAL_INSPECTION)
    dataDF = pd.DataFrame(data)
    for i in range(len(dataDF)):
        annotationsList = dataDF.loc[i, "annotations"]
        imageDirectory = dataDF.loc[i, "destination"]
        img = cv2.imread(imageDirectory, 0)
        image_height, image_width = img.shape[:2]
        print(image_height, image_width)
        print(imageDirectory)
        annotationDF = pd.DataFrame(annotationsList[0][0])
        # print(annotationDF)
        for j in range(len(annotationDF)):
            label = annotationDF.loc[j, "comment"]

            mark = annotationDF.loc[j, 'mark']
            x = mark['x']
            y = mark['y']
            width = mark['width']
            height = mark['height']

            bbox_x_center = x + (width / 2)
            bbox_y_center = y + (height / 2)

            normalized_x = bbox_x_center / image_width
            normalized_y = bbox_y_center / image_height

            normalized_width = width / image_width
            normalized_height = height / image_height

            print(normalized_x, normalized_y, normalized_height, normalized_width)


getAnnotationData()
