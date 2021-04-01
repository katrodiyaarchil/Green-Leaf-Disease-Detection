import cv2
import functions

# Read the image
img = cv2.imread('taken.jfif')

# Segment the leaf
segmented = functions.segmentation(img)

# Apply contrasting
contrasted_img = functions.contrasting(segmented)

# RGB to HSI conversion
hsi= functions.RGB_TO_HSI(contrasted_img)

# Damaged part only
damaded_only = functions.damaged_only(contrasted_img)

hsi2=functions.RGB_TO_HSI(damaded_only)

cv2.imshow('original',img)
cv2.imshow('segmented',segmented)
cv2.imshow('contrasted',contrasted_img)
cv2.imshow('HSI',hsi)
cv2.imshow('damaged only',damaded_only)
cv2.imshow('Damaged HSI', hsi2)
cv2.waitKey(0)
