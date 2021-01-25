import cv2
import distance_functions


def hello_world():
    print("Hello, world! (image_functions)")


def init_opencv():
    cv2.startWindowThread()

def stop_opencv(cap):
    cap.release()
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
    return
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


def get_person_base_pixel_location():
    # from 1-100 ideally
    # 50 is middle of camera
    return 50


def start_human_detection_loop(height, angle, fov, cap):
    print("[+] Human detection started")
    boxes_around_people = []
    while(True):
        ret, frame = cap.read()
        numBoxes = len(boxes_around_people)
        if ret:
            boxes_around_people = detect_people(frame)
            display_boxes(boxes_around_people, frame)
            vert_positions = get_people_base_pixel_location(boxes_around_people)
            distances, lines = distance_functions.find_distances_between_positions(vert_positions)
            #(function this)
            #for index, distance in enumerate(distances):
            #   if distance < 6ft
            #       display_line_and_distance(lines[index], distance)

            #show the output, wait for 'esc' press
            text = "Number of people detected = " + str(numBoxes)
            font       = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeft = (10, frame.shape[0])
            fontScale  = 1
            fontColor  = (255,255,255)
            lineType   = 2
            cv2.putText(frame, text, bottomLeft, font, fontScale, fontColor, lineType)
            cv2.imshow('press esc to exit', frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
        print("Number of boxes: ", numBoxes)
