import requests
import base64
import json
import cv2
# Sample image file is available at http://plates.openalpr.com/ea7the.jpg
def identifyPlate():
  
    IMAGE_PATH = 'img4.jpg'
    SECRET_KEY = 'sk_eecd4b9957b2775cf16309e4'
    with open(IMAGE_PATH, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())

    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=eu&secret_key=%s' % (SECRET_KEY)

    r = requests.post(url, data = img_base64)

    result=json.dumps(r.json(), indent=2)
    resp = json.loads(result)
    resp2=resp['results'][0]['plate']
    return resp2

