# import the necessary packages
import numpy as np
import cv2
import math
 
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

# open webcam video stream
cap = cv2.VideoCapture(0)

# the output will be written to output.avi
out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resizing for faster detection
    frame_width = 640
    frame_height = 480
    frame = cv2.resize(frame, (frame_width, frame_height))

    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
        center_of_box = ((xA + xB)//2, (yA + yB)//2)
        center_of_frame = (frame_width//2, frame_height//2)
        #decide how long the line is
        line_length = math.sqrt( (center_of_box[0] - center_of_frame[0])**2 + (center_of_box[1] - center_of_frame[1])**2 )
        #draw red or green line if it's too close or not
        if line_length < 200:
            # draw red line
            cv2.line(frame, center_of_box, center_of_frame, (0, 0, 255), 3)
        else:
            #draw green line
            cv2.line(frame, center_of_box, center_of_frame, (0, 255, 0), 3)
            
    
    # Write the output video 
    out.write(frame.astype('uint8'))
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
# and release the output
out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)