import zmq
import cv2
import base64

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

cap = cv2.VideoCapture(0)

# cap.set(3, 1280)  # set width
# cap.set(4, 720)  # set Height
while True:
    try:
        color_img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
        ret, frames = cap.read()

        color = cv2.imencode('.jpg', color_img)
        a = base64.b64encode(color[1]).decode('utf-8').encode('utf-8')

        #  Do 10 requests, waiting each time for a response
        socket.send(a)

    except KeyboardInterrupt:
        cap.release()
        cv2.destroyWindow()
        print("client close")
        break
    #  Get the reply.
