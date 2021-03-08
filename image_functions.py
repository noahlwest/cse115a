import cv2
import numpy as np
import distance_functions
import os
import wget
import time

HEIGHT_CONSTANT = 3
WIDTH_CONSTANT = 4

DISTANCE_VIOLATION = 6

PIXEL_WIDTH = 1280
PIXEL_HEIGHT = 720

COLOR_GREEN = (0, 255, 0)
COLOR_RED = (0, 0, 255)
VIOLATION_WAIT = 6

SECONDS_VIOLATION = 10
ALERT_TIMER = 10

# Input:       none
# Output:      string local time
# Description: gets, formats, and returns the local time
def get_time():
    return time.localtime(time.time())

# Input:       a date object from the time module
# Output:      a string version of the date
# Description: stringifies the date into the format (year-month-day-minute-second)
def format_date_time(date):
    year = date.tm_year
    month = date.tm_mon
    return str(date.tm_year) + "-" + str(date.tm_mon) + "-" + str(date.tm_mday) + "-" \
           + str(date.tm_min) + "-" + str(date.tm_sec)

# For the next two functions
# Input:       none
# Output:      none
# Description: opencv setup and end
def init_opencv():
    cv2.startWindowThread()

def stop_opencv():
    cv2.destroyAllWindows()
    cv2.waitKey(1)

# Input:       source, video file name
# Output:      cap
# Description: creates a video capture object that allows for reading from a source. Currently supported video types are webcams and video files. If source is video file, the video capture object reads from the video file
def start_videocapture(source, location):
    print("[+] Getting Video feed")
    mywidth = 0
    myheight = 0
    if source == "webcam":
        cap = cv2.VideoCapture(0)  # starts on default webcam
        print("[+] Webcam set-up")
        mywidth = PIXEL_WIDTH
        myheight = PIXEL_HEIGHT
    elif source == "video_file":
        cap = cv2.VideoCapture(location)
        print("[+] Video File set-up")
        mywidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        myheight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    else:
        # no input:
        print("Invalid starting configuration. Exiting.")
        exit(1)
    set_cap_height_and_width(cap, mywidth, myheight)
    return cap, mywidth, myheight
    # TODO: add video stream as possible source

# Input:       cap, height, width
# Output:      none
# Description: sets up the capture height and width
def set_cap_height_and_width(cap, height, width):
    cap.set(HEIGHT_CONSTANT, height)
    cap.set(WIDTH_CONSTANT, width)

# Input:       frame, width, height
# Output:      none
# Description: resizes the frame to the new width and height
def resize_frame(frame, width, height):
    cv2.resize(frame, (width, height))

# Input:       number of people, frame
# Output:      none
# Description: prints the number of people onto the frame
def display_number_of_people(num_people, frame):
    text = "Number of people detected = " + str(num_people)
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeft = (10, frame.shape[0])
    fontScale = 1
    fontColor = (255, 255, 255)
    lineType = 2
    cv2.putText(frame, text, bottomLeft, font, fontScale, fontColor, lineType)

# Input:       directory name
# Output:      none
# Description: creates a directory with the name provided
def create_dir(dirname):
    try:
        os.mkdir(dirname)
    except OSError as error:
        pass

# Input:       violation bool, audio alert bool, screenshot bool, screenshot directory,
#              frame, output video writer, current time,
#              screenshot filename, video writer fourcc (data)
#              time_of_last_alert, video capture width, video capture height
# Output:      output video writer, screenshot number
# Description: if there is a violation, optionally play an alert based on audio alert, optionally save the frame to a video,
#              creating a new video writer to a new file as needed.
#              If there are no violations, end the video writer and reset the last time an alert was played.
def too_close_handler(violation, audioAlert, screenShots, frame, vidout, vidtime,
                      filename, fourcc, time_of_last_alert, capwidth, capheight):
    if violation == True:
       if audioAlert == True and (time.time() - time_of_last_alert >= ALERT_TIMER):
           print('\a')
           time_of_last_alert = time.time()
           # implement some more advanced stuff?
       if screenShots == True:
          videoname = filename + format_date_time(vidtime) + ".mp4"
          if vidout == None:
             vidout = cv2.VideoWriter(videoname, fourcc, 20.0, (int(capwidth), int(capheight)))
          if vidout != None:
             vidout.write(frame)
    else:
        if vidout != None:
           vidout.release()
           vidout = None
           time_of_last_alert = 0
    return vidout, time_of_last_alert

