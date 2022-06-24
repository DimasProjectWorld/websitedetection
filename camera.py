import cv2

with open('obj.names', 'r') as f:
        classes = f.read().splitlines()

net = cv2.dnn.readNetFromDarknet("yolo-voc.2.0.cfg", "yolo-voc_last.weights")                
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)

labels={0:'Helmet',1:'Vest',2:'No Helmet',3:'No Vest'}
color={0:(0,255,0),1:(0,255,0),2:(0,0,255),3:(0,0,255)}

class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame=self.video.read()
        classIds, scores, boxes = model.detect(frame, confThreshold=0.6, nmsThreshold=0.4)
        
        for (classId, score, box) in zip(classIds, scores, boxes):
            cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),color[classId], thickness=2)
            text = classes[classId]
            cv2.putText(frame, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color[classId], thickness=2)

        ret, jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()