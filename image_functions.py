import cv2
import numpy as np
import distance_functions
import time

def hello_world():
    print("Hello, world! (image_functions)")

# opencv setup and end
def init_opencv():
    cv2.startWindowThread()

def stop_opencv():
    cv2.destroyAllWindows()
    cv2.waitKey(1)

def start_videocapture(source, location):
    if source == "webcam":
        cap = cv2.VideoCapture(0) #starts on default webcam
        set_cap_height_and_width(cap, 1280, 720)
        return cap
    if source == "video_file":
        cap = cv2.VideoCapture(location)
        set_cap_height_and_width(cap, 1280, 720)
        return cap
    #TODO: add video stream as possible source

    #no input:
    print("Invalid starting configuration. Exiting.")
    exit(1)

# Takes the result from GUI user decision on input source.
# Defaults to 0 for default webcam as input.
def get_videocapture_arg():
    return 0

# setup window info
def set_cap_height_and_width(cap, height, width):
    #3 == width, 4 == height
    HEIGHT_CONSTANT = 3
    WIDTH_CONSTANT = 4
    cap.set(HEIGHT_CONSTANT, height)
    cap.set(WIDTH_CONSTANT, width)

def resize_frame(frame, width, height):
    cv2.resize(frame, (width, height))

# gives calling function a list of head positions based on
# a provided list of boxes, assuming each box in the list
# is a person
def get_head_pos(boxes):
   head_pos = []
   for (left, top, right, bottom) in boxes:
      head_pos.append(((left+right)/2, top))
   return head_pos

# gives calling function a list of feet positions based on
# a provided list of boxes, assuming each box in the list
# is a person
def get_feet_pos(boxes):
   feet_pos = []
   for (left, top, right, bottom) in boxes:
      feet_pos.append(((left+right)/2, bottom))
   return feet_pos

# displays the number of people in a frame
def display_number_of_people(num_people, frame):
    text = "Number of people detected = " + str(num_people)
    font       = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeft = (10, frame.shape[0])
    fontScale  = 1
    fontColor  = (255, 255, 255)
    lineType   = 2
    cv2.putText(frame, text, bottomLeft, font, fontScale, fontColor, lineType)

# main loop called by the main function in main.py
# opens the video capture, analyze it frame by frame,
# display boxes over people, and dtermines distance between
# people
def start_human_detection_loop(height, angle, fov):
    print("[+] Human detection started")
    model, classes, colors, output_layers = load_yolo()
    cap = start_videocapture("video_file", "newtest.mp4")
    boxes_around_people = []

    while(True):
        ret, frame = cap.read()
        
        #print("Number of boxes: ", numBoxes)
        height = frame.shape[0]
        width = frame.shape[1]
        channels = frame.shape[2]
        blob, outputs = detect_objects(frame, model, output_layers)
        boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
        draw_labels(boxes, confs, colors, class_ids, classes, frame)
        
        # creates lists of head and feet positions of all boxes
        head_pos = get_head_pos(boxes)
        feet_pos = get_feet_pos(boxes)
        key = cv2.waitKey(1)
        if key == 27:
        	break
	
    cap.release()

    print("[+] Ending detection...")

# load the yolo person detecting software/algorithm
def load_yolo():
	net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
	classes = []
	with open("coco.names", "r") as f:
		classes = [line.strip() for line in f.readlines()]

	layers_names = net.getLayerNames()
	output_layers = [layers_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
	colors = np.random.uniform(0, 255, size=(len(classes), 3))
	return net, classes, colors, output_layers

def display_blob(blob):
	'''
		Three images each for RED, GREEN, BLUE channel
	'''
	for b in blob:
		for n, imgb in enumerate(b):
			cv2.imshow(str(n), imgb)

def detect_objects(img, net, outputLayers):			
	blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
	net.setInput(blob)
	outputs = net.forward(outputLayers)
	return blob, outputs

# generates a list of boxes and what kind of object the box is
def get_box_dimensions(outputs, height, width):
	boxes = []
	confs = []
	class_ids = []
	for output in outputs:
		for detect in output:
			scores = detect[5:]
			class_id = np.argmax(scores)
			conf = scores[class_id]
			if conf > 0.3:
				center_x = int(detect[0] * width)
				center_y = int(detect[1] * height)
				w = int(detect[2] * width)
				h = int(detect[3] * height)
				x = int(center_x - w/2)
				y = int(center_y - h / 2)
				boxes.append([x, y, w, h])
				confs.append(float(conf))
				class_ids.append(class_id)
	return boxes, confs, class_ids

def draw_labels(boxes, confs, colors, class_ids, classes, img):
    #get "unique" boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    #try:
    #    x, y, w, h = boxes[0]
    #    label = str(classes[class_ids[0]])
    #    color = colors[0]
    #    cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
    #    cv2.putText(img, label, (x, y - 5), font, 1, color, 1)
    #except:
        #no detections
    #    pass

    counter = 0
    for i in range(len(boxes)):
        if i in indexes:
            if class_ids[i] == 0:
                counter += 1
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[i]
                cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
                cv2.putText(img, label, (x, y - 5), font, 1, color, 1)
    
    display_number_of_people(counter, img)
    cv2.imshow("Press 'esc' to exit", img)

    return counter
