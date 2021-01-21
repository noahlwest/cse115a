import distance_functions

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
