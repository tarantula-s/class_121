# import cv2 to capture videofeed
import cv2

import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(0)

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
mountain = cv2.imread('mount everest.jpg')

# resizing the mountain image as 640 X 480
resized_image = mountain.resize(640,480)

while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([0,120,50])
        upper_bound = np.array([10,255,255])
        # thresholding image
        mountain.threshold(lower_bound , upper_bound)
        # inverting the mask
        mountain = cv2.bitwise_not(mountain)
        # bitwise and operation to extract foreground / person
        cv2.bitwise_and(src1, src2, mask)
        # final image
        final_output = cv2.addWeighted(res_1,1,res_2,1,0)
        # show it
        cv2.imshow('frame' , frame)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
