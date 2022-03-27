import zmq
import cv2
import base64
import numpy as np

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    try:
        message = socket.recv()
        message2 = message.decode('utf-8')
        img = base64.b64decode(message2)
        color2 = np.asarray(bytearray(img), dtype="uint8")
        testImage = cv2.imdecode(color2, 1)
        #  Do some 'work'
        cv2.imshow('test', testImage)
        cv2.waitKey()
    except KeyboardInterrupt:
        cv2.destroyAllWindow()
        print("Server close")
        break
    #  Send reply back to client