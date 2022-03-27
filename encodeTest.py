import cv2
import base64
import numpy as np

color_img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
color = cv2.imencode('.jpg', color_img)
a = base64.b64encode(color[1]).decode('utf-8').encode('utf-8')

message2 = a.decode('utf-8')
img = base64.b64decode(message2)
color2 = np.asarray(bytearray(img), dtype="uint8")
testImage = cv2.imdecode(color2, 1)
    #  Do some 'work'
cv2.imshow('test', testImage)
cv2.waitKey()
cv2.destroyWindow()