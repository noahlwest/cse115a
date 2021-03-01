import cv2
import numpy as np
import distance_functions
import os
import wget
import time

HEIGHT_CONSTANT = 3
WIDTH_CONSTANT = 4

PIXEL_WIDTH = 1280
PIXEL_HEIGHT = 720

COLOR_GREEN = (0, 255, 0)
COLOR_RED = (0, 0, 255)

SECONDS_VIOLATION = 10
DISTANCE_VIOLATION = 6

def hello_world():
    print("Hello, world! (image_functions)")


def init_opencv():
    cv2.startWindowThread()


def stop_opencv():
    cv2.destroyAllWindows()
    cv2.waitKey(1)


def start_videocapture(source, location):
    print("[+] Getting Video feed")
    if source == "webcam":
        cap = cv2.VideoCapture(0)  # starts on default webcam
        set_cap_height_and_width(cap, PIXEL_WIDTH, PIXEL_HEIGHT)
        print("[+] Webcam set-up")
        return cap
    if source == "video_file":
        cap = cv2.VideoCapture(location)
        set_cap_height_and_width(cap, PIXEL_WIDTH, PIXEL_HEIGHT)
        print("[+] Video File set-up")
        return cap
    # TODO: add video stream as possible source

    # no input:
    print("Invalid starting configuration. Exiting.")
    exit(1)


def set_cap_height_and_width(cap, height, width):
    cap.set(HEIGHT_CONSTANT, height)
    cap.set(WIDTH_CONSTANT, width)


def resize_frame(frame, width, height):
    cv2.resize(frame, (width, height))


def display_number_of_people(num_people, frame):
    text = "Number of people detected = " + str(num_people)
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeft = (10, frame.shape[0])
    fontScale = 1
    fontColor = (255, 255, 255)
    lineType = 2
    cv2.putText(frame, text, bottomLeft, font, fontScale, fontColor, lineType)


def create_dir(dirname):
    try:
        os.mkdir(dirname)
    except OSError as error:
        pass


def too_close_handler(violation, audioAlert, screenShots, screenShotsDir, frame, screenShotOut, screenShotNumber,
                      filename, fourcc):
    if violation:
        if audioAlert:
            print('\a')
            # no cool down means this has the possibility to beep every frame (24/30/60 times a second?) - probably
            # could do better implement some more advanced stuff?
        if screenShots:
            if screenShotOut is None:
                screenShotOut = cv2.VideoWriter(filename + str(screenShotNumber) + ".avi", fourcc, 20.0, (1280, 720))
            screenShotOut.write(frame)
    else:
        if screenShotOut is not None:
            screenShotOut.release()
            screenShotOut = None
            screenShotNumber += 1
    return screenShotOut, screenShotNumber


def setup_video(screenShotsDir):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    filename = 'output'
    if (screenShotsDir == ''):
        finalpath = filename
    else:
        finalpath = screenShotsDir + '/' + filename
        create_dir(screenShotsDir)
    return finalpath, fourcc


def getTime():
    return time.asctime(time.localtime(time.time()))


def start_human_detection_loop(height, angle, fov_h, fov_v, webCheck, audioAlert,
                               screenShots):  # ,screenShotsDir): #temp removed, because GUI doesn't have it yet.
    screenShotsDir = os.getcwd()
    screenShotsDir += "\\screenshots"
    print("[+] Human detection started")
    model, classes, colors, output_layers = load_yolo()
    cap = start_videocapture("webcam", "none")
    # setup screenshot stuff to save a video
    filename, fourcc = setup_video(screenShotsDir)
    screenShotOut = None
    # test code for too_close_handler to handle "sets" of violations
    last_violation_time = 0
    screenShotNumber = 0
    while True:
        ret, frame = cap.read()

        height_window, width, channels = frame.shape
        blob, outputs = detect_objects(frame, model, output_layers)
        boxes, confs, class_ids = get_box_dimensions(outputs, height_window, width)

        update_notify = draw_all_lines(boxes, confs, colors, class_ids, classes, frame, height, angle, fov_v, fov_h)

        if update_notify:
            last_violation_time = time.time()
        notify_bool = (update_notify or time.time() - last_violation_time < SECONDS_VIOLATION)

        print_on_feet(boxes, confs, colors, class_ids, frame, height, angle, fov_v)
        draw_text(frame, getTime(), 0, 25, COLOR_GREEN)
        draw_labels(boxes, confs, colors, class_ids, classes, frame)
        screenShotOut, screenShotNumber = too_close_handler(notify_bool, audioAlert, screenShots, screenShotsDir, frame,
                                                            screenShotOut, screenShotNumber, filename, fourcc)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    if screenShotOut != None:
        screenShotOut.release()
    print("[+] Ending detection...")