# Input:       screenshot directory name        
# Output:      the first part of the video output name, video writer fourcc (data)
# Description: generates the part of the output name that is standard to all output videos
#              and video output data specifically for mp4 videos
def setup_vidout(screenShotsDir):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    filename = 'output'
    if (screenShotsDir == ''):
        finalpath = filename
    else:
        finalpath = screenShotsDir + '/' + filename
        create_dir(screenShotsDir)
    return finalpath, fourcc

# Input:       height of camera, angle of camera (0 degrees = points at floor), horizontal field of view,
#              vertical field of view, boolean for reading from webcam (true = read from webcam, false = read from file,
#              boolean for playing a notification, boolean for saving violations to output videos, path to output video
#              directory, path to input video file
# Output:      none
# Description: glues together all of the setup and the processing, releasing and breaking down objects as needed
def start_human_detection_loop(height, angle, fov_h, fov_v, webCheck, audioAlert, screenShots, screenshot_path, video_path):
    #TODO: add usage for fov_h, fov_v, webCheck, audioAlert, screenShots
    if screenshot_path == "":
       screenShotsDir = os.getcwd()
       screenShotsDir += "/screenshots"
    else:
       screenShotsDir = screenshot_path
    print("screenShotsDir = " + screenShotsDir)
    print("[+] Human detection started")
    model, classes, colors, output_layers = load_yolo()
    source = "video_file"
    if webCheck:
       source = "webcam"
    cap, capwidth, capheight = start_videocapture(source, video_path)
    # setup screenshot stuff to save a video
    filename, fourcc = setup_vidout(screenShotsDir)
    vidout = None
    vidnumber = 0
    violCounter = 0

    last_violation_time = 0
    time_of_last_alert = 0
    while (True):
        ret, frame = cap.read()

        height_window, width, channels = frame.shape
        blob, outputs = detect_objects(frame, model, output_layers)
        boxes, confs, class_ids = get_box_dimensions(outputs, height_window, width)

        update_notify = draw_all_lines(boxes, confs, colors, class_ids, classes, frame, height, angle, fov_v, fov_h)
        # cooldown - notify_bool will tell the program to continue taking video or not.
        if update_notify:
            last_violation_time = time.time()
        notify_bool = (update_notify or time.time() - last_violation_time < SECONDS_VIOLATION)

        print_on_feet(boxes, confs, colors, class_ids, frame, height, angle, fov_v)
        if webCheck:
           draw_text(frame, time.asctime(get_time()), 0, 25, COLOR_GREEN)
        vidnumber = get_time()
        draw_labels(boxes, confs, colors, class_ids, classes, frame)
        vidout, time_of_last_alert = too_close_handler(notify_bool, audioAlert, screenShots,
                                                frame, vidout,
                                                vidnumber, filename, fourcc, time_of_last_alert, capwidth, capheight)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    if vidout != None:
       vidout.release()
    print("[+] Ending detection...")

# Input:       none
# Output:      net, classes, colors, output_layers ****NEEDS AN EXPLANATION OF WHAT THESE ARE****
# Description: loads up the yolo algorithm/software and returns relevant yolo data
def load_yolo():
    yolov3_weights = ""
    yolov3_cfg = ""
    try:

        yolov3_weights = os.getcwd()
        yolov3_weights += "\\yolov3.weights"

        yolov3_cfg = os.getcwd()
        yolov3_cfg += "\\yolov3.cfg"

        if not os.path.exists(yolov3_weights):
            #print(f"file path to {yolov3_weights} not found")
            print("yolov3_weights file not found")
            print("Attempting to download yolov3.weights (250MB)...")

            # url = "https://pjreddie.com/media/files/yolov3.weights" #official source
            url = "https://www.dropbox.com/s/xb3n2zycopf4zte/yolov3.weights?dl=1"  # our own dropbox link
            wget.download(url)
            print("\nSuccesfully downloaded yolov3.weights")

        if not os.path.exists(yolov3_cfg):
            #print(f"file path to {yolov3_cfg} not found")
            print("yolov3_cfg file not found")
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

