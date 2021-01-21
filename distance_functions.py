import math


def adjust_angle(angle, fov, vertical_position):
    bottom_angle = angle - (fov / 2)
    final_angle = bottom_angle + ((vertical_position/100) * fov)
    #any angle > 90 is an error or false detection
    return final_angle


def find_distance(height, angle, fov, vertical_position_of_persons_feet):
    print("height:", height)
    print("angle:", angle)
    print("fov:", fov)
    print("vertical_position_of_persons_feet:", vertical_position_of_persons_feet)
    final_angle = adjust_angle(angle, fov, vertical_position_of_persons_feet)
    print("final_angle:", final_angle)
    distance = height * (1 / math.cos(final_angle))
    return distance