def load_yolo():
    yolov3_weights = ""
    yolov3_cfg = ""
    try:

        yolov3_weights = os.getcwd()
        yolov3_weights += "\\yolov3.weights"

        yolov3_cfg = os.getcwd()
        yolov3_cfg += "\\yolov3.cfg"

        if not os.path.exists(yolov3_weights):
            print(f"file path to {yolov3_weights} not found")
            print("Attempting to download yolov3.weights (250MB)...")

            # url = "https://pjreddie.com/media/files/yolov3.weights" #official source
            url = "https://www.dropbox.com/s/xb3n2zycopf4zte/yolov3.weights?dl=1"  # our own dropbox link
            wget.download(url)
            print("\nSuccesfully downloaded yolov3.weights")

        if not os.path.exists(yolov3_cfg):
            print(f"file path to {yolov3_cfg} not found")
            print("Attempting to download yolov3.cfg...")

            url = "https://raw.githubusercontent.com/noahlwest/cse115a/master/yolov3.cfg"  # our github
            wget.download(url)
            print("\nSuccesfully downloaded yolov3.cfg")

    except Exception as e:
        print(e)

    net = cv2.dnn.readNet(yolov3_weights, yolov3_cfg)

    try:
        result = cv2.cuda.getCudaEnabledDeviceCount()

        if result > 0:
            net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        # else:
        #     print("cuda not found")
    except Exception as error:
        print(error)

    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layers_names = net.getLayerNames()
    output_layers = [layers_names[i[0] - 1]
                     for i in net.getUnconnectedOutLayers()]
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
    blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(
        320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
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
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confs.append(float(conf))
                class_ids.append(class_id)
    return boxes, confs, class_ids


def print_on_feet(boxes, confs, colors, class_ids, img, height, angle, fov_v):
    indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
    feet = get_feet_pos(boxes)
    distances = []
    for i in range(len(boxes)):
        if i in indexes:
            if class_ids[i] == 0:
                x1, y1 = feet[i]
                x1 = int(x1)
                y1 = int(y1)
                dist_on_foot(distance_functions.find_distance(height, angle, fov_v, y1 / PIXEL_HEIGHT), img, (x1 - 20, y1))
                # print("Distance: ", distance_functions.find_distance(height, angle, fov_v, y1 / PIXEL_HEIGHT))


def draw_all_lines(boxes, confs, colors, class_ids, classes, img, height, angle, v_fov, h_fov):
    # get "unique" boxes
    if_violation = False
    un_flatten_index = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
    if isinstance(un_flatten_index, tuple):
        return
    indexes = np.ndarray.flatten(un_flatten_index)
    feet_pos = get_feet_pos(boxes)
    new_feet = []

    for i in indexes:
        if class_ids[i] == 0:
            new_feet.append(feet_pos[i])

    for i in range(len(new_feet)):
        for j in range(i + 1, len(new_feet)):

            if class_ids[i] != 0 or class_ids[j] != 0:
                continue

            (x1, y1) = new_feet[i]
            (x2, y2) = new_feet[j]
            dist1 = distance_functions.find_distance(height, angle, v_fov, y1 / PIXEL_HEIGHT)
            dist2 = distance_functions.find_distance(height, angle, v_fov, y2 / PIXEL_HEIGHT)
            dist = distance_functions.return_distance(new_feet[i], new_feet[j], v_fov, h_fov, angle, dist1, dist2)
            if dist < DISTANCE_VIOLATION:
                if_violation = True
                display_color = COLOR_RED
            else:
                display_color = COLOR_GREEN
            print("[+] Drawing lines")
            draw_text(img, str(round(dist, 2)), int((abs(x1 + x2) / 2)), int((abs(y1 + y2) / 2)), colors[0])
            draw_line(img, x1, y1, x2, y2, colors[0])

    return if_violation


def draw_labels(boxes, confs, colors, class_ids, classes, img):
    # get "unique" boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN

    counter = 0
    for i in range(len(boxes)):
        if i in indexes:
            if class_ids[i] == 0:
                counter += 1
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y - 5), font, 1, color, 1)
    display_number_of_people(counter, img)
    cv2.imshow("Press 'esc' to exit", img)

    return counter


def draw_line(frame, xA, yA, xB, yB, color):
    point_one = (xA, yA)
    point_two = (xB, yB)
    cv2.line(frame, point_one, point_two, color, thickness=2)


def draw_text(frame, text, x_coord, y_coord, color):
    point = (x_coord, y_coord)
    cv2.putText(frame, text, point, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)


def dist_on_foot(dis, frame, coord):
    text = str(round(dis, 2))
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeft = coord
    fontScale = 1
    fontColor = (255, 255, 255)
    lineType = 2
    cv2.putText(frame, text, bottomLeft, font, fontScale, fontColor, lineType)


def get_feet_pos(boxes):
    feet_pos = []
    for (left, top, right, bottom) in boxes:
        feet_pos.append((int((2 * left + right) / 2), int(bottom + top)))
    return feet_pos
