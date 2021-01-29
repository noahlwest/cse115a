import cv2
import numpy as np
import distance_functions


def hello_world():
    print("Hello, world! (image_functions)")


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

def set_cap_height_and_width(cap, height, width):
    #3 == width, 4 == height
    HEIGHT_CONSTANT = 3
    WIDTH_CONSTANT = 4
    cap.set(HEIGHT_CONSTANT, height)
    cap.set(WIDTH_CONSTANT, width)

def resize_frame(frame, width, height):
    cv2.resize(frame, (width, height))

def display_boxes(boxes, frame):
    for (xA, yA, xB, yB) in boxes:
        point_one = (xA, yA)
        point_two = (xB, yB)
        color = (0, 255, 0)
        line_width = 2
        cv2.rectangle(frame, point_one, point_two, color, line_width)

def detect_people(frame):
   # Create a list of boxes, one for each person detected
   locations_list = []

   ## some loop to yoink and analize frames
   #print("[+] Simulated human found")
   #vert_position = get_person_base_pixel_location()
   #distance = distance_functions.find_distance(height, angle, fov, vert_position)
   ## [TODO] now compare this data against other humans with some function
   #
   #print("[+] Human distance found:", distance)
   #
   ##print("[+] Continue simulation...")
   #print("[+] Ending detection...")
    
   return locations_list

def get_people_base_pixel_location(boxes):
    locations_list = []
    #for box in boxes:
    #   location = get_person_base_pixel_location(box)
    #   locations_list.append(location)
    #return locations_list
    pass


def get_person_base_pixel_location():
    # from 1-100 ideally
    # 50 is middle of camera
    return 50


def display_number_of_people(num_people, frame):
    text = "Number of people detected = " + str(num_people)
    font       = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeft = (10, frame.shape[0])
    fontScale  = 1
    fontColor  = (255, 255, 255)
    lineType   = 2
    cv2.putText(frame, text, bottomLeft, font, fontScale, fontColor, lineType)

def start_human_detection_loop(height, angle, fov):
    print("[+] Human detection started")
    model, classes, colors, output_layers = load_yolo()
    cap = start_videocapture("webcam", "none")
    boxes_around_people = []

    while(True):
        ret, frame = cap.read()
        
        boxes_around_people = detect_people(frame)
        display_boxes(boxes_around_people, frame)
        vert_positions = get_people_base_pixel_location(boxes_around_people)
        distances, lines = distance_functions.find_distances_between_positions(vert_positions)
        numBoxes = len(boxes_around_people)
        #(function this)
        #for index, distance in enumerate(distances):
        #   if distance < 6ft
        #       display_line_and_distance(lines[index], distance)
        
        #print("Number of boxes: ", numBoxes)

        height, width, channels = frame.shape
        blob, outputs = detect_objects(frame, model, output_layers)
        boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
        draw_labels(boxes, confs, colors, class_ids, classes, frame)

        key = cv2.waitKey(1)
        if key == 27:
        	break
	
    cap.release()

    print("[+] Ending detection...")

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