# Input:       a blob
# Output:      none
# Description: ??? ****NEEDS A DESCRIPTION****
def display_blob(blob):
    '''
            Three images each for RED, GREEN, BLUE channel
    '''
    for b in blob:
        for n, imgb in enumerate(b):
            cv2.imshow(str(n), imgb)

# Input:       frame
# Output:      a blob, outputs ****NEEDS A BRIEF DESCRIPTION OF outputs****
# Description: ??? ****NEEDS A DESCRIPTION****
def detect_objects(frame, net, outputLayers):
    blob = cv2.dnn.blobFromImage(frame, scalefactor=0.00392, size=(
        320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(outputLayers)
    return blob, outputs

# Input:       outputs, height, width ****NEEDS A BRIEF DESCRIPTION OF outputs****
# Output:      boxes, confs, class_ids ****NEEDS AN EXPLANATION OF WHAT THESE ARE****
# Description: ??? ****NEEDS A DESCRIPTION****
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

# Input:       boxes, confs, colors, class_ids, img, height of camera, angle of camera, vertical field of view
# ****NEEDS AN EXPLANATION FOR confs, colors, class_ids****
# Output:      none
# Description: if a box (i.e., an object) is detected as a person, print text on the right under the feet
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
                #print("Distance: ", distance_functions.find_distance(height, angle, fov_v, y1 / PIXEL_HEIGHT))

# Input:       a list of boxes, confs, a list of colors, class_ids, classes, an image img, height of camera, angle of camera, vertical field of view
# ****NEEDS AN EXPLANATION FOR confs, colors, class_ids, classes****
# Output:      boolean for if there is a violation
# Description: ??? ****NEEDS A DESCRIPTION****
def draw_all_lines(boxes, confs, colors, class_ids, classes, img, height, angle, fov_v, fov_h):
    # get "unique" boxes
    if_violation = False
    #print("[+] Drawing lines")
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

            (x1, y1) = new_feet[i]
            (x2, y2) = new_feet[j]
            dist1 = distance_functions.find_distance(height, angle, fov_v, y1 / PIXEL_HEIGHT)
            dist2 = distance_functions.find_distance(height, angle, fov_v, y2 / PIXEL_HEIGHT)
            dist = distance_functions.return_distance(new_feet[i], new_feet[j], fov_v, fov_h, angle, dist1, dist2)
            if dist < DISTANCE_VIOLATION:
                if_violation = True
            draw_text(img, str(round(dist, 2)), int((abs(x1 + x2) / 2)), int((abs(y1 + y2) / 2)), colors[1])
            draw_line(img, x1, y1, x2, y2, colors[1])

    return if_violation

# Input:       a list of boxes, confs, a list of colors, class_ids, classes, an image
# ****NEEDS AN EXPLANATION FOR confs, class_ids, classes****
# Output:      the number of people detected
# Description: draws each box around each detected person, displaying the distance the person is from the camera and counting each one, returning the counter
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

# Input:       frame, start x, start y, end x, end y, a color
# Output:      none
# Description: draws a line from the start x, y to the end x, y with the given color
def draw_line(frame, xA, yA, xB, yB, color):
    point_one = (xA, yA)
    point_two = (xB, yB)
    cv2.line(frame, point_one, point_two, color, thickness=2)

# Input:       frame, text, bottom left x, bottom left y, color
# Output:      none
# Description: displays some text with at the provided coordinates as the bottom left corner with the provided color
def draw_text(frame, text, x_coord, y_coord, color):
    point = (x_coord, y_coord)
    cv2.putText(frame, text, point, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

# Input:       a distance, frame, bottom left coordinate
# Output:      none
# Description: displays a distance with the provided coordinates as the bottom left corner
def dist_on_foot(dis, frame, coord):
    text = str(round(dis, 2))
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeft = coord
    fontScale = 1
    fontColor = (255, 255, 255)
    lineType = 2
    cv2.putText(frame, text, bottomLeft, font, fontScale, fontColor, lineType)

# Input:       a list of boxes representing people
# Output:      a list of feet positions
# Description: gets the feet positions of all boxes
def get_feet_pos(boxes):
    feet_pos = []
    for (left, top, right, bottom) in boxes:
        feet_pos.append((int((2 * left + right) / 2), int(bottom + top)))
    return feet_pos
