import math


def hello_world():
    print("Hello, world! (distance_functions)")


def adjust_angle(angle, fov, vertical_position):
    bottom_angle = angle - (fov / 2)
    final_angle = bottom_angle + ((vertical_position/100) * fov)
    #any angle > 90 is an error or false detection
    return final_angle


def adjust_angle_horz(fov, horz):

    final_angle = ((horz/1280) * fov)
    #any angle > 90 is an error or false detection
    return final_angle

def adjust_angle_vert(angle, fov, vertical_position):
    bottom_angle = angle - (fov / 2)
    final_angle = bottom_angle + ((vertical_position/720) * fov)
    #any angle > 90 is an error or false detection
    return final_angle


def find_distance(height, angle, fov, vertical_position_of_persons_feet):
    print("height:", height)
    print("angle:", angle)
    print("fov:", fov)
    print("vertical_position_of_persons_feet:", 100 - vertical_position_of_persons_feet * 100)
    final_angle = adjust_angle(angle, fov, 100 - vertical_position_of_persons_feet * 100)
    print("final_angle:", final_angle)
    final_angle = math.radians(final_angle)
    distance = height * (1 / math.cos(final_angle))
    return distance


def distance_between_points(a_radial_dis, a_polar_ang, a_azimuthal_ang, b_radial_dis, b_polar_ang, b_azimuthal_ang):
    # Degrees to radians - required for math trig functions
    a_azimuthal_ang = math.radians(a_azimuthal_ang)
    a_polar_ang = math.radians(a_polar_ang)
    b_azimuthal_ang = math.radians(b_azimuthal_ang)
    b_polar_ang = math.radians(b_polar_ang)

    sin_shit = (math.sin(a_polar_ang) * math.sin(b_polar_ang) * math.cos(a_azimuthal_ang - b_azimuthal_ang) +
                math.cos(a_polar_ang) * math.cos(b_polar_ang))
    final = math.sqrt(a_radial_dis ** 2 + b_radial_dis ** 2 - (2 * a_radial_dis * b_radial_dis * sin_shit))

    return final


def return_distance(xy_tuple1, xy_tuple2, v_fov, h_fov, angle, dist1, dist2):

    x1, y1 = xy_tuple1
    x2, y2 = xy_tuple2
    x1 = adjust_angle_horz(h_fov, x1)
    x2 = adjust_angle_horz(h_fov, x2)
    y1 = adjust_angle_vert(angle, v_fov, y1)
    y2 = adjust_angle_vert(angle, v_fov, y2)

    print(dist1, y1, x1, dist2, y2, x2)

    return distance_between_points(dist1, y1, x1, dist2, y2, x2)