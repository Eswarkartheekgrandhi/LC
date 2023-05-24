from flask import Blueprint
from flask import request

from services.annotations.storeAnnotationsToImage import setAnnotations

annotationRoutesBP = Blueprint('annotationRoutesBP', __name__)


@annotationRoutesBP.route("/setAnnotations", methods=['POST'])
def setAnnotationRoutes():
    data = request.get_json()
    annotations = data['annotations'],
    imageID = data["imageID"]
    setAnnotations(imageID,annotations)
    return "Image Annotations Set Successfully"


