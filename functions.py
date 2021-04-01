import cv2
import numpy as np
import math


# Segment the part containing Green Leaf from Image
def segmentation(img):

        GRAY_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(GRAY_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        img_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
        img_contours = sorted(img_contours, key=cv2.contourArea)
        for i in img_contours:
            if cv2.contourArea(i) > 100:
                break

        mask = np.zeros(img.shape[:2], np.uint8)
        cv2.drawContours(mask, [i], -1, 255, -1)
        new_img = cv2.bitwise_and(img, img, mask=mask)
        return new_img







# Apply contrasting to the image to make colors more clear

def contrasting(new_img):
    alpha = 1.2
    beta = 1.5
    adjusted = cv2.convertScaleAbs(new_img,new_img, alpha=alpha, beta=beta)
    return new_img






# Convert RGB image to HSI image to find and detect perfect green color Range 

def RGB_TO_HSI(img):

    with np.errstate(divide='ignore', invalid='ignore'):

        #Load image with 32 bit floats as variable type
        bgr = np.float32(img)/255

        #Separate color channels
        blue = bgr[:,:,0]
        green = bgr[:,:,1]
        red = bgr[:,:,2]

        #Calculate Intensity
        def calc_intensity(red, blue, green):
            return np.divide(blue + green + red, 3)

        #Calculate Saturation
        def calc_saturation(red, blue, green):
            minimum = np.minimum(np.minimum(red, green), blue)
            saturation = 1 - (3 / (red + green + blue + 0.001) * minimum)

            return saturation

        #Calculate Hue
        def calc_hue(red, blue, green):
            hue = np.copy(red)

            for i in range(0, blue.shape[0]):
                for j in range(0, blue.shape[1]):
                    hue[i][j] = 0.5 * ((red[i][j] - green[i][j]) + (red[i][j] - blue[i][j])) / \
                                math.sqrt((red[i][j] - green[i][j])**2 +
                                        ((red[i][j] - blue[i][j]) * (green[i][j] - blue[i][j])))
                    hue[i][j] = math.acos(hue[i][j])

                    if blue[i][j] <= green[i][j]:
                        hue[i][j] = hue[i][j]
                    else:
                        hue[i][j] = ((360 * math.pi) / 180.0) - hue[i][j]

            return hue

        #Merge channels into picture and return image
        hsi = cv2.merge((calc_hue(red, blue, green), calc_saturation(red, blue, green), calc_intensity(red, blue, green)))
        return hsi






# Remove all grreen Pixels from the image to get only damaged part of the leaf

def damaged_only(img):

   # img = cv2.imread(contrasted_img)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    upper_gree=np.array([80,255,255])
    lower_gree=np.array([35,0,0])
    mask=cv2.inRange(hsv,lower_gree,upper_gree)
    final=cv2.bitwise_and(img,img,mask=mask)
    defected = cv2.subtract(img , final)
    return defected



