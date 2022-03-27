import zmq
import cv2
import base64

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.36.69:5555")
color_img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
color = cv2.imencode('.jpg', color_img)
a = base64.b64encode(color[1]).decode('utf-8').encode('utf-8')

#  Do 10 requests, waiting each time for a response
socket.send(a)

    #  Get the reply.
