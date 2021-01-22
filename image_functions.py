import cv2
import distance_functions


def hello_world():
    print("Hello, world! (image_functions)")


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


def get_person_base_pixel_location():
    # from 1-100 ideally
    # 50 is middle of camera
    return 50


def start_human_detection(height, angle, fov):
    print("[+] Human detection started")

    # some loop to yoink and analize frames
    print("[+] Simulated human found")
    vert_position = get_person_base_pixel_location()
    distance = distance_functions.find_distance(height, angle, fov, vert_position)
    # [TODO] now compare this data against other humans with some function

    print("[+] Human distance found:", distance)

    print("[+] Continue simulation...")
